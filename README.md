# Automated QA Test Artifact Generation with Claude

## Overview

This repository demonstrates the power of **Claude's Skill.md capabilities** to automatically generate comprehensive QA test documentation from Business Requirements Documents (BRDs). Using a custom skill (`SKILL.md`), Claude transforms a single BRD into a complete suite of professional-grade test artifacts suitable for enterprise software testing.

## What This Repository Showcases

Starting from a single **38-page Business Requirements Document** for an ecommerce website (online apparels shopping platform), this project demonstrates the automated generation of:

### Complete QA Test Suite
- **125 Test Scenarios** - User story format covering all functional areas
- **125 Test Scripts** - Detailed Given/When/Then format with preconditions and expected results
- **50 Parameter Variants** - Optimized using pairwise combinatorial testing
- **Comprehensive Test Plan** - 31-page master test plan with strategy, scope, and execution details
- **Combinatorial Test Execution Plan** - Optimized test execution strategy reducing 62,500+ combinations to 200-300 executions
- **Requirements Traceability Matrix (RTM)** - Complete bidirectional traceability between requirements and test artifacts
- **Test Data Specification** - Sample test data for execution
- **Requirements Assessment** - Analysis of functional and non-functional requirements

### Coverage Metrics
- **100% Requirement Coverage** - All 26 functional requirements mapped to test scenarios
- **90.7% Pairwise Coverage** - Efficient parameter interaction testing
- **125/125 Test Scripts** - Complete scenario-to-script mapping

## Repository Structure

```
BPH/
├── BRD.pdf                        # Source Business Requirements Document
├── SKILL.md                       # Claude skill definition for QA generation
├── README.md                      # This file
└── deliverables/
    ├── 01_requirements_assessment.md  # FR/NFR analysis and risk assessment
    ├── 02_entities_and_flows.md       # System entities and user flows
    ├── 03_test_scenarios.md           # 125 test scenarios in user story format
    ├── 04_variants.csv                # 50 optimized parameter combinations
    ├── 05_test_data.csv               # Test data specification
    ├── 06_test_scripts/               # 125 detailed test scripts (TS-001 to TS-125)
    │   ├── TS-001.txt through TS-125.txt
    │   └── TEST_SCRIPTS_SUMMARY.md
    ├── 07_combinatorial_plan.md       # Combinatorial testing strategy
    ├── 08_test_plan.md                # Comprehensive master test plan
    └── 09_rtm.csv                     # Requirements Traceability Matrix
```

## How It Was Created

### 1. Custom Skill Definition
A custom Claude skill was defined in `SKILL.md` that encodes:
- QA best practices and methodologies
- Test artifact templates and formats
- Combinatorial testing principles
- Industry-standard test documentation structures

### 2. Automated Generation Process
Using Claude with the custom skill:

**Step 1**: Requirements Analysis
- Parsed the BRD to extract 26 functional requirements and 4 non-functional requirements
- Identified system entities, user roles, and workflows
- Assessed testing risks and priorities

**Step 2**: Test Scenario Generation
- Generated 125 comprehensive test scenarios covering:
  - Visitor/Guest functionality (10 scenarios)
  - Buyer registration & authentication (7 scenarios)
  - Shopping features (8 scenarios)
  - Checkout & payment (11 scenarios)
  - Order management (5 scenarios)
  - Account management (6 scenarios)
  - Admin functions (60 scenarios)
  - System features (4 scenarios)
  - Error handling (5 scenarios)

**Step 3**: Combinatorial Optimization
- Identified 13 test parameters (browser, device, user type, payment method, etc.)
- Applied pairwise combinatorial testing to reduce 10,000+ combinations to 50 optimized variants
- Achieved 90.7% pairwise coverage with 99.5% reduction in test cases

**Step 4**: Detailed Test Script Creation
- Generated 125 detailed test scripts in Given/When/Then format
- Each script includes preconditions, step-by-step actions, and expected results
- Mapped to corresponding requirements for traceability

**Step 5**: Test Planning & Strategy
- Created comprehensive test plan with execution strategy, resource allocation, and metrics
- Developed combinatorial execution plan with phased approach
- Generated requirements traceability matrix (RTM)

### 3. Key Technologies
- **Claude (Sonnet 4.5)** - AI-powered test artifact generation
- **Skill.md** - Custom skill definition for QA domain expertise
- **Combinatorial Testing** - Pairwise testing methodology for efficient coverage

## Exploring the Artifacts

### Start Here
1. **BRD.pdf** - Review the source business requirements
2. **SKILL.md** - Understand the skill that drives the generation
3. **deliverables/01_requirements_assessment.md** - See how requirements were analyzed
4. **deliverables/03_test_scenarios.md** - Browse all 125 test scenarios
5. **deliverables/08_test_plan.md** - Comprehensive test plan overview

### Deep Dive
- **Test Scripts**: Explore `deliverables/06_test_scripts/` for detailed Given/When/Then test cases
- **Combinatorial Strategy**: Review `deliverables/07_combinatorial_plan.md` for optimization approach
- **Traceability**: Check `deliverables/09_rtm.csv` for requirement-to-test mapping

## Key Highlights

### Comprehensive Coverage
- **All functional requirements** tested across multiple dimensions
- **Positive, negative, and edge cases** included
- **Cross-browser and cross-device** testing planned
- **Integration points** (payment gateway, social login, email) covered

### Industry Best Practices
- Given/When/Then format for test scripts
- User story format for test scenarios
- Combinatorial testing for efficiency
- Risk-based test prioritization
- Complete requirements traceability

### Production-Ready
All artifacts are:
- ✅ Professional quality suitable for enterprise use
- ✅ Comprehensive and detailed
- ✅ Following industry standards
- ✅ Ready for test execution
- ✅ Fully traceable to requirements

## Use Cases

This approach can be applied to:
- **Software Development Projects** - Generate test artifacts from requirements documents
- **QA Process Automation** - Reduce manual test planning effort
- **Requirements Validation** - Identify gaps and ambiguities through test scenario generation
- **Test Coverage Analysis** - Ensure comprehensive requirement coverage
- **Knowledge Transfer** - Capture testing knowledge in structured formats

## Business Value

### Time Savings
- Traditional manual approach: **2-4 weeks** for experienced QA team
- Automated with Claude: **Hours** with human review

### Quality Improvements
- Consistent methodology across all test scenarios
- Comprehensive coverage through systematic approach
- Reduced human error in test planning
- Built-in best practices and standards

### Cost Efficiency
- Reduced QA planning effort by 90%+
- Faster time-to-testing
- Lower barrier to entry for test automation

## Technology Stack

- **AI**: Claude (Anthropic) - Sonnet 4.5 model
- **Framework**: Custom Skill.md for QA domain expertise
- **Methodology**: Combinatorial testing, risk-based testing, user story mapping
- **Output Formats**: Markdown, CSV, TXT

## License

This is a demonstration repository showcasing AI-assisted QA artifact generation.

## Acknowledgments

Generated using Claude's Skill.md capabilities, demonstrating the potential of AI-assisted software testing and quality assurance.

---

**Generated**: November 2025
**Source BRD**: Online Apparels Shopping Website (38 pages, 26 functional requirements)
**Total Artifacts**: 9 core deliverables + 125 test scripts
**Test Coverage**: 100% requirement coverage, 90.7% pairwise parameter coverage