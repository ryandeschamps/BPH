# QA Automation Scripts

This directory contains production-ready scripts for automating QA artifact generation.

## Scripts Overview

### 1. combinatorial.py

**Purpose:** Generates optimized pairwise test execution plans from variant data.

**Version:** 2.0.0

**Key Features:**
- Two modes: variant selection (default) and variant generation
- Comprehensive input validation
- Smart N/A value handling
- Detailed logging and progress tracking
- Coverage statistics reporting
- Configurable output paths

#### Usage

**Basic Usage (Select Mode - Recommended):**
```bash
python3 combinatorial.py deliverables/04_variants.csv
```

This will:
1. Read the predefined variants from `04_variants.csv`
2. Select an optimal subset for maximum pairwise coverage
3. Generate a report at `deliverables/07_combinatorial_plan.md`

**With Verbose Logging:**
```bash
python3 combinatorial.py deliverables/04_variants.csv --verbose
```

**Custom Output Path:**
```bash
python3 combinatorial.py input.csv --output custom_plan.md
```

**Generate Mode (Advanced):**
```bash
python3 combinatorial.py deliverables/04_variants.csv --mode generate
```

**Note:** Generate mode creates new variants from the parameter space and can be very slow with large parameter sets (1M+ combinations). Use select mode for typical workflows.

#### Input Format

The input CSV should have the following structure:

```csv
Variant_ID,User_Type,Browser,Device,Payment_Method,...
V001,Visitor,Chrome,Desktop,N/A,...
V002,Visitor,Firefox,Mobile,N/A,...
V003,New Buyer,Chrome,Desktop,Credit Card,...
```

**Requirements:**
- First column should be `Variant_ID` (optional but recommended)
- Subsequent columns are parameters
- Use "N/A" for parameters that don't apply
- Include 30-100 comprehensive variants

#### Output

The script generates a markdown report with:
- Coverage statistics (total pairs, coverage percentage)
- List of selected variants with all parameter values
- Variant IDs for traceability
- Recommendations for testing

**Example Output:**
```
Coverage Statistics:
- Total Parameter Pairs: 760
- Covered Pairs: 576
- Coverage Percentage: 75.79%
- Test Cases Generated: 42
```

#### Modes Explained

**Select Mode (Default):**
- Reads predefined variants from the CSV
- Uses greedy algorithm to select optimal subset
- Maintains variant IDs for traceability
- Respects N/A constraints
- Fast and practical for most use cases

**Generate Mode:**
- Extracts parameter values from CSV
- Generates new combinations algorithmically
- Does not preserve variant IDs
- Filters out N/A values
- Can be very slow with large parameter spaces
- Use only when you want to ignore predefined variants

#### Algorithm

The script uses a **greedy pairwise selection algorithm**:

1. Calculate all possible parameter pairs that need coverage
2. For each iteration:
   - Evaluate all remaining candidates
   - Select the candidate that covers the most uncovered pairs
   - Remove covered pairs from the uncovered set
3. Stop when no more pairs can be covered or candidates exhausted

This provides near-optimal coverage (typically 70-95%) with minimal test cases.

#### Performance

**Select Mode:**
- Time Complexity: O(n² × m²) where n = variants, m = parameters
- Typical execution: < 1 second for 50 variants, 12 parameters

**Generate Mode:**
- Time Complexity: O(c × m²) where c = total combinations, m = parameters
- Can generate millions of combinations
- Typical execution: Several minutes to hours depending on parameter space

#### Error Handling

The script provides comprehensive error handling:
- File not found errors
- CSV parsing errors
- Empty file validation
- Malformed row handling (padding/truncation)
- Permission errors
- Encoding errors

All errors provide clear, actionable messages.

#### Limitations

1. **Pairwise Coverage Only:** The algorithm covers 2-way parameter interactions. For 3-way or higher, consider specialized tools:
   - `allpairspy` (Python library)
   - `PICT` (Microsoft's tool)
   - `ACTS` (NIST tool)

2. **Greedy Algorithm:** Provides near-optimal but not guaranteed optimal coverage. For perfect optimization, use constraint solvers.

3. **Performance in Generate Mode:** Very slow with large parameter spaces. For production use with complex parameters, use specialized libraries.

#### Best Practices

1. **Use Select Mode:** For typical workflows, select mode is faster and more practical.

2. **Comprehensive Variants:** In Step 4, create 50-100 comprehensive variants. Step 7 will optimize.

3. **Proper N/A Usage:** Use "N/A" consistently for non-applicable parameters.

4. **Review Coverage:** Check the coverage percentage in the output. Aim for >70%.

5. **Variant IDs:** Always include a `Variant_ID` column for traceability.

6. **Verbose Mode:** Use `--verbose` for debugging or understanding selection logic.

---

### 2. rtm_builder.py

**Purpose:** Builds comprehensive Requirements Traceability Matrix (RTM) by mapping requirements to test scenarios and scripts.

**Version:** 2.0.0

**Key Features:**
- Automatic requirement metadata extraction (description, priority)
- Test script availability tracking
- Coverage statistics and gap analysis
- Comprehensive input validation
- Multiple requirement file format support
- Detailed logging and reporting
- Optional gap analysis report generation
- Orphaned scenario detection

#### Usage

**Basic Usage (Recommended):**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md requirements.md \
    --test-scripts deliverables/06_test_scripts
```

**Multiple Requirement Files:**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md \
    req1.md req2.md req3.md --test-scripts deliverables/06_test_scripts
```

**With Gap Analysis Report:**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md requirements.md \
    --test-scripts deliverables/06_test_scripts --gap-report
```

**Custom Output Path:**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md requirements.md \
    --output custom_rtm.csv
```

**With Verbose Logging:**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md requirements.md \
    --test-scripts deliverables/06_test_scripts --verbose
```

#### Input Format

**Requirements Files:**
- Any markdown or text file containing requirement IDs
- Supported patterns: `FR-001`, `NFR-001`, `REQ-001`, `BR-001`, `UR-001`
- Supports underscores: `FR_001`, `NFR_001`
- Can extract metadata from structured formats:
  - Table format: `FR-001 | Description | Priority`
  - Line format: `FR-001: Description (Priority: High)`
  - Markdown headers: `### FR-001: Description`

**Test Scenarios File:**
- Markdown file with test scenarios (e.g., `03_test_scenarios.md`)
- Scenario IDs should match pattern: `TS-001`, `TS_001`, etc.
- Should include metadata sections:
  - `**Related Requirements**: FR-001, FR-002`
  - `**Priority**: Critical/High/Medium/Low`
  - Title after `###` header

**Test Scripts Directory (Optional):**
- Directory containing test script files
- Scripts should be named: `TS-001.txt`, `TS-002.txt`, etc.
- Used to check test script availability

#### Output

**Primary Output (CSV):**
The script generates a rich RTM CSV file at `deliverables/09_rtm.csv`:

```csv
Requirement_ID,Requirement_Description,Priority,Test_Scenario_IDs,Test_Script_Available,Coverage_Status,Notes
FR-001,Login,Critical,"TS-013, TS-014, TS-015",Yes,Covered,
FR-002,Registration,Critical,"TS-011, TS-012",Yes,Covered,
FR-999,Unused Feature,Low,N/A,N/A,Not Covered,No test scenarios mapped to this requirement
```

**Columns:**
- **Requirement_ID**: Unique requirement identifier
- **Requirement_Description**: Extracted description (if available)
- **Priority**: Extracted priority (if available)
- **Test_Scenario_IDs**: Comma-separated list of mapped scenarios
- **Test_Script_Available**: Yes/No/Partial/N/A
- **Coverage_Status**: Covered/Not Covered
- **Notes**: Additional information (e.g., missing scripts, coverage gaps)

**Gap Analysis Report (Optional):**
When `--gap-report` flag is used, generates `<output>_gap_report.md`:

```markdown
# RTM Gap Analysis Report

## Summary
- Total Requirements: 26
- Coverage: 100.0%
- Uncovered Requirements: 0
- Orphaned Scenarios: 0

## ⚠️ Uncovered Requirements
(Lists requirements with no test scenarios)

## ⚠️ Orphaned Test Scenarios
(Lists scenarios not linked to any requirement)

## ℹ️ Scenarios Without Test Scripts
(Lists scenarios missing script files)
```

**Console Summary:**
The script also prints a summary to console:

```
============================================================
RTM GENERATION SUMMARY
============================================================

📋 Requirements:
  Total Requirements: 26
  Covered: 26 (100.0%)
  Uncovered: 0

🧪 Test Scenarios:
  Total Scenarios: 125
  Orphaned (no requirements): 0
  With Test Scripts: 125
  Without Test Scripts: 0

✅ Perfect traceability! All requirements covered and all scenarios linked.
============================================================
```

#### Algorithm

**Requirement Extraction:**
1. Read all requirement files
2. Find requirement IDs using regex patterns
3. Attempt to extract metadata (description, priority) from context
4. Store requirement objects with metadata

**Scenario Extraction:**
1. Read test scenarios file
2. Split by scenario IDs
3. Extract scenario metadata (title, priority, related requirements)
4. Check if test script file exists (if test scripts directory provided)
5. Store scenario objects with metadata

**RTM Building:**
1. For each scenario, map to its related requirements
2. Build bidirectional mapping (requirements ↔ scenarios)
3. Flag requirements mentioned in scenarios but not in requirement files
4. Calculate coverage statistics

**Gap Detection:**
- **Uncovered Requirements**: Requirements with no mapped scenarios
- **Orphaned Scenarios**: Scenarios not linked to any requirement
- **Missing Scripts**: Scenarios without corresponding script files

#### Metadata Extraction

The script intelligently extracts requirement metadata from various formats:

**Table Format:**
```
| ID | Description | Priority |
|----|-------------|----------|
| FR-001 | User Login | Critical (1) |
```

**Colon Format:**
```
FR-001: User must be able to login (Priority: Critical)
```

**Markdown Header:**
```markdown
### FR-001: User Login Feature
```

If metadata cannot be extracted, it defaults to "N/A".

#### Coverage Statistics

The script calculates and reports:
- Total requirements and coverage percentage
- Number of uncovered requirements
- Total scenarios and orphaned scenarios
- Test script availability statistics

#### Performance

- **Time Complexity**: O(R + S) where R = requirements, S = scenarios
- **Typical Execution**: < 1 second for 26 requirements, 125 scenarios

#### Error Handling

The script provides comprehensive error handling:
- File not found errors
- File permission errors
- File encoding errors (uses UTF-8 with error ignore)
- Empty file detection
- Invalid path detection
- Missing metadata graceful degradation

All errors provide clear, actionable messages.

#### Best Practices

1. **Include Test Scripts Directory**: Always use `--test-scripts` flag for complete tracking
2. **Use Gap Report**: Run with `--gap-report` to get detailed gap analysis
3. **Multiple Requirement Files**: Pass all requirement documents for complete traceability
4. **Structured Requirements**: Use structured formats (tables, headers) for better metadata extraction
5. **Link Scenarios**: Always include `**Related Requirements**` in scenario descriptions
6. **Review Summary**: Check the console summary for coverage gaps

#### Supported Requirement ID Patterns

- Functional Requirements: `FR-001`, `FR_001`
- Non-Functional Requirements: `NFR-001`, `NFR_001`
- Generic Requirements: `REQ-001`, `REQ_001`
- Business Requirements: `BR-001`, `BR_001`
- User Requirements: `UR-001`, `UR_001`
- Case insensitive
- Automatically normalized (underscores → dashes, uppercase)

---

## Integration with Skill Workflow

The scripts integrate with the QA skill workflow as follows:

```
Step 3: Test Scenarios → 03_test_scenarios.md
Step 4: Define Variants → 04_variants.csv (50 variants)
Step 6: Test Scripts → 06_test_scripts/ directory
          ↓                     ↓                    ↓
          |                     |                    |
Step 7:   |          Run combinatorial.py           |
          |        → 07_combinatorial_plan.md       |
          |          (optimal subset)                |
          |                                          |
Step 9:   └─────────────────┬────────────────────────┘
                            ↓
                   Run rtm_builder.py
                  → 09_rtm.csv + gap report
                   (requirements traceability)
```

**Script Execution Order:**
1. **Step 7**: `combinatorial.py` - Optimizes test variants
2. **Step 9**: `rtm_builder.py` - Builds requirements traceability

## Requirements

- Python 3.7+
- Standard library only (no external dependencies)

## Troubleshooting

### "File not found" error
- Ensure the input file path is correct
- Use absolute paths or run from the repository root

### "CSV parsing error"
- Check CSV is valid UTF-8
- Ensure all rows have the same number of columns
- Check for unescaped commas in values

### "No valid parameters extracted"
- Ensure CSV has at least one column with non-N/A values
- Check that variant data is present (not just headers)

### Generate mode is very slow
- This is expected with large parameter spaces
- Consider using select mode instead
- For large-scale generation, use `allpairspy` or `PICT`

### Low coverage percentage (<60%)
- Add more diverse variants in Step 4
- Ensure variants cover different parameter combinations
- Check that N/A values aren't preventing pair coverage

## Version History

### v2.0.0 (2025-11-14) - rtm_builder.py
- Complete rewrite for production readiness
- Rich RTM output with 7 columns (vs 2 in v1.0)
- Automatic requirement metadata extraction (description, priority)
- Test script availability tracking
- Coverage statistics and gap analysis
- Gap analysis report generation
- Orphaned scenario detection
- Multiple requirement file format support
- Comprehensive input validation
- Configurable CLI with argparse
- Detailed logging and progress tracking
- Better error handling and graceful degradation

### v2.0.0 (2025-11-14) - combinatorial.py
- Complete rewrite for production readiness
- Added select mode for optimal variant selection
- Comprehensive input validation
- Smart N/A value handling
- Detailed logging and progress tracking
- Configurable CLI with argparse
- Performance improvements (O(n) to O(1) removal)
- Better error handling and recovery
- Coverage statistics reporting

### v1.0.0 - Initial release
- Basic pairwise generation
- Simple CSV parsing
- Markdown output
- Basic RTM generation

## Contributing

When modifying scripts:
1. Maintain backward compatibility with existing workflows
2. Add comprehensive error handling
3. Update documentation
4. Test with sample data
5. Update version numbers

## Support

For issues or questions:
1. Check this README
2. Run script with `--help` flag
3. Use `--verbose` flag for detailed logging
4. Review error messages carefully

---

**Last Updated:** 2025-11-14
**Maintainer:** QA Automation Skill
