# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:12

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 134
- **Covered Pairs:** 134
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 17

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Quantity_Change | Stock_Level | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-027 | Chrome | Desktop | High | Increase | Sufficient | Buyer |
| 2 | V00122 | TS-027 | Firefox | Mobile | Medium | Decrease | Insufficient | Buyer |
| 3 | V00171 | TS-027 | Safari | Tablet | Low | Max_Limit | Sufficient | Buyer |
| 4 | V00282 | TS-027 | Edge | Desktop | Low | Zero | Insufficient | Buyer |
| 5 | V00032 | TS-027 | Edge | Mobile | Medium | Increase | Sufficient | Buyer |
| 6 | V00052 | TS-027 | Firefox | Tablet | High | Increase | Insufficient | Buyer |
| 7 | V00182 | TS-027 | Chrome | Desktop | Medium | Max_Limit | Insufficient | Buyer |
| 8 | V00238 | TS-027 | Safari | Mobile | High | Zero | Sufficient | Buyer |
| 9 | V00078 | TS-027 | Chrome | Mobile | Low | Decrease | Sufficient | Buyer |
| 10 | V00106 | TS-027 | Edge | Tablet | High | Decrease | Sufficient | Buyer |
| 11 | V00128 | TS-027 | Safari | Desktop | Medium | Decrease | Insufficient | Buyer |
| 12 | V00224 | TS-027 | Chrome | Tablet | Medium | Zero | Sufficient | Buyer |
| 13 | V00012 | TS-027 | Firefox | Desktop | Low | Increase | Sufficient | Buyer |
| 14 | V00157 | TS-027 | Firefox | Mobile | High | Max_Limit | Sufficient | Buyer |
| 15 | V00019 | TS-027 | Safari | Desktop | High | Increase | Sufficient | Buyer |
| 16 | V00172 | TS-027 | Edge | Desktop | High | Max_Limit | Sufficient | Buyer |
| 17 | V00226 | TS-027 | Firefox | Desktop | High | Zero | Sufficient | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
