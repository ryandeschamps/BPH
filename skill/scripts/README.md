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

### 3. chunk_large_pdf.py

**Purpose:** Intelligently chunks large PDF files that exceed LLM context limits into manageable pieces with preserved traceability.

**Version:** 1.0.0

**Key Features:**
- Automatic size detection (file size, page count, character count)
- Multiple chunking strategies (pages, size, sections)
- Text extraction with multiple PDF library support
- Page number preservation for traceability
- Context overlap between chunks
- Summary file generation with usage instructions
- Progress tracking and verbose logging
- Graceful error handling

#### Usage

**Basic Usage (Auto-detect):**
```bash
python3 chunk_large_pdf.py requirements.pdf
```

This will:
1. Analyze the PDF file
2. Determine if chunking is needed based on thresholds
3. If needed, extract text and create chunks automatically
4. Generate summary file with processing details

**Check Without Processing:**
```bash
# Script will report if chunking is needed without creating chunks
python3 chunk_large_pdf.py requirements.pdf
```

**Force Chunking:**
```bash
python3 chunk_large_pdf.py requirements.pdf --force
```

**With Specific Strategy:**
```bash
# Chunk by pages (10 pages per chunk)
python3 chunk_large_pdf.py requirements.pdf --strategy pages --pages-per-chunk 10

# Chunk by character count
python3 chunk_large_pdf.py requirements.pdf --strategy size --chunk-size 50000

# Chunk by detected sections/headings (best quality)
python3 chunk_large_pdf.py requirements.pdf --strategy sections
```

**Custom Output Directory:**
```bash
python3 chunk_large_pdf.py requirements.pdf --output my_chunks/
```

**Verbose Logging:**
```bash
python3 chunk_large_pdf.py requirements.pdf --verbose
```

#### Detection Thresholds

The script automatically determines if chunking is needed based on:

| Threshold | Value | Reason |
|-----------|-------|--------|
| File Size | > 5 MB | Large files may cause processing issues |
| Page Count | > 50 pages | Too many pages for single LLM context |
| Character Count | > 100,000 chars | Exceeds typical LLM token limits (~25k tokens) |

**Note:** Use `--force` flag to chunk files that are below thresholds.

#### Chunking Strategies

**1. Auto Strategy (Default - Recommended):**
- Automatically selects best strategy based on file characteristics:
  - Large page count (>100 pages) → Uses "pages" strategy
  - Large text content (>200k chars) → Uses "sections" strategy
  - Otherwise → Uses "size" strategy

**2. Pages Strategy:**
- Chunks by page count
- Good for: Very large PDFs, consistent page-based processing
- Default: 10 pages per chunk (configurable with `--pages-per-chunk`)
- Pros: Simple, predictable chunk sizes
- Cons: May split mid-section

**3. Size Strategy:**
- Chunks by character count
- Good for: Consistent chunk sizing, balanced processing
- Default: 50,000 characters per chunk (configurable with `--chunk-size`)
- Features: Includes context overlap between chunks (500 chars)
- Pros: Consistent sizing, maintains some context between chunks
- Cons: May split mid-paragraph

**4. Sections Strategy (Best Quality):**
- Chunks by detected headings/sections
- Good for: Structured documents, preserving logical flow
- Detection: Finds markdown headings, numbered sections, ALL CAPS headings
- Fallback: If no sections detected, falls back to size-based chunking
- Pros: Preserves document structure, cleanest breaks
- Cons: Variable chunk sizes, depends on document structure

#### Output Format

**Directory Structure:**
```
<pdf_name>_chunks/
├── 00_CHUNKING_SUMMARY.txt          # Overview and usage instructions
├── chunk_001_pages_1-10.txt         # First chunk (pages 1-10)
├── chunk_002_pages_11-20.txt        # Second chunk (pages 11-20)
├── chunk_003_pages_21-30.txt        # Third chunk (pages 21-30)
└── ...
```

**Chunk File Format:**
Each chunk file contains:

```
================================================================================
CHUNK 1 of 5
================================================================================
Source PDF: requirements.pdf
Pages: 1-10 (10 pages)
Characters: 45,823
Chunking Strategy: pages
================================================================================

[Page 1]
<page 1 text content>

[Page 2]
<page 2 text content>

...
```

**Summary File Format:**
`00_CHUNKING_SUMMARY.txt` contains:
- Source file information (size, pages, characters)
- Chunking details (reason, strategy, number of chunks)
- Individual chunk details (page ranges, character counts)
- Usage instructions for processing chunks

#### PDF Library Support

The script supports multiple PDF libraries (tries in order):
1. **PyPDF2** - Fast, widely used
2. **pdfplumber** - Better text extraction quality
3. **pypdf** - Modern alternative to PyPDF2

**Installation:**
```bash
# Install any one of these (or all for fallback):
pip install PyPDF2        # Recommended
pip install pdfplumber    # Best quality
pip install pypdf         # Modern alternative
```

**No Library Error:**
If no PDF library is installed, the script will provide clear installation instructions.

#### Integration with Skill Workflow

**In Step 1 (Acknowledge and Prepare):**

When user provides PDF files:

1. **Run chunking check:**
   ```bash
   python3 skill/scripts/chunk_large_pdf.py requirements.pdf
   ```

2. **If chunking not needed:**
   - Script outputs: "✓ No chunking needed: File is within acceptable limits"
   - Process PDF normally with LLM

3. **If chunking needed:**
   - Script creates chunks in `requirements_chunks/` directory
   - Read `00_CHUNKING_SUMMARY.txt` for overview

4. **Process chunks in Step 2 (Extract Requirements):**
   - Read `chunk_001_pages_1-10.txt`
   - Extract requirements with page references
   - Read `chunk_002_pages_11-20.txt`
   - Continue extracting from each chunk
   - Combine all requirements into single `00_requirements.md`

**Benefits:**
- ✅ Handles PDFs of any size
- ✅ Preserves page numbers for traceability
- ✅ Maintains document structure
- ✅ Prevents LLM context overflow errors
- ✅ Automatic detection - no manual intervention unless needed

#### Performance

**Text Extraction:**
- Speed: ~1-5 seconds per page (varies by PDF complexity)
- Memory: Loads one page at a time (low memory footprint)

**Chunking:**
- Strategy selection: < 1 second
- Chunk creation: < 1 second per chunk
- File writing: < 1 second total

**Typical Times:**
- Small PDF (20 pages): 5-10 seconds
- Medium PDF (100 pages): 30-60 seconds
- Large PDF (500 pages): 2-5 minutes

#### Error Handling

The script provides comprehensive error handling:

| Error Type | Handling |
|------------|----------|
| File not found | Clear error message with file path |
| No PDF library | Installation instructions for all supported libraries |
| Corrupted PDF | Graceful failure with error details |
| Permission errors | Clear error message |
| Encoding errors | UTF-8 with error ignore fallback |
| Empty PDF | Detection and warning |

#### Best Practices

1. **Use Auto Strategy:** Let the script choose the best chunking method
2. **Install pdfplumber:** Provides best text extraction quality
   ```bash
   pip install pdfplumber
   ```
3. **Check Summary First:** Always review `00_CHUNKING_SUMMARY.txt` before processing
4. **Process Sequentially:** Process chunks in order (001, 002, 003...) to maintain document flow
5. **Preserve Page References:** When extracting requirements, note page numbers from chunk headers
6. **Combine Results:** Merge findings from all chunks into single deliverable

#### Limitations

1. **Text Extraction Quality:** Depends on PDF quality
   - Scanned PDFs (images): May need OCR pre-processing
   - Complex formatting: May lose some layout information
   - Tables/diagrams: May not extract perfectly

2. **Section Detection:** Requires structured headings
   - Works best with: Markdown headers, numbered sections, ALL CAPS headings
   - May not detect: Inconsistent formatting, custom heading styles

3. **Context Preservation:** Limited overlap between chunks
   - Size strategy: 500 character overlap
   - Pages/sections: No overlap (clean breaks)

#### Troubleshooting

**"No PDF library installed" error:**
```bash
pip install PyPDF2  # or pdfplumber or pypdf
```

**Poor text extraction quality:**
- Try pdfplumber: `pip install pdfplumber`
- Check if PDF is scanned (requires OCR)
- Verify PDF is not corrupted

**Sections strategy not finding sections:**
- Check document has clear headings
- Try size or pages strategy instead
- Use `--verbose` to see what's detected

**Chunk files too large/small:**
- Adjust with `--chunk-size` or `--pages-per-chunk`
- Try different strategy

**Memory issues:**
- Script processes one page at a time (low memory)
- For very large PDFs (1000+ pages), use pages strategy

#### Examples

**Example 1: Check if chunking needed**
```bash
$ python3 chunk_large_pdf.py requirements.pdf

================================================================================
PDF Chunking Tool - Processing: requirements.pdf
================================================================================

✓ No chunking needed: File is within acceptable limits
  File size: 2.34 MB
  Pages: 25

You can process this PDF directly with the LLM.
```

**Example 2: Automatic chunking**
```bash
$ python3 chunk_large_pdf.py large_spec.pdf

================================================================================
PDF Chunking Tool - Processing: large_spec.pdf
================================================================================

⚠ Chunking needed: Page count (127) exceeds 50 pages
Extracting text using pdfplumber...
Extracted 127 pages, 234,567 characters

Auto-selected strategy: pages (large page count)

Applying 'pages' chunking strategy...

Saving 13 chunks to large_spec_chunks/
  ✓ Saved chunk_001_pages_1-10.txt (18,234 chars)
  ✓ Saved chunk_002_pages_11-20.txt (19,123 chars)
  ...
  ✓ Saved chunk_013_pages_121-127.txt (15,432 chars)
  ✓ Saved summary: 00_CHUNKING_SUMMARY.txt

================================================================================
CHUNKING COMPLETE
================================================================================
  Original: 127 pages, 234,567 chars
  Created: 13 chunks
  Output: large_spec_chunks/

Next steps:
  1. Review: large_spec_chunks/00_CHUNKING_SUMMARY.txt
  2. Process chunks sequentially in the skill workflow
================================================================================
```

**Example 3: Section-based chunking**
```bash
$ python3 chunk_large_pdf.py spec.pdf --strategy sections --verbose

================================================================================
PDF Chunking Tool - Processing: spec.pdf
================================================================================

⚠ Chunking needed: Force flag enabled
Extracting text using pdfplumber...
  Extracted page 1/80
  Extracted page 2/80
  ...
Extracted 80 pages, 156,789 characters

Applying 'sections' chunking strategy...

Saving 8 chunks to spec_chunks/
  ✓ Saved chunk_001_pages_1-12.txt (Section: Introduction)
  ✓ Saved chunk_002_pages_13-28.txt (Section: Requirements)
  ✓ Saved chunk_003_pages_29-45.txt (Section: Architecture)
  ...
```

---

## Integration with Skill Workflow

The scripts integrate with the QA skill workflow as follows:

```
Step 1: Prepare          → Check PDF size with chunk_large_pdf.py
                          → If large, create chunks for processing
                          ↓
Step 2: Requirements     → Process PDF chunks (if created)
                          → Extract requirements from all chunks
                          → Combine into 00_requirements.md
                          ↓
Step 3: Test Scenarios   → 03_test_scenarios.md
                          ↓
Step 4: Define Variants  → 04_variants.csv (50 variants)
                          ↓
Step 6: Test Scripts     → 06_test_scripts/ directory
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
1. **Step 1**: `chunk_large_pdf.py` - Handles large PDFs (if needed)
2. **Step 7**: `combinatorial.py` - Optimizes test variants
3. **Step 9**: `rtm_builder.py` - Builds requirements traceability

## Requirements

**Core Requirements:**
- Python 3.7+
- Standard library only (no external dependencies for combinatorial.py and rtm_builder.py)

**PDF Processing Requirements (for chunk_large_pdf.py):**
- One of the following PDF libraries:
  - PyPDF2: `pip install PyPDF2` (recommended)
  - pdfplumber: `pip install pdfplumber` (best quality)
  - pypdf: `pip install pypdf` (modern alternative)

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

### v1.0.0 (2025-11-15) - chunk_large_pdf.py
- Initial release of PDF chunking tool
- Automatic size detection (file size, page count, character count)
- Multiple chunking strategies (auto, pages, size, sections)
- Text extraction with multiple PDF library support (PyPDF2, pdfplumber, pypdf)
- Page number preservation for traceability
- Context overlap between chunks for continuity
- Summary file generation with usage instructions
- Progress tracking and verbose logging
- Comprehensive error handling and graceful degradation
- CLI with argparse for flexible configuration

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

**Last Updated:** 2025-11-15
**Maintainer:** QA Automation Skill
**Scripts:** 4 (chunk_large_pdf.py, combinatorial.py, rtm_builder.py, generate_test_scripts_from_variants.py, validate_test_data.py)
