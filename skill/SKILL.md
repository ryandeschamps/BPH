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
  - `04_variants.csv` (Step 5 complete)
  - `05_test_data.csv` (Step 6 complete)
  - `06_test_scripts/` directory with files (Step 7 complete)
  - `07_combinatorial_plan.md` (Step 8 complete)
  - `08_test_plan.md` (Step 9 complete)
  - `09_rtm.csv` (Step 10 complete)

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


Step 5: Define Variants (EXHAUSTIVE):

**CRITICAL**: This step must generate the TRUE EXHAUSTIVE CARTESIAN PRODUCT of all parameters. This is NOT "a few variants per scenario" - this is EVERY POSSIBLE COMBINATION.

**Step 5A: Identify Global Parameters**

First, identify ALL parameters that apply across scenarios (these form the columns of your CSV):
- **User_Type**: All roles (Visitor, Buyer, Seller, Admin, Sub_Admin, etc.)
- **Browser**: Chrome, Firefox, Safari, Edge
- **Device**: Desktop, Mobile, Tablet
- **Network_Speed**: High, Medium, Low
- **Input_Validity**: Valid, Invalid
- **Data_State**: New, Existing, Duplicate, Expired, etc.
- **Auth_Method**: Email/Password, Facebook, Google (if applicable)
- **Payment_Method**: Credit Card, PayPal, Stripe (if applicable)
- And any other scenario-specific parameters

**Step 5B: For EACH Scenario, Generate Full Cartesian Product**

For each scenario (e.g., TS-001: User Registration), calculate the FULL Cartesian product:

**Example Calculation for TS-001:**
```
Parameters applicable to Registration:
- User_Type: 1 value (Visitor only - not logged in yet)
- Input_Validity: 2 values (Valid, Invalid)
- Field_Values: 12 values (All_Valid, Missing_FirstName, Missing_LastName, Missing_Email,
  Invalid_Email, Weak_Password, Password_Mismatch, Duplicate_Email, Invalid_Phone,
  Missing_Phone, Terms_Not_Accepted, etc.)
- Browser: 4 values (Chrome, Firefox, Safari, Edge)
- Device: 3 values (Desktop, Mobile, Tablet)
- Network_Speed: 3 values (High, Medium, Low)

Total TS-001 variants = 1 × 2 × 12 × 4 × 3 × 3 = 864 variants
```

**Example Calculation for TS-010: Checkout Process:**
```
Parameters:
- User_Type: 2 values (Buyer, Guest)
- Input_Validity: 2 values (Valid, Invalid)
- Payment_Method: 3 values (Credit_Card, PayPal, Stripe)
- Shipping_Address: 3 values (New, Existing, Invalid)
- Cart_State: 4 values (Single_Item, Multiple_Items, Max_Quantity, Out_Of_Stock_Item)
- Browser: 4 values
- Device: 3 values
- Network_Speed: 3 values

Total TS-010 variants = 2 × 2 × 3 × 3 × 4 × 4 × 3 × 3 = 5,184 variants
```

**Expected Scale:**
- Small application (20 scenarios): 10,000-25,000 variants
- Moderate application (100 scenarios): 25,000-75,000 variants
- Large application (200+ scenarios): 75,000-200,000+ variants

**Step 5C: Generate Variants Systematically**

Use a systematic approach to ensure NO combinations are missed:

1. For each scenario, list all parameter dimensions
2. Calculate total expected variants (multiply all dimension sizes)
3. Use nested loops or itertools.product() approach to generate ALL combinations
4. Assign sequential Variant_IDs starting from V001

**PROGRESS TRACKING (for long-running generation):**

When generating variants, provide real-time progress updates:
- **Before starting**: Report total scenarios and estimated variants (e.g., "Generating ~50,000 variants for 100 scenarios...")
- **During generation**: Update progress at regular intervals
  - Report every 10-20 scenarios completed (e.g., "Completed 20/100 scenarios - 10,248 variants generated so far")
  - Show percentage complete (e.g., "[25%] Processing scenario TS-025...")
- **After completion**: Report final count and duration (e.g., "✓ Generated 47,520 variants in 2m 15s")

**REQUIRED CSV FORMAT (for combinatorial.py script consumption):**

**Column structure:**
1. First column MUST be: `Scenario_ID` (links to TS-XXX from 03_test_scenarios.md)
2. Second column MUST be: `Variant_ID` (format: V001, V002, V003, etc.)
3. Remaining columns: Parameter names (e.g., User_Type, Browser, Input_Validity, Data_State, etc.)

**Example format showing TRUE exhaustive generation:**
```csv
Scenario_ID,Variant_ID,User_Type,Input_Validity,Field_Values,Browser,Device,Network_Speed
TS-001,V001,Visitor,Valid,All_Valid,Chrome,Desktop,High
TS-001,V002,Visitor,Valid,All_Valid,Chrome,Desktop,Medium
TS-001,V003,Visitor,Valid,All_Valid,Chrome,Desktop,Low
TS-001,V004,Visitor,Valid,All_Valid,Chrome,Mobile,High
TS-001,V005,Visitor,Valid,All_Valid,Chrome,Mobile,Medium
...
TS-001,V864,Visitor,Invalid,Terms_Not_Accepted,Edge,Tablet,Low
TS-002,V865,Buyer,Valid,Valid_Login,Chrome,Desktop,High
...
```

**CRITICAL FORMAT REQUIREMENTS:**
- Use exact column names: `Scenario_ID` and `Variant_ID` (case-sensitive)
- Variant IDs MUST be unique across entire file
- Use "N/A" for parameters that don't apply to certain combinations (e.g., payment_method=N/A for visitor registration)
- NO empty cells - use "N/A" instead
- Parameter values should be consistent (e.g., don't mix "Admin" and "Administrator")
- DO NOT skip combinations - generate ALL of them

**Generation Approach (if using Python helper):**
```python
from itertools import product

# For TS-001:
user_types = ['Visitor']
input_validity = ['Valid', 'Invalid']
field_values = ['All_Valid', 'Missing_FirstName', 'Missing_Email', ...]  # 12 values
browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
devices = ['Desktop', 'Mobile', 'Tablet']
network_speeds = ['High', 'Medium', 'Low']

variants = list(product(user_types, input_validity, field_values, browsers, devices, network_speeds))
# This generates 1×2×12×4×3×3 = 864 combinations automatically
```

Output this as a CSV file to OUTPUT_DIR/04_variants.csv.

**VERIFICATION CHECKPOINT:**
After generating, perform these checks:
1. **Count total variants** and report: "Generated X variants across Y scenarios"
2. **Calculate expected minimum**: Should be 50+ average variants per scenario for true exhaustive
3. **Spot check Cartesian product**: Pick one scenario and verify ALL combinations exist
   - Example: For TS-001 with 4 browsers × 3 devices = verify all 12 browser/device combos exist
4. **Report scale**: "This represents the EXHAUSTIVE set. Step 8 will reduce by ~90-95%"

**If variant count seems too low (<5,000 for moderate app), YOU HAVE NOT GENERATED THE FULL CARTESIAN PRODUCT. Go back and regenerate.**

Note: Step 8 will use combinatorial analysis to reduce this to an optimal subset (~90-95% reduction, achieving 95%+ pairwise coverage).

**GIT CHECKPOINT - Commit Step 5:**
```bash
git add OUTPUT_DIR/04_variants.csv
git commit -m "Complete Step 5: Generate exhaustive variants (X variants)"
```


Step 6: Create Test Data (EXHAUSTIVE):

For EACH AND EVERY variant in OUTPUT_DIR/04_variants.csv, generate corresponding realistic test data.
DO NOT skip variants. One variant = one data row.
Include the Variant_ID as the first column to maintain traceability.
Save this data in OUTPUT_DIR/05_test_data.csv.

**PROGRESS TRACKING (for large datasets):**

When generating test data, provide regular progress updates:
- **Before starting**: Report total variants from 04_variants.csv (e.g., "Generating test data for 47,520 variants...")
- **During generation**: Update progress at regular intervals
  - Report every 5,000-10,000 variants (e.g., "Generated 10,000/47,520 variants [21%]")
  - Show time estimates if generation is slow (e.g., "~3 minutes remaining")
- **After completion**: Report final count (e.g., "✓ Generated test data for 47,520 variants")

VERIFICATION CHECKPOINT: After generating, verify row count matches OUTPUT_DIR/04_variants.csv and report: "Generated test data for X variants."

**DATA VALIDATION (CRITICAL):**

After generating test data, run the validation script to ensure data quality and consistency:

```bash
python3 skill/scripts/validate_test_data.py OUTPUT_DIR/04_variants.csv OUTPUT_DIR/05_test_data.csv
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**The validation script checks:**
- Row count matches between variants and test data
- All Variant_IDs are present in both files
- Parameter consistency (test data reflects variant parameters)
- Data completeness (no empty critical fields)

**Expected output:**
- ✅ "All validations passed!" - Continue to next step
- ❌ "Validation completed with errors" - Fix errors before proceeding:
  - Missing test data rows: Generate data for missing variants
  - Row count mismatch: Verify generation process completed fully
  - Empty fields: Populate missing test data values

Quality check: Ensure data is realistic, valid, and matches the variant parameters.

**GIT CHECKPOINT - Commit Step 6:**
```bash
git add OUTPUT_DIR/05_test_data.csv
git commit -m "Complete Step 6: Generate test data (X rows)"
```


Step 7: Generate Test Scripts (AUTOMATED - VARIANT-BASED):

**CRITICAL IMPROVEMENT**: Instead of manually writing test scripts (which causes LLM fatigue and quality degradation), we now use an automated script that generates test scripts programmatically from your variants and test data.

**How It Works:**
- Reads test scenarios from `03_test_scenarios.md` to understand what to test
- Reads variants from `04_variants.csv` to get parameter combinations
- Reads test data from `05_test_data.csv` to get concrete values
- **Automatically generates** one test script per variant (e.g., TS-001_V001.txt, TS-001_V002.txt, etc.)
- Uses intelligent templates based on scenario type (Registration, Login, Checkout, etc.)
- Injects specific test data and parameters into GIVEN/WHEN/THEN sections

**Benefits:**
- ✅ **100% automated** - no manual LLM script writing
- ✅ **Perfect consistency** - no quality degradation across thousands of scripts
- ✅ **Instant generation** - generates 25,000-75,000 scripts in seconds
- ✅ **Maintainable** - update templates, regenerate all scripts
- ✅ **Eliminates Critique Issue #3** - no more generic placeholders or template fatigue

**Execute the script:**

```bash
python3 skill/scripts/generate_test_scripts_from_variants.py \
  OUTPUT_DIR/03_test_scenarios.md \
  OUTPUT_DIR/04_variants.csv \
  OUTPUT_DIR/05_test_data.csv \
  -o OUTPUT_DIR/06_test_scripts
```

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**Expected Output:**
- One test script per variant: `TS-XXX_VXXX.txt`
- Generation summary: `00_GENERATION_SUMMARY.txt`
- Progress updates every 5% with ETA
- Generation speed: ~500-2,000 scripts per second
- **Example**: For 47,520 variants, expect ~30-60 seconds generation time

**File Naming Convention:**
- Format: `TS-XXX_VXXX.txt` where:
  - `TS-XXX` = Scenario ID (e.g., TS-001)
  - `VXXX` = Variant ID (e.g., V001)
- Example: `TS-001_V001.txt` = Registration scenario, variant 1 (Chrome/Desktop/Valid)
- Example: `TS-001_V002.txt` = Registration scenario, variant 2 (Chrome/Desktop/Invalid email)

**Script Content Format:**
Each generated script contains:
- **Header**: Scenario title, variant ID, priority, description
- **GIVEN**: Specific preconditions based on variant parameters (user type, browser, device, network)
- **WHEN**: Specific actions with concrete test data from CSV
- **THEN**: Specific assertions based on input validity and scenario type
- **EXPECTED RESULT**: Detailed outcomes with database/email/UI verification
- **VARIANT PARAMETERS**: All parameter values for this variant
- **TEST DATA**: All test data fields for this variant
- **RELATED REQUIREMENTS**: Traceability to requirements

VERIFICATION CHECKPOINT:

After generation completes, perform these checks:

**Quantity Check:**
- List the OUTPUT_DIR/06_test_scripts/ directory
- Count files: `ls OUTPUT_DIR/06_test_scripts/*.txt | wc -l`
- Verify count matches variant count from 04_variants.csv
- Check generation summary: `cat OUTPUT_DIR/06_test_scripts/00_GENERATION_SUMMARY.txt`
- **Report**: "Generated X test scripts for Y variants - 100% complete"

**Quality Spot-Check (10 random scripts):**

Since scripts are generated programmatically, quality is consistent. However, verify the templates work correctly:

Sample 10 random scripts and verify:
- ✓ Contains specific scenario details (not generic "scenario NN")
- ✓ GIVEN section has concrete conditions (user email, device, browser)
- ✓ WHEN section has concrete test data values from CSV
- ✓ THEN section has specific assertions
- ✓ EXPECTED RESULT has measurable outcomes
- ✓ Variant parameters and test data are populated

**Example commands to spot-check:**
```bash
# View a few random scripts
ls OUTPUT_DIR/06_test_scripts/TS-001_V*.txt | head -3 | xargs cat

# Check script contains variant-specific data
grep -l "Chrome" OUTPUT_DIR/06_test_scripts/TS-001_*.txt | head -5

# Verify no placeholder text remains
grep -r "scenario NN\|TODO\|PLACEHOLDER" OUTPUT_DIR/06_test_scripts/ || echo "✓ No placeholders found"
```

**Report:**
- "Generated X test scripts in Y seconds (Z scripts/sec)"
- "Spot-checked 10 random scripts - all contain specific variant data"
- "Quality verification complete - programmatic generation ensures consistency"

**If Issues Found:**
- If scripts are missing data: Verify test data CSV has all variant IDs
- If scripts are generic: Check that variant parameters are being read correctly
- If scenario-specific details are wrong: Update template logic in the Python script and regenerate

**GIT CHECKPOINT - Commit Step 7:**
```bash
git add OUTPUT_DIR/06_test_scripts/
git commit -m "Complete Step 7: Generate test scripts (X scripts)"
```


Step 8: Produce Combinatorial Plan (OPTIMIZATION):

**THIS IS WHERE THE MAGIC HAPPENS**: You have generated 25,000-75,000 exhaustive variants. Now reduce to ~500-2,000 optimized test cases while maintaining 95%+ pairwise coverage.

Execute the scripts/combinatorial.py script using the command:

python3 skill/scripts/combinatorial.py OUTPUT_DIR/04_variants.csv --output OUTPUT_DIR/07_combinatorial_plan.md

**IMPORTANT:** Replace OUTPUT_DIR with the actual directory path being used (e.g., `deliverables/` or custom path).

**How Combinatorial Optimization Works:**
- The script analyzes all parameter pairs in your exhaustive variants
- Selects a minimal subset that covers 95%+ of all possible parameter pair interactions
- Example: Instead of testing all 4 browsers × 3 devices × 3 network speeds (36 combos), tests ~12 carefully selected combos that cover all pairs
- This is the foundation of "pairwise testing" - research shows 70-90% of bugs are caused by single parameters or pairs

**Expected Results (for truly exhaustive input):**

| Input Variants | Expected Output | Expected Reduction | Expected Coverage |
|----------------|-----------------|-------------------|-------------------|
| 10,000-25,000  | 300-800        | 92-97%           | 95-100%          |
| 25,000-75,000  | 800-2,000      | 95-98%           | 95-100%          |
| 75,000-200,000 | 2,000-5,000    | 97-99%           | 95-100%          |

**After Execution:**

1. **Review the generated OUTPUT_DIR/07_combinatorial_plan.md** for:
   - Total exhaustive variants (input)
   - Selected optimal variants (output)
   - Pairwise coverage percentage
   - Coverage statistics table

2. **Verify Expected Performance:**
   - Reduction should be 90-95%+
   - Pairwise coverage should be 95%+
   - If reduction < 90% or coverage < 95%, something went wrong

3. **Report Results:**
   - "Combinatorial analysis reduced X variants to Y test cases (Z% reduction) with W% pairwise coverage."
   - Example: "Combinatorial analysis reduced 47,520 variants to 1,247 test cases (97.4% reduction) with 98.2% pairwise coverage."

**If Results Don't Meet Expectations:**

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Reduction < 50% | Input wasn't truly exhaustive | Go back to Step 5, regenerate with full Cartesian product |
| Coverage < 80% | Too few parameter combinations | Check that Step 5 identified all relevant parameters |
| Output > 10,000 | Input was TOO exhaustive (millions of rows) | Consider reducing some parameter dimensions or splitting into multiple runs |

**Optional flags:**
- `--mode select` - Select optimal subset from existing variants (DEFAULT - recommended)
- `--mode generate` - Generate new variants from scratch (not recommended - use Step 5 instead)
- `--verbose` - Enable detailed logging to see selection algorithm progress
- `--output <path>` - Specify custom output path (REQUIRED when using custom OUTPUT_DIR)

**What Happens Next:**
- The optimized variant list from Step 8 is used for test execution planning
- The exhaustive variant list (Step 5) remains as documentation of full coverage
- Step 9 (Test Plan) references both: exhaustive for documentation, optimized for execution

**GIT CHECKPOINT - Commit Step 8:**
```bash
git add OUTPUT_DIR/07_combinatorial_plan.md
git commit -m "Complete Step 8: Combinatorial optimization (X% reduction, Y% coverage)"
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
- Total variants created (exhaustive)
- Optimized test case count (from combinatorial analysis)
- Reduction percentage achieved
- Requirements coverage percentage
- Test scripts completion status
- Notify the user that all QA artifacts have been generated and are available in the OUTPUT_DIR directory.
- Confirm the final output directory path (e.g., "All artifacts saved to: deliverables/")
- Final verification: Confirm no gaps or missing artifacts.

**FINAL GIT CHECKPOINT - Commit all remaining files:**
```bash
# Add any remaining files not yet committed
git add OUTPUT_DIR/

# Create final summary commit
git commit -m "Complete QA artifacts generation: $(ls OUTPUT_DIR/ | wc -l) files generated"

# Optional: Tag this completion
git tag -a "qa-artifacts-$(date +%Y%m%d-%H%M%S)" -m "Completed QA artifact generation"
```

**Report final git status:**
```bash
git log --oneline -11  # Show all 11 commits (10 steps + final)
git status
```