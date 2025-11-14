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


Step 2: Extract and Number Requirements:

From the source requirement documents, extract and clearly articulate all functional and non-functional requirements.
Assign a unique ID to each requirement in the format: REQ-001, REQ-002, etc.
Group requirements by functional area (e.g., User Management, Data Processing, Security, Performance).

**REQUIRED FORMAT (for rtm_builder.py script consumption):**
```markdown
## [Functional Area Name]
- **REQ-001**: [Clear, concise requirement statement]
- **REQ-002**: [Clear, concise requirement statement]
```
OR
```markdown
| Requirement ID | Description | Priority |
|---------------|-------------|----------|
| REQ-001 | [Requirement statement] | High |
| REQ-002 | [Requirement statement] | Medium |
```

Include both explicit requirements (stated in the document) and implicit requirements (derived from context).
Save to OUTPUT_DIR/00_requirements.md (numbered 00 to appear first in directory listing).
Count and report: State the total number of requirements extracted (e.g., "Extracted 47 requirements").
This document will be used by Step 10 for Requirements Traceability Matrix generation.


Step 3: Extract Entities and Flows:

From the requirements, identify and list all key entities (e.g., user roles, system components, data objects) and the primary user/system flows.
Document these in OUTPUT_DIR/02_entities_and_flows.md.
Count and report: State the number of entities and flows identified.


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


Step 6: Create Test Data (EXHAUSTIVE):

For EACH AND EVERY variant in OUTPUT_DIR/04_variants.csv, generate corresponding realistic test data.
DO NOT skip variants. One variant = one data row.
Include the Variant_ID as the first column to maintain traceability.
Save this data in OUTPUT_DIR/05_test_data.csv.
VERIFICATION CHECKPOINT: After generating, verify row count matches OUTPUT_DIR/04_variants.csv and report: "Generated test data for X variants."
Quality check: Ensure data is realistic, valid, and matches the variant parameters.


Step 7: Generate Test Scripts (EXHAUSTIVE - BATCH APPROACH):

CRITICAL: You must generate a test script for EVERY SINGLE SCENARIO from OUTPUT_DIR/03_test_scenarios.md.
DO NOT skip any scenarios. Missing scripts break traceability.

**REQUIRED FORMAT (for rtm_builder.py script consumption):**
- File naming: MUST use format `TS-XXX.txt` where XXX matches scenario ID
- Content format: Use "Given / When / Then" format with clear "Expected Result"
- Save location: OUTPUT_DIR/06_test_scripts/

BATCH PROCESSING STRATEGY (for large scenario counts):

First: Count total scenarios to generate (e.g., "Need to generate 85 test scripts")
Batch 1 (scripts 1-20): Generate TS-001 through TS-020, save all files
Batch 2 (scripts 21-40): Generate TS-021 through TS-040, save all files
Batch 3 (scripts 41-60): Generate TS-041 through TS-060, save all files
Continue until ALL scenarios have scripts
After each batch: Report progress (e.g., "Completed 40/85 test scripts")

VERIFICATION CHECKPOINT:

After completion, perform BOTH quantity and quality checks:

**Quantity Check:**
- List the OUTPUT_DIR/06_test_scripts/ directory
- Count files and verify: "Generated X test scripts for X scenarios - 100% complete"
- If any are missing: Generate the missing scripts immediately before proceeding

**Quality Check (CRITICAL - prevents generic templates):**

**Sampling Strategy:**
- Sample at least 15-20 scripts (minimum 10% of total, distributed across all batches)
- Must include scripts from: Beginning (TS-001 to TS-020), Middle (around TS-050% mark), End (last 20 scripts)
- Example for 100 scripts: Sample TS-005, TS-012, TS-025, TS-038, TS-047, TS-053, TS-066, TS-071, TS-084, TS-091, TS-095, TS-099
- This ensures quality doesn't degrade in later batches

**For EACH sampled script, verify:**

✓ **NO generic placeholders**:
  - BAD: "scenario NN", "scenario 50", "appropriate page", "user/admin", "required action", "expected result"
  - GOOD: Specific page names ("Product Search page", "Checkout page"), specific roles ("Buyer", "Admin")

✓ **Specific GIVEN conditions**:
  - BAD: "system is in ready state", "preconditions are met"
  - GOOD: "Buyer is logged in with account john.doe@example.com", "Shopping cart contains 3 items totaling $127.99"

✓ **Specific WHEN actions**:
  - BAD: "performs required action", "executes the operation", "completes the task"
  - GOOD: "Clicks 'Add to Cart' button", "Enters credit card number 4111-1111-1111-1111", "Selects 'Express Shipping'"

✓ **Specific THEN outcomes**:
  - BAD: "displays expected result", "system updates correctly", "appropriate message shown"
  - GOOD: "Displays success message 'Item added to cart'", "Redirects to /cart page", "Cart badge shows quantity '4'"

✓ **Concrete test data values**:
  - BAD: "[User email]", "valid credentials", "sample data"
  - GOOD: "john.doe@example.com", "Password: SecurePass123!", "Product ID: PROD-12345"

✓ **Measurable expected results**:
  - BAD: "confirmation message displayed", "system behaves correctly"
  - GOOD: "Email sent to john.doe@example.com with subject 'Order Confirmation #ORD-456'", "Database shows order status = 'PENDING'"

**Quality Assessment:**
- Create a checklist for each sampled script with the 6 criteria above
- Mark each as PASS or FAIL
- Calculate pass rate: X/Y scripts passed quality check

**If quality check fails (pass rate < 90%):**
1. Identify all FAILED scripts and note their batch numbers
2. List specific quality issues found (e.g., "TS-050 uses 'scenario 50' placeholder", "TS-078 has vague expected result")
3. Regenerate ENTIRE affected batches with explicit instruction:
   - "Generate test scripts with SPECIFIC details. Use concrete values, not placeholders. Reference actual field names, button labels, error messages, and page URLs."
4. After regeneration, re-sample the regenerated batches (sample 20% of regenerated scripts)
5. Verify quality improved to >90% pass rate
6. If still failing, regenerate individual scripts one by one with detailed prompting

**Report:**
- "Quality check: X/Y sampled scripts passed (Z% pass rate)"
- If <90%: "Regenerated batches [list], re-verified, final pass rate: W%"
- If ≥90%: "Quality verification complete - all scripts meet standards"


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

9. Step 9: Draft Full Test Plan:
- Synthesize all previous outputs into a comprehensive test plan document.
- The plan should include:
- Executive summary with key statistics
- Scope and objectives
- Test approach (exhaustive generation + combinatorial optimization)
- Schedule and resource estimates
- Summary of all test scenarios and variants (both exhaustive and optimized)
- Traceability matrix summary
- Risk assessment
- Save the document as OUTPUT_DIR/08_test_plan.md.

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
Requirement_ID,Requirement_Description,Priority,Test_Scenario_IDs,Test_Script_Available,Coverage_Status,Notes
REQ-001,Users shall be able to log in...,N/A,"TS-007, TS-009, TS-017",Yes,Covered,
REQ-002,Password reset functionality...,High,"TS-013, TS-014",Yes,Covered,
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