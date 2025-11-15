# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:11

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 150
- **Covered Pairs:** 150
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 19

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Quantity | Stock_Level | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-025 | Chrome | Desktop | High | Two | Sufficient | Buyer |
| 2 | V00158 | TS-025 | Firefox | Mobile | Medium | Five | Insufficient | Buyer |
| 3 | V00315 | TS-025 | Safari | Tablet | Low | Ten | Exact_Match | Buyer |
| 4 | V00357 | TS-025 | Edge | Mobile | Low | Hundred | Sufficient | Buyer |
| 5 | V00070 | TS-025 | Edge | Tablet | High | Two | Insufficient | Buyer |
| 6 | V00209 | TS-025 | Edge | Desktop | Medium | Five | Exact_Match | Buyer |
| 7 | V00085 | TS-025 | Firefox | Mobile | High | Two | Exact_Match | Buyer |
| 8 | V00116 | TS-025 | Chrome | Tablet | Medium | Five | Sufficient | Buyer |
| 9 | V00255 | TS-025 | Chrome | Desktop | Low | Ten | Insufficient | Buyer |
| 10 | V00379 | TS-025 | Safari | Desktop | High | Hundred | Insufficient | Buyer |
| 11 | V00239 | TS-025 | Safari | Mobile | Medium | Ten | Sufficient | Buyer |
| 12 | V00341 | TS-025 | Firefox | Tablet | Medium | Hundred | Sufficient | Buyer |
| 13 | V00400 | TS-025 | Chrome | Mobile | High | Hundred | Exact_Match | Buyer |
| 14 | V00012 | TS-025 | Firefox | Desktop | Low | Two | Sufficient | Buyer |
| 15 | V00020 | TS-025 | Safari | Desktop | Medium | Two | Sufficient | Buyer |
| 16 | V00127 | TS-025 | Safari | Desktop | High | Five | Sufficient | Buyer |
| 17 | V00226 | TS-025 | Firefox | Desktop | High | Ten | Sufficient | Buyer |
| 18 | V00111 | TS-025 | Chrome | Desktop | Low | Five | Sufficient | Buyer |
| 19 | V00244 | TS-025 | Edge | Desktop | High | Ten | Sufficient | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
