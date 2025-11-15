# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:09

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 152
- **Covered Pairs:** 152
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 16

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | User_Type | Variation_Availability | Variation_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-021 | Chrome | Desktop | High | Visitor | All_Available | Size_Only |
| 2 | V00482 | TS-021 | Firefox | Mobile | Medium | Buyer | Some_Out_Of_Stock | Color_Only |
| 3 | V00315 | TS-021 | Safari | Tablet | Low | Visitor | All_Out_Of_Stock | Size_And_Color |
| 4 | V00357 | TS-021 | Edge | Mobile | Low | Buyer | All_Available | Size_Only |
| 5 | V00178 | TS-021 | Edge | Tablet | High | Visitor | Some_Out_Of_Stock | Color_Only |
| 6 | V00614 | TS-021 | Chrome | Desktop | Medium | Buyer | All_Out_Of_Stock | Size_And_Color |
| 7 | V00017 | TS-021 | Firefox | Tablet | Medium | Visitor | All_Available | Size_Only |
| 8 | V00301 | TS-021 | Firefox | Mobile | High | Visitor | All_Out_Of_Stock | Size_And_Color |
| 9 | V00489 | TS-021 | Safari | Desktop | Low | Buyer | Some_Out_Of_Stock | Color_Only |
| 10 | V00346 | TS-021 | Safari | Mobile | High | Buyer | All_Available | Size_Only |
| 11 | V00369 | TS-021 | Chrome | Tablet | Low | Buyer | Some_Out_Of_Stock | Size_Only |
| 12 | V00101 | TS-021 | Edge | Desktop | Medium | Visitor | All_Out_Of_Stock | Size_Only |
| 13 | V00112 | TS-021 | Chrome | Mobile | High | Visitor | All_Available | Color_Only |
| 14 | V00192 | TS-021 | Firefox | Desktop | Low | Visitor | All_Out_Of_Stock | Color_Only |
| 15 | V00236 | TS-021 | Safari | Desktop | Medium | Visitor | All_Available | Size_And_Color |
| 16 | V00280 | TS-021 | Edge | Desktop | High | Visitor | Some_Out_Of_Stock | Size_And_Color |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
