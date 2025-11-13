---
name: generate-qa-artifacts-from-requirements
description: >
  Generate QA deliverables (scenarios, variants, data, scripts, plan, RTM) from
  requirement/specification documents. Use when you have requirements, specs,
  user stories or acceptance criteria and need to automate QA artifact generation.
---

# Generate QA Artifacts from Requirements

This skill automates the creation of a full suite of Quality Assurance artifacts based on provided requirements documents.

## Instructions

Follow this workflow precisely. Create a `deliverables/` directory to store all outputs.

1.  **Acknowledge and Prepare:** Confirm you have understood the request. Ask the user to upload all their requirements and specification documents. Once they are provided, create the `deliverables/` and `deliverables/06_test_scripts/` directories.

2.  **Step 1: Assess Requirements:**
    - Carefully read all the provided requirement documents.
    - Analyze them for gaps, ambiguities, contradictions, and unstated assumptions.
    - Synthesize your findings into a markdown file named `deliverables/01_requirements_assessment.md`.

3.  **Step 2: Extract Entities and Flows:**
    - From the requirements, identify and list all key entities (e.g., user roles, system components, data objects) and the primary user/system flows.
    - Document these in `deliverables/02_entities_and_flows.md`.

4.  **Step 3: Derive Test Scenarios:**
    - Based on the entities and flows, generate a comprehensive set of test scenarios.
    - Each scenario must follow the user story format: **"As a [user role], I want to [perform an action], so that I can [achieve a benefit]."**
    - Assign a unique ID (e.g., TS-001, TS-002) to each scenario.
    - Save these to `deliverables/03_test_scenarios.md`.

5.  **Step 4: Define Variants:**
    - Identify parameters within the scenarios that can vary (e.g., user types, input values, configurations).
    - Create logical combinations of these parameters to define distinct test variants.
    - Output this as a CSV file to `deliverables/04_variants.csv`. The headers should be the parameters.

6.  **Step 5: Create Test Data:**
    - For each variant defined in `04_variants.csv`, generate corresponding, realistic test data.
    - Save this data in `deliverables/05_test_data.csv`. Ensure the data aligns with the variants.

7.  **Step 6: Generate Test Scripts:**
    - For each scenario in `03_test_scenarios.md`, write a detailed test script using the "Given / When / Then" format.
    - Include a clear **"Expected Result"** for each script.
    - Save each script as a separate file inside the `deliverables/06_test_scripts/` directory (e.g., `TS-001.txt`).

8.  **Step 7: Produce Combinatorial Plan:**
    - **Execute the `scripts/combinatorial.py` script.** Pass the `deliverables/04_variants.csv` file as an argument.
    - This script will generate an optimized, pairwise test execution plan.
    - Save the script's output to `deliverables/07_combinatorial_plan.md`.

9.  **Step 8: Draft Full Test Plan:**
    - Synthesize all previous outputs into a comprehensive test plan document.
    - The plan should include scope, objectives, schedule, and a summary of all test scenarios and variants.
    - Save the document as `deliverables/08_test_plan.md`.

10. **Step 9: Build Requirements Traceability Matrix (RTM):**
    - **Execute the `scripts/rtm_builder.py` script.** Pass the paths to the requirements file(s) and `deliverables/03_test_scenarios.md` as arguments.
    - The script will generate a CSV mapping requirements to test scenarios.
    - Save the resulting RTM to `deliverables/09_rtm.csv`.

11. **Completion:** Notify the user that all QA artifacts have been generated and are available in the `deliverables/` directory.