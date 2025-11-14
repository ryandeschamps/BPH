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

Once they are provided, handle the output directory:
- **If deliverables/ directory does NOT exist**: Create deliverables/ and deliverables/06_test_scripts/
- **If deliverables/ directory EXISTS**:
  - Ask user: "Output directory 'deliverables/' already exists. Options: (1) Overwrite, (2) Use timestamped directory (e.g., deliverables_20251114_225805/), (3) Cancel"
  - Based on user choice:
    - Overwrite: Remove existing deliverables/ and create fresh directories
    - Timestamped: Create deliverables_YYYYMMDD_HHMMSS/ and update all subsequent paths
    - Cancel: Stop and wait for user to manually handle the directory

Set expectations: Tell the user this process generates exhaustive content first, then optimizes.


Step 1: Assess Requirements:

Carefully read all the provided requirement documents.
Analyze them for gaps, ambiguities, contradictions, and unstated assumptions.
Synthesize your findings into a markdown file named deliverables/01_requirements_assessment.md.


Step 2: Extract and Number Requirements:

From the source requirement documents, extract and clearly articulate all functional and non-functional requirements.
Assign a unique ID to each requirement in the format: REQ-001, REQ-002, etc.
Group requirements by functional area (e.g., User Management, Data Processing, Security, Performance).
Use the format: - **REQ-XXX**: [Clear, concise requirement statement]
Include both explicit requirements (stated in the document) and implicit requirements (derived from context).
Save to deliverables/00_requirements.md (numbered 00 to appear first in directory listing).
Count and report: State the total number of requirements extracted (e.g., "Extracted 47 requirements").
This document will be used by Step 10 for Requirements Traceability Matrix generation.


Step 3: Extract Entities and Flows:

From the requirements, identify and list all key entities (e.g., user roles, system components, data objects) and the primary user/system flows.
Document these in deliverables/02_entities_and_flows.md.
Count and report: State the number of entities and flows identified.


Step 4: Derive Test Scenarios (EXHAUSTIVE):

Based on the entities and flows, generate an EXHAUSTIVE set of test scenarios.
DO NOT skip scenarios. Cover every requirement, every entity, every flow, every edge case.
Each scenario must follow the user story format: "As a [user role], I want to [perform an action], so that I can [achieve a benefit]."
Assign a unique ID (e.g., TS-001, TS-002) to each scenario.
IMPORTANT: Add a "Related Requirements:" line after each scenario listing the requirement IDs it covers (e.g., Related Requirements: REQ-001, REQ-005, REQ-012)
Save these to deliverables/03_test_scenarios.md.
VERIFICATION CHECKPOINT: After generating, count the total scenarios and report: "Generated X test scenarios covering Y requirements."
Cross-check: Review deliverables/00_requirements.md to ensure every requirement has at least one scenario. If any are missing, add them now.


Step 5: Define Variants (EXHAUSTIVE):

For EACH AND EVERY scenario from Step 4, identify all parameters that can vary.
Parameters include: user types, input values, data states, system configurations, edge cases, boundary conditions.
Create the COMPLETE EXHAUSTIVE CARTESIAN PRODUCT of these parameters.
DO NOT limit variants. The goal is to capture EVERY possible combination. Optimization happens in Step 8.
Include a Scenario_ID column as the first column that corresponds to the Test Scenario identified in Step 4.
Include a Variant_ID column (e.g., V001, V002, etc.) as the second column.
Use "N/A" for parameters that don't apply to certain user types (e.g., payment method for visitors).
Expected scale: For a moderate application, expect 200-1000+ variants.
Output this as a CSV file to deliverables/04_variants.csv.
VERIFICATION CHECKPOINT: After generating, count total variants and report: "Generated X variants across Y scenarios (average Z variants per scenario)."
Spot check: Verify that common scenarios have multiple variants (e.g., TS-001 should have variants for all user types × all input conditions).
Note: Step 8 will use combinatorial analysis to reduce this to an optimal subset (~95% reduction).


Step 6: Create Test Data (EXHAUSTIVE):

For EACH AND EVERY variant in 04_variants.csv, generate corresponding realistic test data.
DO NOT skip variants. One variant = one data row.
Include the Variant_ID as the first column to maintain traceability.
Save this data in deliverables/05_test_data.csv.
VERIFICATION CHECKPOINT: After generating, verify row count matches 04_variants.csv and report: "Generated test data for X variants."
Quality check: Ensure data is realistic, valid, and matches the variant parameters.


Step 7: Generate Test Scripts (EXHAUSTIVE - BATCH APPROACH):

CRITICAL: You must generate a test script for EVERY SINGLE SCENARIO from 03_test_scenarios.md.
DO NOT skip any scenarios. Missing scripts break traceability.
Each script uses the "Given / When / Then" format with clear "Expected Result".
Save each script as a separate file: deliverables/06_test_scripts/TS-XXX.txt

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
- List the deliverables/06_test_scripts/ directory
- Count files and verify: "Generated X test scripts for X scenarios - 100% complete"
- If any are missing: Generate the missing scripts immediately before proceeding

**Quality Check (CRITICAL - prevents generic templates):**
- Randomly sample 10-15 scripts (at least 5% of total)
- For each sampled script, verify it has:
  ✓ NO generic placeholders like "scenario NN", "appropriate page", "user/admin", "required action"
  ✓ Specific GIVEN conditions (not "system is in ready state")
  ✓ Specific WHEN actions (not "performs required action")
  ✓ Specific THEN outcomes (not "displays expected result")
  ✓ Concrete test data values (actual names, emails, numbers)
  ✓ Measurable expected results (specific messages, states, redirects)
- If ANY sampled script fails quality check:
  - Identify the affected batch (scripts were generated in batches)
  - Regenerate that entire batch with explicit instruction: "Be specific, no placeholders, use concrete values"
  - Re-sample to verify quality
- Report: "Quality check passed for X/X sampled scripts"


Step 8: Produce Combinatorial Plan (OPTIMIZATION):

NOW is when optimization happens - you have exhaustive content, now reduce it intelligently.
Execute the scripts/combinatorial.py script using the command:

python3 skill/scripts/combinatorial.py deliverables/04_variants.csv

- The script will automatically select an optimal subset of variants from `04_variants.csv` that achieves maximum pairwise coverage.
- This reduces the number of test executions while maintaining comprehensive parameter interaction coverage.
- The output is automatically saved to `deliverables/07_combinatorial_plan.md`.
- Review the generated plan for coverage statistics and selected variants.
- **Report:** "Combinatorial analysis reduced X variants to Y test cases (Z% reduction) with W% pairwise coverage."
- **Optional flags:**
  - `--mode generate` - Generate new variants instead of selecting from existing ones (not recommended for typical use)
  - `--verbose` - Enable detailed logging
  - `--output <path>` - Specify custom output path

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
- Save the document as deliverables/08_test_plan.md.

10. Step 10: Build Requirements Traceability Matrix (RTM):

Execute the scripts/rtm_builder.py script using the command:

python3 skill/scripts/rtm_builder.py deliverables/03_test_scenarios.md deliverables/00_requirements.md --test-scripts deliverables/06_test_scripts --gap-report

- The script will generate a comprehensive RTM with:
  - Requirement-to-scenario mappings
  - Coverage status and statistics
  - Test script availability tracking
  - Gap analysis (uncovered requirements, orphaned scenarios)
- The output is automatically saved to `deliverables/09_rtm.csv`.
- Review the summary statistics and address any coverage gaps.
- **Report:** "RTM shows X% requirement coverage with Y uncovered requirements and Z orphaned scenarios."
- **Optional flags:**
  - `--gap-report` - Generate detailed gap analysis report (recommended)
  - `--output <path>` - Specify custom output path
  - `--verbose` - Enable detailed logging

11. Completion and Summary:
- List all files in deliverables/ directory with file sizes
- Provide a comprehensive summary with key metrics:
- Total requirements extracted
- Total test scenarios generated
- Total variants created (exhaustive)
- Optimized test case count (from combinatorial analysis)
- Reduction percentage achieved
- Requirements coverage percentage
- Test scripts completion status
- Notify the user that all QA artifacts have been generated and are available in the deliverables/ directory.
- Final verification: Confirm no gaps or missing artifacts.