name: generate-qa-artifacts-from-requirements
description: >
Generate QA deliverables (scenarios, variants, data, scripts, plan, RTM) from
requirement/specification documents. Use when you have requirements, specs,
user stories or acceptance criteria and need to automate QA artifact generation.
Generate QA Artifacts from Requirements
This skill automates the creation of a full suite of Quality Assurance artifacts based on provided requirements documents.
Instructions
Follow this workflow precisely. Create a deliverables/ directory to store all outputs.
CRITICAL PRINCIPLE: This skill prioritizes EXHAUSTIVE generation first, OPTIMIZATION second. Generate ALL content completely before any reduction happens via combinatorial analysis.

Acknowledge and Prepare:

Confirm you have understood the request.
Ask the user to upload all their requirements and specification documents.
Ask the user if they want to use a custom output directory or use the default `deliverables/` directory.

**HANDLE LARGE PDF FILES:**

If the user provides PDF files, check if they might be too large for LLM processing:
- Run the PDF chunking script to analyze the file:
  ```bash
  python3 skill/scripts/chunk_large_pdf.py <pdf_file>
  ```
- The script will automatically detect if chunking is needed based on:
  - File size (>5 MB)
  - Page count (>50 pages)
  - Character count (>100,000 chars)

**If chunking is NOT needed:**
- Script will report "No chunking needed"
- Process the PDF normally

**If chunking IS needed:**
- Script will automatically create chunks in `<pdf_name>_chunks/` directory
- Chunks are saved as text files with page number preservation
- Review the `00_CHUNKING_SUMMARY.txt` file for chunk details
- **Processing Strategy**: When extracting requirements (Step 2), process chunks sequentially:
  1. Read chunk_001_pages_X-Y.txt
  2. Extract requirements with page number references
  3. Move to chunk_002_pages_X-Y.txt
  4. Continue until all chunks processed
  5. Combine requirements from all chunks into single 00_requirements.md

**Chunking Options:**
```bash
# Auto-detect and chunk if needed (recommended)
python3 skill/scripts/chunk_large_pdf.py requirements.pdf

# Force chunking with specific strategy
python3 skill/scripts/chunk_large_pdf.py requirements.pdf --strategy pages --pages-per-chunk 10

# Custom output directory
python3 skill/scripts/chunk_large_pdf.py requirements.pdf --output custom_chunks/
```

**Available Strategies:**
- `auto` - Automatically select best strategy (default)
- `pages` - Chunk by page count (good for very large PDFs)
- `size` - Chunk by character count (consistent sizing)
- `sections` - Chunk by detected headings/sections (best quality, preserves logical structure)

Once they are provided, handle the output directory:
- **Set OUTPUT_DIR variable**: If user specified a custom directory, use it (e.g., `custom_output/`). Otherwise, use `deliverables/`
- **If OUTPUT_DIR does NOT exist**: Create OUTPUT_DIR and OUTPUT_DIR/06_test_scripts/
- **If OUTPUT_DIR EXISTS**:
  - Ask user: "Output directory 'OUTPUT_DIR' already exists. Options: (1) Overwrite, (2) Use timestamped directory (e.g., OUTPUT_DIR_20251114_225805/), (3) Cancel"
  - Based on user choice:
    - Overwrite: Remove existing OUTPUT_DIR and create fresh directories
    - Timestamped: Create OUTPUT_DIR_YYYYMMDD_HHMMSS/ and update OUTPUT_DIR variable and all subsequent paths
    - Cancel: Stop and wait for user to manually handle the directory

Set expectations: Tell the user this process generates exhaustive content first, then optimizes.
Confirm the final output directory path being used (e.g., "All artifacts will be saved to: deliverables/")

**RESUME CAPABILITY - Check for Existing Outputs:**

Before starting the workflow, check if OUTPUT_DIR contains any existing artifacts from a previous run. This allows resuming from failures without redoing completed work.

**Checkpoint Detection:**
- Check for these key files in OUTPUT_DIR:
  - `01_requirements_assessment.md` (Step 1 complete)
  - `00_requirements.md` (Step 2 complete)
  - `02_entities_and_flows.md` (Step 3 complete)
  - `03_test_scenarios.md` (Step 4 complete)
  - **NEW**: `scenarios/` directory with TS-* folders containing variants.csv (Step 5 complete)
  - **NEW**: `scenarios/` directory with TS-* folders containing test_data.csv (Step 6 complete)
  - **NEW**: `scenarios/` directory with TS-* folders containing scripts/ directories with files (Step 7 complete)
  - **NEW**: `scenarios/` directory with TS-* folders containing combinatorial_plan.md (Step 8 complete)
  - `08_test_plan.md` (Step 9 complete)
  - `09_rtm.csv` (Step 10 complete)

**Legacy Checkpoint Detection** (for older projects):
  - `04_variants.csv` (Step 5 complete - legacy monolithic mode)
  - `05_test_data.csv` (Step 6 complete - legacy monolithic mode)
  - `06_test_scripts/` directory with files (Step 7 complete - legacy monolithic mode)
  - `07_combinatorial_plan.md` (Step 8 complete - legacy monolithic mode)

**Resume Logic:**
If ANY files exist, ask the user: "Found existing artifacts from a previous run. Options:
1. **Resume from last completed step** (skip completed steps, start from first missing output)
2. **Regenerate specific step** (keep previous steps, regenerate one step)
3. **Start fresh** (delete all existing artifacts and start from Step 1)
4. **Cancel** (stop and let user manually handle the situation)"

**If user chooses "Resume":**
- Identify the last completed step based on existing files
- Report: "Resuming from Step X. Steps 1-Y are complete and will be skipped."
- Start workflow from the first incomplete step
- Reuse existing artifacts for subsequent steps (e.g., use existing 00_requirements.md for RTM generation)

**If user chooses "Regenerate specific step":**
- Ask: "Which step number would you like to regenerate? (1-10)"
- Regenerate only that step
- Keep all other artifacts unchanged
- Warn if downstream steps depend on this (e.g., regenerating Step 4 scenarios should trigger regenerating Steps 7, 10)

**If user chooses "Start fresh":**
- Proceed with normal workflow (directory handling as specified above)


Step 1: Assess Requirements:

Carefully read all the provided requirement documents.
Analyze them for gaps, ambiguities, contradictions, and unstated assumptions.
Synthesize your findings into a markdown file named OUTPUT_DIR/01_requirements_assessment.md.

**GIT CHECKPOINT - Commit Step 1:**
```bash
git add OUTPUT_DIR/01_requirements_assessment.md
git commit -m "Complete Step 1: Requirements assessment"
```


Step 2: Extract and Number Requirements:

**CRITICAL: Two distinct approaches based on input document type:**

**Approach A: Input Contains Documented Requirements**

If the source document already contains explicitly documented requirements (e.g., numbered requirements, requirement IDs, formal specifications):
- **Extract requirements EXACTLY as documented** - do not deviate from the source
- **Do NOT generate additional requirements** - only use what is explicitly stated in the document
- Preserve original requirement IDs if present, or assign IDs in format: REQ-001, REQ-002, etc.
- Maintain the original structure and grouping from the source document
- **Do NOT add implicit or derived requirements** - stick strictly to what is documented

**Approach B: Input Does NOT Contain Documented Requirements**

If the source document does not contain explicit requirements (e.g., business narrative, use cases, general specifications):
- **Derive requirements from the source content**
- For EACH derived requirement, you MUST include:
  - **Source Page**: Page number where the requirement was derived from
  - **Source Excerpt**: Direct quote or excerpt from the document that supports this requirement
- This provides full traceability back to the source material

**How to Detect Which Approach:**
- **Use Approach A if**: Document contains phrases like "REQ-", "Requirement:", numbered requirements, formal specification sections
- **Use Approach B if**: Document is narrative, descriptive, contains business cases, user stories without formal requirement IDs

**REQUIRED FORMAT (for rtm_builder.py script consumption):**

**Format for Approach A (Documented Requirements):**
```markdown
## [Functional Area Name]

### REQ-001: [Requirement Title from Source]
**Description**: [Exact requirement statement from source document]
**Priority**: Critical|High|Medium|Low
**Type**: Functional|Non-Functional|Security|Performance|Usability
**Affected Roles**: [Comma-separated list of user roles, e.g., "Buyer, Seller, Admin"]

### REQ-002: [Requirement Title from Source]
**Description**: [Exact requirement statement from source document]
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Guest
```

**Format for Approach B (Derived Requirements - with source citations):**
```markdown
## [Functional Area Name]

### REQ-001: [Derived Requirement Title]
**Description**: [Clear, concise requirement statement derived from source]
**Priority**: Critical|High|Medium|Low
**Type**: Functional|Non-Functional|Security|Performance|Usability
**Affected Roles**: [Comma-separated list of user roles]
**Source Page**: Page X
**Source Excerpt**: "[Direct quote or excerpt from source document that supports this requirement]"

### REQ-002: [Derived Requirement Title]
**Description**: [Clear, concise requirement statement derived from source]
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Guest
**Source Page**: Page Y
**Source Excerpt**: "[Direct quote or excerpt from source document]"
```

**ALTERNATE FORMATS (also supported):**

For Approach A:
```markdown
## [Functional Area Name]
- **REQ-001**: [Exact requirement from source]
- **REQ-002**: [Exact requirement from source]
```

For Approach B:
```markdown
## [Functional Area Name]
- **REQ-001**: [Derived requirement] (Source: Page X - "[excerpt]")
- **REQ-002**: [Derived requirement] (Source: Page Y - "[excerpt]")
```

**Metadata Field Descriptions:**
- **Priority**: Business priority (Critical, High, Medium, Low) - helps prioritize test execution
- **Type**: Requirement category - helps organize testing by domain
- **Affected Roles**: User roles impacted by this requirement - helps identify stakeholders and test coverage
- **Source Page**: (Approach B only) Page number from source document
- **Source Excerpt**: (Approach B only) Direct quote supporting the derived requirement

**Workflow:**
1. First, analyze the input document to determine which approach (A or B) to use
2. State your decision: "This document contains [documented requirements / narrative content requiring derivation]"
3. If Approach A: Extract requirements exactly as documented, no additions
4. If Approach B: Derive requirements and include source page + excerpt for each one
5. Assign unique IDs in format: REQ-001, REQ-002, etc. (unless source has existing IDs)
6. Group requirements by functional area
7. Save to OUTPUT_DIR/00_requirements.md (numbered 00 to appear first in directory listing)
8. Count and report: State the total number of requirements extracted (e.g., "Extracted 47 requirements from documented specifications" OR "Derived 47 requirements from source narrative with full traceability")
9. This document will be used by Step 10 for Requirements Traceability Matrix generation

**GIT CHECKPOINT - Commit Step 2:**
```bash
git add OUTPUT_DIR/00_requirements.md
git commit -m "Complete Step 2: Extract and number requirements (X requirements)"
```


Step 3: Extract Entities and Flows:

From the requirements, identify and list all key entities (e.g., user roles, system components, data objects) and the primary user/system flows.
Document these in OUTPUT_DIR/02_entities_and_flows.md.
Count and report: State the number of entities and flows identified.

**GIT CHECKPOINT - Commit Step 3:**
```bash
git add OUTPUT_DIR/02_entities_and_flows.md
git commit -m "Complete Step 3: Extract entities and flows (X entities, Y flows)"
```


Step 4: Derive Test Scenarios (EXHAUSTIVE):

Based on the entities and flows, generate an EXHAUSTIVE set of test scenarios.
DO NOT skip scenarios. Cover every requirement, every entity, every flow, every edge case.
Each scenario must follow the user story format: "As a [user role], I want to [perform an action], so that I can [achieve a benefit]."
Assign a unique ID (e.g., TS-001, TS-002) to each scenario.

**REQUIRED FORMAT (for rtm_builder.py script consumption):**
```markdown
### TS-001: [Scenario Title]
As a [user role], I want to [perform an action], so that I can [achieve a benefit].

**Priority**: Critical|High|Medium|Low
**Related Requirements**: REQ-001, REQ-005, REQ-012

[Additional scenario details...]

### TS-002: [Scenario Title]
...
```

**CRITICAL FORMAT REQUIREMENTS:**
- Scenario heading MUST use format: `### TS-XXX: Title`
- Priority field is OPTIONAL but recommended
- **Related Requirements** field is REQUIRED - list all requirement IDs this scenario tests
- Use exact format: `**Related Requirements**: REQ-001, REQ-002` (comma-separated, no line breaks)

Save these to OUTPUT_DIR/03_test_scenarios.md.
VERIFICATION CHECKPOINT: After generating, count the total scenarios and report: "Generated X test scenarios covering Y requirements."
Cross-check: Review OUTPUT_DIR/00_requirements.md to ensure every requirement has at least one scenario. If any are missing, add them now.

**GIT CHECKPOINT - Commit Step 4:**
```bash
git add OUTPUT_DIR/03_test_scenarios.md
git commit -m "Complete Step 4: Generate test scenarios (X scenarios)"
```


Step 5: Define Variants (EXHAUSTIVE - Per-Scenario Architecture):

**CRITICAL IMPROVEMENT**: Variants are now generated **per-scenario** in isolated folders for better organization, maintainability, and scalability.

**NEW ARCHITECTURE BENEFITS:**
- ✅ **Isolation**: Each scenario's variants are self-contained
- ✅ **Modularity**: Add/remove/debug scenarios independently
- ✅ **Scalability**: Linear growth instead of exponential
- ✅ **Clarity**: Folder structure shows what's being tested
- ✅ **Traceability**: Clear path from scenario → variants → data → scripts

**Step 5A: Identify Parameters (Same as Before)**

First, identify ALL parameters that apply across scenarios:
- **User_Type**: All roles (Visitor, Buyer, Seller, Admin, Sub_Admin, etc.)
- **Browser**: Chrome, Firefox, Safari, Edge
- **Device**: Desktop, Mobile, Tablet
- **Network_Speed**: High, Medium, Low
- **Input_Validity**: Valid, Invalid
- **Data_State**: New, Existing, Duplicate, Expired, etc.
- **Auth_Method**: Email/Password, Facebook, Google (if applicable)
- **Payment_Method**: Credit Card, PayPal, Stripe (if applicable)
- And any other scenario-specific parameters

**Step 5B: Generate Variants Per-Scenario Using Automated Script**

Execute the scenario orchestrator to generate variants for all scenarios:

```bash
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps variants \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**What This Does:**
1. Parses `03_test_scenarios.md` to extract all scenario IDs (TS-001, TS-002, etc.)
2. For each scenario:
   - Creates isolated directory: `OUTPUT_DIR/scenarios/TS-XXX_Title/`
   - Generates exhaustive variants using Cartesian product: `variants.csv`
   - Calculates expected variant count
   - Saves scenario metadata: `metrics.json`
3. Provides real-time progress tracking

**Expected Output Structure:**
```
OUTPUT_DIR/scenarios/
├── TS-001_New_Buyer_Registration_with_Email_Verification/
│   ├── variants.csv              (864 variants - isolated to TS-001 only)
│   └── metrics.json              (statistics: variant count, parameters, timestamps)
│
├── TS-002_Registration_with_Invalid_Email_Format/
│   ├── variants.csv              (144 variants - isolated to TS-002 only)
│   └── metrics.json
│
├── TS-010_Checkout_Process_with_Payment/
│   ├── variants.csv              (5,184 variants - isolated to TS-010 only)
│   └── metrics.json
│
└── ... (one folder per scenario)
```

**Example Calculation (Same Math, Different Organization):**

**TS-001 Variants (in TS-001_New_Buyer_Registration/ folder):**
```
Parameters:
- User_Type: 1 value (Visitor)
- Input_Validity: 2 values (Valid, Invalid)
- Field_Values: 12 values (All_Valid, Missing_FirstName, Missing_Email, etc.)
- Browser: 4 values (Chrome, Firefox, Safari, Edge)
- Device: 3 values (Desktop, Mobile, Tablet)
- Network_Speed: 3 values (High, Medium, Low)

Total TS-001 variants = 1 × 2 × 12 × 4 × 3 × 3 = 864 variants
Saved to: OUTPUT_DIR/scenarios/TS-001_New_Buyer_Registration/variants.csv
```

**TS-010 Variants (in TS-010_Checkout_Process/ folder):**
```
Parameters:
- User_Type: 2 values (Buyer, Guest)
- Input_Validity: 2 values (Valid, Invalid)
- Payment_Method: 3 values (Credit_Card, PayPal, Stripe)
- Shipping_Address: 3 values (New, Existing, Invalid)
- Cart_State: 4 values (Single_Item, Multiple_Items, Max_Quantity, Out_Of_Stock)
- Browser: 4 values
- Device: 3 values
- Network_Speed: 3 values

Total TS-010 variants = 2 × 2 × 3 × 3 × 4 × 4 × 3 × 3 = 5,184 variants
Saved to: OUTPUT_DIR/scenarios/TS-010_Checkout_Process/variants.csv
```

**Expected Scale (Per Scenario):**
- Simple scenarios: 100-500 variants per folder
- Moderate scenarios: 500-2,000 variants per folder
- Complex scenarios: 2,000-10,000 variants per folder

**Expected Scale (Total Across All Scenarios):**
- Small application (20 scenarios): 10,000-25,000 total variants
- Moderate application (100 scenarios): 25,000-75,000 total variants
- Large application (200+ scenarios): 75,000-200,000+ total variants

**Per-Scenario CSV Format:**

Each `variants.csv` file contains ONLY variants for that scenario:

```csv
Scenario_ID,Variant_ID,User_Type,Input_Validity,Field_Values,Browser,Device,Network_Speed
TS-001,V00001,Visitor,Valid,All_Valid,Chrome,Desktop,High
TS-001,V00002,Visitor,Valid,All_Valid,Chrome,Desktop,Medium
TS-001,V00003,Visitor,Valid,All_Valid,Chrome,Desktop,Low
...
TS-001,V00864,Visitor,Invalid,Terms_Not_Accepted,Edge,Tablet,Low
```

**CRITICAL FORMAT REQUIREMENTS (unchanged):**
- Use exact column names: `Scenario_ID` and `Variant_ID` (case-sensitive)
- Variant IDs use 5-digit zero-padded format: V00001, V00002, etc.
- Use "N/A" for parameters that don't apply
- NO empty cells - use "N/A" instead
- Parameter values should be consistent

**PROGRESS TRACKING:**

The orchestrator provides real-time updates:
```
Scenario Orchestration - Variants Generation
============================================================
Output Directory: deliverables/scenarios
Total Scenarios: 106
Selected Steps: variants

[1/106] TS-001: New Buyer Registration
  ✓ Generated 864 variants
  Output: deliverables/scenarios/TS-001_New_Buyer_Registration/variants.csv

[2/106] TS-002: Invalid Email Format
  ✓ Generated 144 variants
  Output: deliverables/scenarios/TS-002_Invalid_Email_Format/variants.csv

...

[106/106] TS-106: Security Testing
  ✓ Generated 36 variants
  Output: deliverables/scenarios/TS-106_Security_Testing/variants.csv

Summary:
  Total Scenarios Processed: 106
  Total Variants Generated: 47,520
  Average Variants per Scenario: 448
  Successful: 106
  Failed: 0
```

**ALTERNATIVE USAGE - Specific Scenarios Only:**

If you only need to generate/regenerate specific scenarios:

```bash
# Generate single scenario
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-001 \
  --steps variants \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios

# Generate specific scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --scenarios TS-001,TS-002,TS-010 \
  --steps variants \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios
```

**VERIFICATION CHECKPOINT:**

After generation completes:

1. **Count total scenarios:**
   ```bash
   ls -d OUTPUT_DIR/scenarios/TS-* | wc -l
   ```
   Should match scenario count from Step 4.

2. **Count total variants across all scenarios:**
   ```bash
   python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios
   ```

3. **View summary report:**
   Check `OUTPUT_DIR/summary/metrics_dashboard.md` for:
   - Total variants across all scenarios
   - Min/max/average variants per scenario
   - Scenarios with missing artifacts

4. **Spot-check individual scenario:**
   ```bash
   # View TS-001 metrics
   cat OUTPUT_DIR/scenarios/TS-001_*/metrics.json

   # Count TS-001 variants
   wc -l OUTPUT_DIR/scenarios/TS-001_*/variants.csv
   ```

5. **Report Results:**
   - "Generated X variants across Y scenarios"
   - "Average Z variants per scenario"
   - "Min: A variants (TS-XXX), Max: B variants (TS-YYY)"
   - "All scenario folders created successfully"

**If variant count seems too low (<5,000 for moderate app), YOU HAVE NOT GENERATED THE FULL CARTESIAN PRODUCT. Regenerate specific scenarios with --force flag.**

**BACKWARDS COMPATIBILITY:**

The old monolithic approach is still supported via legacy mode:

```bash
python3 skill/scripts/generate_variants.py \
  --monolithic \
  --output OUTPUT_DIR/04_variants.csv
```

However, the **per-scenario approach is strongly recommended** for all new projects.

**GIT CHECKPOINT - Commit Step 5:**
```bash
git add OUTPUT_DIR/scenarios/
git commit -m "Complete Step 5: Generate exhaustive variants per-scenario (X total variants across Y scenarios)"
```


Step 6: Create Test Data (EXHAUSTIVE - Per-Scenario):

**CRITICAL IMPROVEMENT**: Test data is now generated **per-scenario** to match the new variants architecture.

Generate test data for each scenario's variants using the orchestrator:

```bash
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps test-data \
  --output-dir OUTPUT_DIR/scenarios
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**What This Does:**
1. For each scenario directory in `OUTPUT_DIR/scenarios/`:
   - Reads the scenario's `variants.csv`
   - Generates realistic test data for EACH variant (one variant = one data row)
   - Saves to `test_data.csv` in the same scenario folder
   - Updates `metrics.json` with test data statistics
2. Provides real-time progress tracking

**Expected Output Structure:**
```
OUTPUT_DIR/scenarios/
├── TS-001_New_Buyer_Registration/
│   ├── variants.csv              (864 variants)
│   ├── test_data.csv             (864 rows - NEW)
│   └── metrics.json              (updated with test data count)
│
├── TS-002_Invalid_Email_Format/
│   ├── variants.csv              (144 variants)
│   ├── test_data.csv             (144 rows - NEW)
│   └── metrics.json
│
└── ... (test_data.csv in each scenario folder)
```

**Per-Scenario Test Data Format:**

Each `test_data.csv` contains realistic data for that scenario's variants:

```csv
Variant_ID,First_Name,Last_Name,Email,Password,Phone,Browser,Device,Network_Speed
V00001,John,Smith,john.smith@example.com,SecurePass123!,+1-555-0101,Chrome,Desktop,High
V00002,Jane,Doe,jane.doe@example.com,AnotherPass456!,+1-555-0102,Chrome,Desktop,Medium
V00003,Bob,Johnson,bob.j@test.com,MyPassword789!,+1-555-0103,Chrome,Desktop,Low
...
V00864,Alice,Williams,alice.w@demo.com,TestPass321!,+1-555-0864,Edge,Tablet,Low
```

**PROGRESS TRACKING:**

The orchestrator provides real-time updates:
```
Scenario Orchestration - Test Data Generation
============================================================
Output Directory: deliverables/scenarios
Total Scenarios: 106
Selected Steps: test-data

[1/106] TS-001: New Buyer Registration
  Reading variants from: TS-001_New_Buyer_Registration/variants.csv
  ✓ Generated 864 test data rows
  Output: TS-001_New_Buyer_Registration/test_data.csv

[2/106] TS-002: Invalid Email Format
  Reading variants from: TS-002_Invalid_Email_Format/variants.csv
  ✓ Generated 144 test data rows
  Output: TS-002_Invalid_Email_Format/test_data.csv

...

[106/106] TS-106: Security Testing
  ✓ Generated 36 test data rows
  Output: TS-106_Security_Testing/test_data.csv

Summary:
  Total Scenarios Processed: 106
  Total Test Data Rows: 47,520
  Successful: 106
  Failed: 0
```

**ALTERNATIVE USAGE - Specific Scenarios Only:**

Generate test data for specific scenarios only:

```bash
# Single scenario
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-001 \
  --steps test-data \
  --output-dir OUTPUT_DIR/scenarios

# Multiple scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --scenarios TS-001,TS-002,TS-010 \
  --steps test-data \
  --output-dir OUTPUT_DIR/scenarios
```

**VERIFICATION CHECKPOINT:**

After generation completes:

1. **Verify all scenarios have test data:**
   ```bash
   # Count test_data.csv files
   find OUTPUT_DIR/scenarios -name "test_data.csv" | wc -l
   ```
   Should match scenario count.

2. **Verify row counts match variants:**
   ```bash
   # Check TS-001 specifically
   echo "Variants: $(wc -l < OUTPUT_DIR/scenarios/TS-001_*/variants.csv)"
   echo "Test Data: $(wc -l < OUTPUT_DIR/scenarios/TS-001_*/test_data.csv)"
   ```
   Counts should match (excluding header row).

3. **View aggregate statistics:**
   ```bash
   python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios
   cat OUTPUT_DIR/summary/metrics_dashboard.md
   ```

4. **Report Results:**
   - "Generated test data for X scenarios"
   - "Total test data rows: Y"
   - "All variants have corresponding test data"

**DATA VALIDATION (Per-Scenario):**

Validate test data quality for each scenario:

```bash
# Validate all scenarios
python3 skill/scripts/validate_test_data.py \
  --scenarios-dir OUTPUT_DIR/scenarios \
  --all

# Validate specific scenario
python3 skill/scripts/validate_test_data.py \
  --scenario-dir OUTPUT_DIR/scenarios/TS-001_New_Buyer_Registration
```

**The validation script checks:**
- Row count matches between variants and test data (per scenario)
- All Variant_IDs are present in both files
- Parameter consistency (test data reflects variant parameters)
- Data completeness (no empty critical fields)
- Data realism (valid emails, phone numbers, etc.)

**Expected output:**
- ✅ "All scenarios validated successfully!" - Continue to next step
- ❌ "Validation failed for X scenarios" - Fix errors before proceeding:
  - Missing test data rows: Regenerate data for specific scenarios
  - Row count mismatch: Check variants.csv and test_data.csv line counts
  - Empty fields: Review data generation logic

Quality check: Ensure data is realistic, valid, and matches the variant parameters.

**BACKWARDS COMPATIBILITY:**

The old monolithic approach is still supported:

```bash
python3 skill/scripts/generate_test_data.py \
  --monolithic \
  --variants OUTPUT_DIR/04_variants.csv \
  --output OUTPUT_DIR/05_test_data.csv
```

However, the **per-scenario approach is strongly recommended** for all new projects.

**GIT CHECKPOINT - Commit Step 6:**
```bash
git add OUTPUT_DIR/scenarios/*/test_data.csv OUTPUT_DIR/scenarios/*/metrics.json
git commit -m "Complete Step 6: Generate test data per-scenario (X total rows across Y scenarios)"
```


Step 7: Generate Test Scripts (AUTOMATED - Per-Scenario):

**CRITICAL IMPROVEMENT**: Test scripts are now generated **per-scenario** in isolated folders, matching the new architecture.

**How It Works:**
- Reads test scenarios from `03_test_scenarios.md` to understand what to test
- For each scenario, reads variants and test data from scenario folder
- **Automatically generates** one test script per variant in scenario's `scripts/` folder
- Uses intelligent templates based on scenario type (Registration, Login, Checkout, etc.)
- Injects specific test data and parameters into GIVEN/WHEN/THEN sections

**Benefits:**
- ✅ **100% automated** - no manual LLM script writing
- ✅ **Perfect consistency** - no quality degradation across thousands of scripts
- ✅ **Instant generation** - generates 25,000-75,000 scripts in seconds
- ✅ **Isolated by scenario** - easy to find, debug, and manage scripts
- ✅ **Maintainable** - update templates, regenerate all or specific scenarios

**Execute the orchestrator:**

```bash
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps scripts \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**Expected Output Structure:**
```
OUTPUT_DIR/scenarios/
├── TS-001_New_Buyer_Registration/
│   ├── variants.csv
│   ├── test_data.csv
│   ├── scripts/                  (NEW - 864 scripts)
│   │   ├── TS-001_V00001.txt
│   │   ├── TS-001_V00002.txt
│   │   ├── TS-001_V00003.txt
│   │   └── ... (864 total)
│   └── metrics.json              (updated with script count)
│
├── TS-002_Invalid_Email_Format/
│   ├── variants.csv
│   ├── test_data.csv
│   ├── scripts/                  (NEW - 144 scripts)
│   │   ├── TS-002_V00001.txt
│   │   ├── TS-002_V00002.txt
│   │   └── ... (144 total)
│   └── metrics.json
│
└── ... (scripts/ folder in each scenario)
```

**File Naming Convention (unchanged):**
- Format: `TS-XXX_VXXXXX.txt` where:
  - `TS-XXX` = Scenario ID (e.g., TS-001)
  - `VXXXXX` = Variant ID with zero-padding (e.g., V00001, V00002)
- Example: `TS-001_V00001.txt` = Registration scenario, variant 1 (Chrome/Desktop/Valid)
- Example: `TS-001_V00864.txt` = Registration scenario, variant 864 (Edge/Tablet/Invalid)

**Script Content Format (unchanged):**
Each generated script contains:
- **Header**: Scenario title, variant ID, priority, description
- **GIVEN**: Specific preconditions based on variant parameters
- **WHEN**: Specific actions with concrete test data from CSV
- **THEN**: Specific assertions based on input validity
- **EXPECTED RESULT**: Detailed outcomes with verification steps
- **VARIANT PARAMETERS**: All parameter values for this variant
- **TEST DATA**: All test data fields for this variant
- **RELATED REQUIREMENTS**: Traceability to requirements

**PROGRESS TRACKING:**

The orchestrator provides real-time updates:
```
Scenario Orchestration - Test Scripts Generation
============================================================
Output Directory: deliverables/scenarios
Scenarios File: deliverables/03_test_scenarios.md
Total Scenarios: 106
Selected Steps: scripts

[1/106] TS-001: New Buyer Registration
  Reading variants: TS-001_New_Buyer_Registration/variants.csv (864 variants)
  Reading test data: TS-001_New_Buyer_Registration/test_data.csv (864 rows)
  ✓ Generated 864 test scripts
  Output: TS-001_New_Buyer_Registration/scripts/

[2/106] TS-002: Invalid Email Format
  Reading variants: TS-002_Invalid_Email_Format/variants.csv (144 variants)
  Reading test data: TS-002_Invalid_Email_Format/test_data.csv (144 rows)
  ✓ Generated 144 test scripts
  Output: TS-002_Invalid_Email_Format/scripts/

...

[106/106] TS-106: Security Testing
  ✓ Generated 36 test scripts
  Output: TS-106_Security_Testing/scripts/

Summary:
  Total Scenarios Processed: 106
  Total Test Scripts Generated: 47,520
  Generation Speed: ~1,850 scripts/sec
  Total Time: 25.7 seconds
  Successful: 106
  Failed: 0
```

**ALTERNATIVE USAGE - Specific Scenarios Only:**

Generate scripts for specific scenarios only:

```bash
# Single scenario
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-001 \
  --steps scripts \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios

# Multiple scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --scenarios TS-001,TS-002,TS-010 \
  --steps scripts \
  --scenarios-file OUTPUT_DIR/03_test_scenarios.md \
  --output-dir OUTPUT_DIR/scenarios
```

**VERIFICATION CHECKPOINT:**

After generation completes:

**1. Quantity Check:**
```bash
# Count total scripts across all scenarios
find OUTPUT_DIR/scenarios -name "*.txt" -type f | wc -l

# Count scripts for specific scenario
ls OUTPUT_DIR/scenarios/TS-001_*/scripts/*.txt | wc -l

# View aggregate statistics
python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios
cat OUTPUT_DIR/summary/metrics_dashboard.md
```

**2. Quality Spot-Check (10 random scripts):**

Sample random scripts from different scenarios to verify template quality:

```bash
# View random scripts from TS-001
ls OUTPUT_DIR/scenarios/TS-001_*/scripts/TS-001_V*.txt | shuf | head -3 | xargs cat

# Check scripts contain variant-specific data (not placeholders)
grep -l "Chrome" OUTPUT_DIR/scenarios/TS-001_*/scripts/*.txt | head -5

# Verify no placeholder text remains
grep -r "scenario NN\|TODO\|PLACEHOLDER" OUTPUT_DIR/scenarios/*/scripts/ || echo "✓ No placeholders found"
```

**3. Verify Script Quality Criteria:**
- ✓ Contains specific scenario details (not generic "scenario NN")
- ✓ GIVEN section has concrete conditions (user email, device, browser)
- ✓ WHEN section has concrete test data values from CSV
- ✓ THEN section has specific assertions
- ✓ EXPECTED RESULT has measurable outcomes
- ✓ Variant parameters and test data are populated

**4. Report Results:**
- "Generated X test scripts across Y scenarios"
- "Generation speed: Z scripts/second"
- "Spot-checked 10 random scripts - all contain specific variant data"
- "Quality verification complete - programmatic generation ensures consistency"

**If Issues Found:**
- **Missing scripts**: Verify variants.csv and test_data.csv exist for the scenario
- **Generic scripts**: Check that test data is being read correctly
- **Wrong scenario details**: Verify 03_test_scenarios.md has correct scenario descriptions

**BACKWARDS COMPATIBILITY:**

The old monolithic approach is still supported:

```bash
python3 skill/scripts/generate_test_scripts_from_variants.py \
  OUTPUT_DIR/03_test_scenarios.md \
  OUTPUT_DIR/04_variants.csv \
  OUTPUT_DIR/05_test_data.csv \
  -o OUTPUT_DIR/06_test_scripts
```

However, the **per-scenario approach is strongly recommended** for all new projects.

**GIT CHECKPOINT - Commit Step 7:**
```bash
git add OUTPUT_DIR/scenarios/*/scripts/ OUTPUT_DIR/scenarios/*/metrics.json
git commit -m "Complete Step 7: Generate test scripts per-scenario (X total scripts across Y scenarios)"
```


Step 8: Produce Combinatorial Plan (OPTIMIZATION - Per-Scenario):

**THIS IS WHERE THE MAGIC HAPPENS**: You have generated 25,000-75,000 exhaustive variants across all scenarios. Now optimize **each scenario independently** to reduce to ~500-2,000 total optimized test cases while maintaining 95%+ pairwise coverage per scenario.

**CRITICAL IMPROVEMENT**: Combinatorial optimization is now performed **per-scenario** for better flexibility and precision.

**Benefits of Per-Scenario Optimization:**
- ✅ **Independent optimization**: Different scenarios can have different optimization targets
- ✅ **Better coverage**: Complex scenarios get more test cases, simple ones get fewer
- ✅ **Easier debugging**: Issues isolated to specific scenario optimizations
- ✅ **Flexible**: Can reoptimize individual scenarios without affecting others

**Execute the orchestrator:**

```bash
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps combinatorial \
  --output-dir OUTPUT_DIR/scenarios
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**What This Does:**
1. For each scenario directory:
   - Reads the scenario's `variants.csv`
   - Analyzes parameter pair combinations
   - Selects optimal subset achieving 95%+ pairwise coverage
   - Saves optimization plan to `combinatorial_plan.md`
   - Updates `metrics.json` with optimization statistics
2. Provides real-time progress tracking with reduction percentages

**Expected Output Structure:**
```
OUTPUT_DIR/scenarios/
├── TS-001_New_Buyer_Registration/
│   ├── variants.csv              (864 exhaustive variants)
│   ├── test_data.csv
│   ├── scripts/
│   ├── combinatorial_plan.md     (NEW - optimization details)
│   └── metrics.json              (updated with optimized count: ~42 test cases)
│
├── TS-002_Invalid_Email_Format/
│   ├── variants.csv              (144 exhaustive variants)
│   ├── test_data.csv
│   ├── scripts/
│   ├── combinatorial_plan.md     (NEW - ~18 test cases)
│   └── metrics.json
│
├── TS-010_Checkout_Process/
│   ├── variants.csv              (5,184 exhaustive variants)
│   ├── combinatorial_plan.md     (NEW - ~127 test cases)
│   └── metrics.json
│
└── ... (combinatorial_plan.md in each scenario folder)
```

**How Combinatorial Optimization Works (unchanged):**
- Analyzes all parameter pairs in scenario's exhaustive variants
- Selects a minimal subset covering 95%+ of all possible parameter pair interactions
- Example: For 864 variants → selects ~42 that cover all critical parameter combinations
- Foundation of "pairwise testing" - research shows 70-90% of bugs are caused by single parameters or pairs

**Expected Results Per Scenario:**

| Scenario Complexity | Input Variants | Expected Output | Expected Reduction | Expected Coverage |
|---------------------|----------------|-----------------|-------------------|-------------------|
| Simple | 100-500 | 10-25 | 90-95% | 95-100% |
| Moderate | 500-2,000 | 25-75 | 92-96% | 95-100% |
| Complex | 2,000-10,000 | 75-300 | 95-98% | 95-100% |

**Expected Results Overall:**

| Total Input Variants | Expected Total Output | Expected Reduction | Average Coverage |
|----------------------|----------------------|-------------------|------------------|
| 10,000-25,000 | 300-800 | 92-97% | 95-100% |
| 25,000-75,000 | 800-2,000 | 95-98% | 95-100% |
| 75,000-200,000 | 2,000-5,000 | 97-99% | 95-100% |

**PROGRESS TRACKING:**

The orchestrator provides real-time updates:
```
Scenario Orchestration - Combinatorial Optimization
============================================================
Output Directory: deliverables/scenarios
Total Scenarios: 106
Selected Steps: combinatorial

[1/106] TS-001: New Buyer Registration
  Reading variants: TS-001_New_Buyer_Registration/variants.csv (864 variants)
  Analyzing parameter pairs...
  ✓ Optimized to 42 test cases (95.1% reduction, 98.2% coverage)
  Output: TS-001_New_Buyer_Registration/combinatorial_plan.md

[2/106] TS-002: Invalid Email Format
  Reading variants: TS-002_Invalid_Email_Format/variants.csv (144 variants)
  ✓ Optimized to 18 test cases (87.5% reduction, 96.8% coverage)
  Output: TS-002_Invalid_Email_Format/combinatorial_plan.md

[10/106] TS-010: Checkout Process
  Reading variants: TS-010_Checkout_Process/variants.csv (5,184 variants)
  Analyzing parameter pairs...
  ✓ Optimized to 127 test cases (97.5% reduction, 97.1% coverage)
  Output: TS-010_Checkout_Process/combinatorial_plan.md

...

[106/106] TS-106: Security Testing
  ✓ Optimized to 12 test cases (66.7% reduction, 95.5% coverage)
  Output: TS-106_Security_Testing/combinatorial_plan.md

Summary:
  Total Exhaustive Variants: 47,520
  Total Optimized Test Cases: 1,892
  Overall Reduction: 96.0%
  Average Coverage: 97.1%
  Min Coverage: 95.5% (TS-106)
  Max Coverage: 99.8% (TS-035)
  Successful: 106
  Failed: 0
```

**ALTERNATIVE USAGE - Specific Scenarios Only:**

Optimize specific scenarios only:

```bash
# Single scenario
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-001 \
  --steps combinatorial \
  --output-dir OUTPUT_DIR/scenarios

# Multiple scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --scenarios TS-001,TS-010,TS-035 \
  --steps combinatorial \
  --output-dir OUTPUT_DIR/scenarios
```

**VERIFICATION CHECKPOINT:**

After optimization completes:

**1. Review Individual Scenario Optimization:**
```bash
# View TS-001 combinatorial plan
cat OUTPUT_DIR/scenarios/TS-001_*/combinatorial_plan.md

# Check TS-001 metrics
cat OUTPUT_DIR/scenarios/TS-001_*/metrics.json
```

**2. View Aggregate Summary:**
```bash
python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios
cat OUTPUT_DIR/summary/metrics_dashboard.md
```

**3. Verify Expected Performance:**

For each scenario:
- Reduction should be 85-98% (varies by complexity)
- Pairwise coverage should be 95%+
- Optimized count should be manageable (10-300 test cases per scenario)

Overall:
- Total reduction: 90-96%
- Average coverage: 95%+
- Total optimized test cases: Reasonable for execution (500-2,000 total)

**4. Report Results:**
- "Combinatorial analysis completed for X scenarios"
- "Total exhaustive variants: Y"
- "Total optimized test cases: Z (W% reduction)"
- "Average pairwise coverage: V%"
- "Min coverage: A% (TS-XXX), Max coverage: B% (TS-YYY)"

**Example Report:**
```
Combinatorial analysis completed for 106 scenarios
Total exhaustive variants: 47,520
Total optimized test cases: 1,892 (96.0% reduction)
Average pairwise coverage: 97.1%
Min coverage: 95.5% (TS-106), Max coverage: 99.8% (TS-035)
```

**If Results Don't Meet Expectations:**

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Coverage < 95% for a scenario | Too few parameters or variants | Regenerate that scenario with more parameter dimensions |
| Reduction < 50% for a scenario | Input wasn't truly exhaustive | Regenerate that scenario with full Cartesian product |
| Output > 10,000 total | Too many complex scenarios | Review if all scenarios are necessary; consider prioritization |

**Per-Scenario Reoptimization:**

If a specific scenario's optimization is unsatisfactory, regenerate just that scenario:

```bash
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-035 \
  --steps combinatorial \
  --output-dir OUTPUT_DIR/scenarios \
  --force
```

**What Happens Next:**
- Each scenario's `combinatorial_plan.md` contains the optimized variant list
- Exhaustive variants remain in `variants.csv` for documentation
- Summary aggregator creates overall optimization statistics
- Test Plan (Step 9) references both exhaustive and optimized counts

**BACKWARDS COMPATIBILITY:**

The old monolithic approach is still supported:

```bash
python3 skill/scripts/combinatorial.py \
  OUTPUT_DIR/04_variants.csv \
  --output OUTPUT_DIR/07_combinatorial_plan.md
```

However, the **per-scenario approach is strongly recommended** for all new projects.

**GIT CHECKPOINT - Commit Step 8:**
```bash
git add OUTPUT_DIR/scenarios/*/combinatorial_plan.md OUTPUT_DIR/scenarios/*/metrics.json
git commit -m "Complete Step 8: Combinatorial optimization per-scenario (X% reduction, Y% coverage)"
```

9. Step 9: Draft Full Test Plan:
- Synthesize all previous outputs into a comprehensive test plan document.
- The plan should include:
  - **Executive Summary**: Key statistics and overview
  - **Scope and Objectives**: What is being tested and why
  - **Test Approach**: Exhaustive generation + combinatorial optimization methodology
  - **Test Environment Specifications**:
    - **Hardware Requirements**: Server specs, client device requirements (Desktop, Mobile, Tablet configurations)
    - **Software Requirements**:
      - Operating Systems (Windows 10/11, macOS 12+, Ubuntu 20.04+, iOS 14+, Android 10+)
      - Browsers and versions (Chrome 120+, Firefox 121+, Safari 17+, Edge 120+)
      - Database systems and versions (e.g., PostgreSQL 14+, MySQL 8.0+, MongoDB 6.0+)
      - Application server requirements (e.g., Node.js 18+, Python 3.9+, Java 17+)
    - **Network Configuration**: Bandwidth requirements, VPN/proxy settings, CDN configurations
    - **Test Data Requirements**: Database setup, seed data, test user accounts
    - **Third-Party Dependencies**: External APIs, payment gateways, authentication services
    - **Tools and Frameworks**: Test automation tools, monitoring tools, CI/CD pipeline requirements
  - **Schedule and Resource Estimates**: Timeline and staffing needs
  - **Summary of Test Scenarios**: Overview of all test scenarios and variants (both exhaustive and optimized)
  - **Traceability Matrix Summary**: Link to RTM and coverage statistics
  - **Risk Assessment**: Potential risks and mitigation strategies
  - **Entry and Exit Criteria**: When testing can start and when it's considered complete
- Save the document as OUTPUT_DIR/08_test_plan.md.

**GIT CHECKPOINT - Commit Step 9:**
```bash
git add OUTPUT_DIR/08_test_plan.md
git commit -m "Complete Step 9: Draft test plan"
```

10. Step 10: Build Requirements Traceability Matrix (RTM):

Execute the scripts/rtm_builder.py script using the command:

python3 skill/scripts/rtm_builder.py OUTPUT_DIR/03_test_scenarios.md OUTPUT_DIR/00_requirements.md --test-scripts OUTPUT_DIR/06_test_scripts --gap-report --output OUTPUT_DIR/09_rtm.csv

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

- The script will generate a comprehensive RTM with:
  - Requirement-to-scenario mappings
  - Coverage status and statistics
  - Test script availability tracking
  - Gap analysis (uncovered requirements, orphaned scenarios)
- The output will be saved to `OUTPUT_DIR/09_rtm.csv`.
- Gap report (if --gap-report flag used) will be saved to `OUTPUT_DIR/09_rtm_gap_report.md`.
- Review the summary statistics and address any coverage gaps.
- **Report:** "RTM shows X% requirement coverage with Y uncovered requirements and Z orphaned scenarios."
- **Optional flags:**
  - `--gap-report` - Generate detailed gap analysis report (recommended)
  - `--output <path>` - Specify custom output path (REQUIRED when using custom OUTPUT_DIR)
  - `--verbose` - Enable detailed logging

**Expected RTM Output Format:**
```csv
Requirement_ID,Requirement_Description,Priority,Type,Affected_Roles,Test_Scenario_IDs,Test_Script_Available,Coverage_Status,Notes
REQ-001,Users shall be able to log in...,High,Functional,"Buyer, Seller, Admin","TS-007, TS-009, TS-017",Yes,Covered,
REQ-002,Password reset functionality...,High,Security,"All Users","TS-013, TS-014",Yes,Covered,
REQ-003,System performance requirements...,Medium,Performance,N/A,TS-025,Yes,Covered,
```

**Enhanced Metadata Columns:**
- **Priority**: Extracted from requirements document (Critical/High/Medium/Low, or N/A if not specified)
- **Type**: Requirement category (Functional/Non-Functional/Security/Performance/Usability, or N/A if not specified)
- **Affected_Roles**: User roles impacted by this requirement (extracted from requirements, or N/A if not specified)

**GIT CHECKPOINT - Commit Step 10:**
```bash
git add OUTPUT_DIR/09_rtm.csv OUTPUT_DIR/09_rtm_gap_report.md
git commit -m "Complete Step 10: Build RTM (X% coverage)"
```

11. Completion and Summary:
- List all files in OUTPUT_DIR directory with file sizes
- Provide a comprehensive summary with key metrics:
  - Total requirements extracted
  - Total test scenarios generated
  - **Per-Scenario Breakdown**:
    - Total scenario folders created
    - Total variants created (exhaustive, across all scenarios)
    - Total test data rows generated
    - Total test scripts generated
    - Total optimized test cases (from combinatorial analysis across all scenarios)
  - Reduction percentage achieved (overall)
  - Average pairwise coverage percentage
  - Requirements coverage percentage
  - Test artifacts completion status

**Generate Final Summary Report:**
```bash
# Generate comprehensive summary across all scenarios
python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios

# View the summary dashboard
cat OUTPUT_DIR/summary/metrics_dashboard.md

# View scenario index
cat OUTPUT_DIR/summary/scenario_index.json
```

**Expected Output Structure:**
```
OUTPUT_DIR/
├── 00_requirements.md
├── 01_requirements_assessment.md
├── 02_entities_and_flows.md
├── 03_test_scenarios.md
├── 08_test_plan.md
├── 09_rtm.csv
├── 09_rtm_gap_report.md
│
├── scenarios/                       (NEW - per-scenario architecture)
│   ├── TS-001_Title/
│   │   ├── variants.csv
│   │   ├── test_data.csv
│   │   ├── scripts/
│   │   │   ├── TS-001_V00001.txt
│   │   │   └── ... (864 scripts)
│   │   ├── combinatorial_plan.md
│   │   └── metrics.json
│   │
│   ├── TS-002_Title/
│   │   └── ... (same structure)
│   │
│   └── ... (106 scenario folders)
│
└── summary/                        (NEW - aggregate analytics)
    ├── metrics_dashboard.md
    ├── scenario_index.json
    └── (optional) all_variants.csv
```

**Final Verification Checklist:**

✅ **Core Documents:**
- [ ] 00_requirements.md exists and contains all requirements
- [ ] 01_requirements_assessment.md exists
- [ ] 02_entities_and_flows.md exists
- [ ] 03_test_scenarios.md exists and contains all scenarios
- [ ] 08_test_plan.md exists
- [ ] 09_rtm.csv exists
- [ ] 09_rtm_gap_report.md exists

✅ **Per-Scenario Artifacts:**
- [ ] All scenarios have their own folder in OUTPUT_DIR/scenarios/
- [ ] Each scenario folder contains: variants.csv, test_data.csv, scripts/, combinatorial_plan.md, metrics.json
- [ ] Variant counts match expected exhaustive Cartesian products
- [ ] Test data row counts match variant counts
- [ ] Script counts match variant counts
- [ ] Combinatorial plans show 95%+ coverage

✅ **Summary Reports:**
- [ ] OUTPUT_DIR/summary/metrics_dashboard.md exists
- [ ] OUTPUT_DIR/summary/scenario_index.json exists
- [ ] Aggregate metrics look correct

**Verification Commands:**
```bash
# Count scenario folders
ls -d OUTPUT_DIR/scenarios/TS-* | wc -l

# Count total variants
find OUTPUT_DIR/scenarios -name "variants.csv" -exec wc -l {} + | tail -1

# Count total scripts
find OUTPUT_DIR/scenarios -name "*.txt" -type f | wc -l

# Verify no missing artifacts
python3 skill/scripts/summary_aggregator.py --scenarios-dir OUTPUT_DIR/scenarios --validate
```

**Example Summary Report:**
```
QA Artifact Generation Complete!
================================

Core Deliverables:
  ✓ Requirements: 47 requirements extracted
  ✓ Assessment: Gaps and ambiguities documented
  ✓ Entities & Flows: 12 entities, 8 flows identified
  ✓ Test Scenarios: 106 scenarios generated
  ✓ Test Plan: Comprehensive test plan drafted
  ✓ RTM: 98.5% requirement coverage

Per-Scenario Artifacts (NEW Architecture):
  ✓ Scenario Folders: 106 scenarios
  ✓ Exhaustive Variants: 47,520 variants total
    - Simple scenarios: 100-500 variants each
    - Complex scenarios: 2,000-10,000 variants each
  ✓ Test Data: 47,520 realistic data rows
  ✓ Test Scripts: 47,520 automated scripts
  ✓ Combinatorial Optimization: 1,892 optimized test cases
    - Overall Reduction: 96.0%
    - Average Coverage: 97.1%
    - Min Coverage: 95.5%, Max Coverage: 99.8%

All artifacts saved to: OUTPUT_DIR/
```

**Notify the user:**
- All QA artifacts have been generated and are available in the OUTPUT_DIR directory
- Confirm the final output directory path (e.g., "All artifacts saved to: deliverables/")
- Highlight the new scenario-based architecture benefits
- Confirm no gaps or missing artifacts

**FINAL GIT CHECKPOINT - Commit all remaining files:**
```bash
# Add summary reports
git add OUTPUT_DIR/summary/

# Add any remaining files not yet committed
git add OUTPUT_DIR/

# Create final summary commit
git commit -m "Complete QA artifacts generation: $(find OUTPUT_DIR -type f | wc -l) files generated across $(ls -d OUTPUT_DIR/scenarios/TS-* | wc -l) scenarios"

# Optional: Tag this completion
git tag -a "qa-artifacts-$(date +%Y%m%d-%H%M%S)" -m "Completed QA artifact generation with scenario-based architecture"
```

**Report final git status:**
```bash
git log --oneline -11  # Show all 11 commits (10 steps + final)
git status
```