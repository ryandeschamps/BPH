# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:10

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 170
- **Covered Pairs:** 170
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 19

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_State | Device | Network_Speed | Product_Variation | Quantity | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-023 | Chrome | Empty | Desktop | High | No_Variation | Single | Buyer |
| 2 | V00266 | TS-023 | Firefox | Has_Items | Mobile | Medium | Size_Selected | Multiple | Buyer |
| 3 | V00351 | TS-023 | Safari | Has_Items | Tablet | Low | Color_Selected | Single | Buyer |
| 4 | V00534 | TS-023 | Edge | Empty | Desktop | Low | Size_And_Color | Multiple | Buyer |
| 5 | V00098 | TS-023 | Safari | Empty | Tablet | Medium | No_Variation | Multiple | Buyer |
| 6 | V00499 | TS-023 | Edge | Has_Items | Mobile | High | Size_And_Color | Single | Buyer |
| 7 | V00160 | TS-023 | Firefox | Empty | Tablet | High | Size_Selected | Single | Buyer |
| 8 | V00364 | TS-023 | Chrome | Empty | Mobile | High | Color_Selected | Multiple | Buyer |
| 9 | V00182 | TS-023 | Chrome | Has_Items | Desktop | Medium | Size_Selected | Single | Buyer |
| 10 | V00051 | TS-023 | Firefox | Has_Items | Mobile | Low | No_Variation | Single | Buyer |
| 11 | V00299 | TS-023 | Firefox | Empty | Desktop | Medium | Color_Selected | Single | Buyer |
| 12 | V00440 | TS-023 | Chrome | Empty | Tablet | Medium | Size_And_Color | Single | Buyer |
| 13 | V00035 | TS-023 | Edge | Empty | Tablet | Medium | No_Variation | Single | Buyer |
| 14 | V00163 | TS-023 | Safari | Empty | Desktop | High | Size_Selected | Single | Buyer |
| 15 | V00147 | TS-023 | Chrome | Empty | Desktop | Low | Size_Selected | Single | Buyer |
| 16 | V00454 | TS-023 | Safari | Empty | Mobile | High | Size_And_Color | Single | Buyer |
| 17 | V00172 | TS-023 | Edge | Empty | Desktop | High | Size_Selected | Single | Buyer |
| 18 | V00316 | TS-023 | Edge | Empty | Desktop | High | Color_Selected | Single | Buyer |
| 19 | V00442 | TS-023 | Firefox | Empty | Desktop | High | Size_And_Color | Single | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
