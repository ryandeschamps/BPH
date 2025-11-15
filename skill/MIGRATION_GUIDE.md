# Migration Guide: Scenario-Based Architecture

## Overview

We've refactored the QA artifact generation system from a **monolithic CSV approach** to a **scenario-based folder architecture**. This change provides better isolation, scalability, and maintainability.

## What Changed?

### Before (Monolithic Architecture)
```
deliverables/
├── 04_variants.csv           # ALL scenarios mixed together (50,000+ rows)
├── 05_test_data.csv          # ALL test data mixed together (50,000+ rows)
└── 06_test_scripts/          # ALL scripts mixed together (50,000+ files)
    ├── TS-001_V00001.txt
    ├── TS-001_V00002.txt
    ├── TS-002_V00865.txt
    └── ...
```

**Problems:**
- ❌ Tight coupling between scenarios
- ❌ Hard to debug individual scenarios
- ❌ Can't work on scenarios independently
- ❌ Poor scalability (monolithic files grow exponentially)
- ❌ No parallelization possible

### After (Scenario-Based Architecture)
```
deliverables/scenarios/
├── TS-001_New_Buyer_Registration/
│   ├── variants.csv                # Only TS-001 variants
│   ├── test_data.csv              # Only TS-001 test data
│   ├── scripts/                    # Only TS-001 scripts
│   │   ├── TS-001_V00001.txt
│   │   └── TS-001_V00002.txt
│   ├── combinatorial_plan.md      # TS-001 optimization
│   └── metrics.json               # TS-001 statistics
│
├── TS-002_Invalid_Email/
│   ├── variants.csv
│   ├── test_data.csv
│   ├── scripts/
│   ├── combinatorial_plan.md
│   └── metrics.json
│
└── ...

deliverables/summary/               # NEW: Aggregate analytics
├── metrics_dashboard.md
├── scenario_index.json
└── all_variants.csv (optional)
```

**Benefits:**
- ✅ **Isolation**: Each scenario is self-contained
- ✅ **Modularity**: Add/remove scenarios independently
- ✅ **Debugging**: Issues isolated to specific folders
- ✅ **Scalability**: Linear growth instead of exponential
- ✅ **Parallelization**: Can generate scenarios concurrently
- ✅ **Clarity**: Folder names show what's being tested

## New Tools

### 1. `scenario_orchestrator.py` (NEW)
Master script for managing per-scenario artifact generation.

```bash
# Generate all artifacts for one scenario
python3 skill/scripts/scenario_orchestrator.py \
  --scenario TS-001 \
  --all-steps \
  --scenarios-file deliverables/03_test_scenarios.md

# Generate variants for all scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps variants \
  --output-dir deliverables/scenarios

# Generate specific scenarios with specific steps
python3 skill/scripts/scenario_orchestrator.py \
  --scenarios TS-001,TS-002,TS-010 \
  --steps variants,test-data,scripts \
  --output-dir deliverables/scenarios \
  --scenarios-file deliverables/03_test_scenarios.md
```

### 2. `summary_aggregator.py` (NEW)
Aggregate metrics across all scenarios.

```bash
# Generate summary reports
python3 skill/scripts/summary_aggregator.py \
  --scenarios-dir deliverables/scenarios

# Include combined variants CSV (legacy compatibility)
python3 skill/scripts/summary_aggregator.py \
  --scenarios-dir deliverables/scenarios \
  --combine-variants
```

### 3. `generate_variants.py` (UPDATED v2.0.0)
Now supports per-scenario mode.

```bash
# NEW: Per-scenario mode
python3 skill/scripts/generate_variants.py \
  --scenario TS-001 \
  --output-dir deliverables/scenarios

# NEW: Multiple scenarios
python3 skill/scripts/generate_variants.py \
  --scenarios TS-001,TS-002,TS-010 \
  --output-dir deliverables/scenarios

# NEW: All scenarios
python3 skill/scripts/generate_variants.py \
  --all \
  --output-dir deliverables/scenarios

# OLD: Legacy monolithic mode (still works)
python3 skill/scripts/generate_variants.py \
  --monolithic \
  --output deliverables/04_variants.csv
```

### 4. `generate_test_data.py` (UPDATED v2.0.0)
Now supports per-scenario mode.

```bash
# NEW: Per-scenario mode
python3 skill/scripts/generate_test_data.py \
  --scenario TS-001 \
  --variants deliverables/scenarios/TS-001/variants.csv \
  --output deliverables/scenarios/TS-001/test_data.csv

# OLD: Legacy monolithic mode (still works)
python3 skill/scripts/generate_test_data.py \
  --monolithic \
  --variants deliverables/04_variants.csv \
  --output deliverables/05_test_data.csv
```

## Migration Steps

### Option 1: Start Fresh with New Architecture (Recommended)

If you're starting a new project, just use the new workflow:

```bash
# Step 1: Generate variants for all scenarios
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps variants \
  --output-dir deliverables/scenarios

# Step 2: Generate test data
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps test-data \
  --output-dir deliverables/scenarios

# Step 3: Generate test scripts
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps scripts \
  --output-dir deliverables/scenarios \
  --scenarios-file deliverables/03_test_scenarios.md

# Step 4: Run combinatorial optimization
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --steps combinatorial \
  --output-dir deliverables/scenarios

# Step 5: Generate summary
python3 skill/scripts/summary_aggregator.py \
  --scenarios-dir deliverables/scenarios
```

Or use the shortcut:

```bash
# All steps at once
python3 skill/scripts/scenario_orchestrator.py \
  --all \
  --all-steps \
  --output-dir deliverables/scenarios \
  --scenarios-file deliverables/03_test_scenarios.md

# Then generate summary
python3 skill/scripts/summary_aggregator.py \
  --scenarios-dir deliverables/scenarios
```

### Option 2: Keep Using Legacy Monolithic Mode

All scripts still support the old `--monolithic` mode:

```bash
# Variants (old way)
python3 skill/scripts/generate_variants.py \
  --monolithic \
  --output deliverables/04_variants.csv

# Test data (old way)
python3 skill/scripts/generate_test_data.py \
  --monolithic \
  --variants deliverables/04_variants.csv \
  --output deliverables/05_test_data.csv

# Everything else works the same
```

### Option 3: Migrate Existing Artifacts

If you have existing monolithic artifacts, you can split them:

```bash
# TODO: Migration script coming soon
python3 skill/scripts/migrate_to_scenarios.py \
  --variants deliverables/04_variants.csv \
  --test-data deliverables/05_test_data.csv \
  --scripts deliverables/06_test_scripts \
  --output deliverables/scenarios
```

## Updated SKILL.md Workflow

The SKILL.md has been updated with the new workflow. Key changes:

- **Step 5 (Variants)**: Now uses `scenario_orchestrator.py` to generate per-scenario variants
- **Step 6 (Test Data)**: Now generates per-scenario test data
- **Step 7 (Scripts)**: Now generates scripts in per-scenario folders
- **Step 8 (Combinatorial)**: Now optimizes per-scenario
- **New Step**: Aggregate summary reports across scenarios

## FAQs

### Q: Do I have to migrate?
**A:** No. The `--monolithic` mode still works. You can keep using the old workflow.

### Q: Can I mix both approaches?
**A:** Yes, but not recommended. Pick one architecture and stick with it.

### Q: How do I combine scenario variants for legacy tools?
**A:** Use `summary_aggregator.py --combine-variants` to generate a combined CSV.

### Q: What about RTM generation?
**A:** RTM builder still works the same way. It can read from either architecture.

### Q: Can I generate scenarios in parallel?
**A:** Not yet, but the architecture supports it. Coming in future update.

### Q: Which mode should I use?
**A:** **Scenario-based** for new projects. It's more scalable and maintainable.

## Performance Comparison

| Aspect | Monolithic | Scenario-Based |
|--------|-----------|----------------|
| Generation Time | Same | Same |
| Debugging | Hard (search 50K rows) | Easy (isolated folders) |
| Scalability | Poor (exponential growth) | Excellent (linear growth) |
| Maintainability | Poor (tight coupling) | Excellent (isolation) |
| Parallelization | Not possible | Possible (future) |
| File Organization | Flat (confusing) | Hierarchical (clear) |

## Breaking Changes

### None!

All changes are **backwards compatible**. The `--monolithic` mode ensures existing workflows continue to work.

## Support

If you encounter issues:
1. Check if you're using `--monolithic` flag for legacy mode
2. Review the updated SKILL.md for new workflow
3. Check script help: `python3 script.py --help`
4. Report issues with detailed error messages

## Conclusion

The scenario-based architecture is a significant improvement that:
- ✅ Makes the system more maintainable
- ✅ Improves scalability
- ✅ Enables future parallelization
- ✅ Provides better debugging experience
- ✅ Maintains backwards compatibility

We recommend adopting the new architecture for all new projects while keeping the legacy mode available for existing workflows.

---

**Updated:** 2025-11-15
**Version:** 2.0.0
