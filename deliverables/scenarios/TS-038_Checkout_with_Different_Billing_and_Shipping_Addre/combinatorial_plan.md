# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:18

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 153
- **Covered Pairs:** 153
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Address_State | Address_Type | Browser | Device | Network_Speed | Payment_Method | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-038 | Both_New | Different_Addresses | Chrome | Desktop | High | Credit_Card | Buyer |
| 2 | V00158 | TS-038 | Both_Saved | Different_Addresses | Firefox | Mobile | Medium | Debit_Card | Buyer |
| 3 | V00315 | TS-038 | Mixed | Different_Addresses | Safari | Tablet | Low | Net_Banking | Buyer |
| 4 | V00033 | TS-038 | Both_New | Different_Addresses | Edge | Mobile | Low | Credit_Card | Buyer |
| 5 | V00178 | TS-038 | Both_Saved | Different_Addresses | Edge | Tablet | High | Debit_Card | Buyer |
| 6 | V00317 | TS-038 | Mixed | Different_Addresses | Edge | Desktop | Medium | Net_Banking | Buyer |
| 7 | V00017 | TS-038 | Both_New | Different_Addresses | Firefox | Tablet | Medium | Credit_Card | Buyer |
| 8 | V00147 | TS-038 | Both_Saved | Different_Addresses | Chrome | Desktop | Low | Debit_Card | Buyer |
| 9 | V00292 | TS-038 | Mixed | Different_Addresses | Chrome | Mobile | High | Net_Banking | Buyer |
| 10 | V00055 | TS-038 | Both_New | Different_Addresses | Safari | Desktop | High | Debit_Card | Buyer |
| 11 | V00131 | TS-038 | Both_Saved | Different_Addresses | Safari | Mobile | Medium | Credit_Card | Buyer |
| 12 | V00082 | TS-038 | Both_New | Different_Addresses | Firefox | Desktop | High | Net_Banking | Buyer |
| 13 | V00188 | TS-038 | Both_Saved | Different_Addresses | Chrome | Tablet | Medium | Net_Banking | Buyer |
| 14 | V00228 | TS-038 | Mixed | Different_Addresses | Firefox | Desktop | Low | Credit_Card | Buyer |
| 15 | V00253 | TS-038 | Mixed | Different_Addresses | Chrome | Desktop | High | Debit_Card | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
