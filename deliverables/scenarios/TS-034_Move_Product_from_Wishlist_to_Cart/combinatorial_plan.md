# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:16

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 120
- **Covered Pairs:** 120
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_State | Device | Network_Speed | Product_State | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-034 | Chrome | Empty | Desktop | High | In_Stock | Buyer |
| 2 | V00122 | TS-034 | Firefox | Has_Items | Mobile | Medium | Out_Of_Stock | Buyer |
| 3 | V00171 | TS-034 | Safari | Empty | Tablet | Low | Price_Changed | Buyer |
| 4 | V00066 | TS-034 | Edge | Has_Items | Desktop | Low | In_Stock | Buyer |
| 5 | V00103 | TS-034 | Edge | Empty | Mobile | High | Out_Of_Stock | Buyer |
| 6 | V00187 | TS-034 | Chrome | Has_Items | Tablet | High | Price_Changed | Buyer |
| 7 | V00017 | TS-034 | Firefox | Empty | Tablet | Medium | In_Stock | Buyer |
| 8 | V00128 | TS-034 | Safari | Has_Items | Desktop | Medium | Out_Of_Stock | Buyer |
| 9 | V00078 | TS-034 | Chrome | Empty | Mobile | Low | Out_Of_Stock | Buyer |
| 10 | V00022 | TS-034 | Safari | Empty | Mobile | High | In_Stock | Buyer |
| 11 | V00154 | TS-034 | Firefox | Empty | Desktop | High | Price_Changed | Buyer |
| 12 | V00176 | TS-034 | Edge | Empty | Mobile | Medium | Price_Changed | Buyer |
| 13 | V00080 | TS-034 | Chrome | Empty | Tablet | Medium | Out_Of_Stock | Buyer |
| 14 | V00012 | TS-034 | Firefox | Empty | Desktop | Low | In_Stock | Buyer |
| 15 | V00034 | TS-034 | Edge | Empty | Tablet | High | In_Stock | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
