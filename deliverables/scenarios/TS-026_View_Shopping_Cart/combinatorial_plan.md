# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:12

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 150
- **Covered Pairs:** 150
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 19

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_State | Device | Item_Availability | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-026 | Chrome | Empty | Desktop | All_Available | High | Buyer |
| 2 | V00158 | TS-026 | Firefox | Single_Item | Mobile | Some_Out_Of_Stock | Medium | Buyer |
| 3 | V00315 | TS-026 | Safari | Multiple_Items | Tablet | Price_Changed | Low | Buyer |
| 4 | V00357 | TS-026 | Edge | Mixed_Variations | Mobile | All_Available | Low | Buyer |
| 5 | V00070 | TS-026 | Edge | Empty | Tablet | Some_Out_Of_Stock | High | Buyer |
| 6 | V00209 | TS-026 | Edge | Single_Item | Desktop | Price_Changed | Medium | Buyer |
| 7 | V00085 | TS-026 | Firefox | Empty | Mobile | Price_Changed | High | Buyer |
| 8 | V00116 | TS-026 | Chrome | Single_Item | Tablet | All_Available | Medium | Buyer |
| 9 | V00255 | TS-026 | Chrome | Multiple_Items | Desktop | Some_Out_Of_Stock | Low | Buyer |
| 10 | V00379 | TS-026 | Safari | Mixed_Variations | Desktop | Some_Out_Of_Stock | High | Buyer |
| 11 | V00239 | TS-026 | Safari | Multiple_Items | Mobile | All_Available | Medium | Buyer |
| 12 | V00341 | TS-026 | Firefox | Mixed_Variations | Tablet | All_Available | Medium | Buyer |
| 13 | V00400 | TS-026 | Chrome | Mixed_Variations | Mobile | Price_Changed | High | Buyer |
| 14 | V00012 | TS-026 | Firefox | Empty | Desktop | All_Available | Low | Buyer |
| 15 | V00020 | TS-026 | Safari | Empty | Desktop | All_Available | Medium | Buyer |
| 16 | V00127 | TS-026 | Safari | Single_Item | Desktop | All_Available | High | Buyer |
| 17 | V00226 | TS-026 | Firefox | Multiple_Items | Desktop | All_Available | High | Buyer |
| 18 | V00111 | TS-026 | Chrome | Single_Item | Desktop | All_Available | Low | Buyer |
| 19 | V00244 | TS-026 | Edge | Multiple_Items | Desktop | All_Available | High | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
