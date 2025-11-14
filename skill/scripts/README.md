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

**Purpose:** Builds Requirements Traceability Matrix (RTM) by mapping requirements to test scenarios.

**Version:** 1.0.0

#### Usage

```bash
python3 rtm_builder.py <scenarios_file> <req_file_1> [<req_file_2> ...]
```

**Example:**
```bash
python3 rtm_builder.py deliverables/03_test_scenarios.md requirements/BRD.md
```

#### Input Format

**Requirements Files:**
- Any markdown or text file containing requirement IDs
- Requirement IDs should match pattern: `REQ-001`, `REQ_001`, or `REQ001`

**Scenarios File:**
- Markdown file with test scenarios
- Scenario IDs should match pattern: `TS-001`, `TS_001`, or `TS001`
- Requirements should be referenced in scenario descriptions

#### Output

Generates a CSV file at `deliverables/09_rtm.csv`:

```csv
Requirement_ID,Test_Scenario_ID(s)
REQ-001,"TS-001, TS-002, TS-003"
REQ-002,"TS-004"
REQ-003,"NOT COVERED"
```

#### Algorithm

1. Extract all requirement IDs from requirement files
2. For each test scenario, find mentioned requirement IDs
3. Map requirements to scenarios
4. Flag requirements with no coverage as "NOT COVERED"

---

## Integration with Skill Workflow

The scripts integrate with the QA skill workflow as follows:

```
Step 4: Define Variants → 04_variants.csv (50 variants)
                          ↓
Step 7: Run combinatorial.py → 07_combinatorial_plan.md (optimal subset)
                          ↓
                  Use selected variants for testing
```

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
