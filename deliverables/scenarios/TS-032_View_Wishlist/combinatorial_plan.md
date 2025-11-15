# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:15

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 135
- **Covered Pairs:** 135
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Item_Availability | Network_Speed | User_Type | Wishlist_State |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-032 | Chrome | Desktop | All_Available | High | Buyer | Empty |
| 2 | V00158 | TS-032 | Firefox | Mobile | Some_Out_Of_Stock | Medium | Buyer | Single_Item |
| 3 | V00315 | TS-032 | Safari | Tablet | Price_Changed | Low | Buyer | Multiple_Items |
| 4 | V00033 | TS-032 | Edge | Mobile | All_Available | Low | Buyer | Empty |
| 5 | V00178 | TS-032 | Edge | Tablet | Some_Out_Of_Stock | High | Buyer | Single_Item |
| 6 | V00317 | TS-032 | Edge | Desktop | Price_Changed | Medium | Buyer | Multiple_Items |
| 7 | V00017 | TS-032 | Firefox | Tablet | All_Available | Medium | Buyer | Empty |
| 8 | V00147 | TS-032 | Chrome | Desktop | Some_Out_Of_Stock | Low | Buyer | Single_Item |
| 9 | V00292 | TS-032 | Chrome | Mobile | Price_Changed | High | Buyer | Multiple_Items |
| 10 | V00055 | TS-032 | Safari | Desktop | Some_Out_Of_Stock | High | Buyer | Empty |
| 11 | V00131 | TS-032 | Safari | Mobile | All_Available | Medium | Buyer | Single_Item |
| 12 | V00082 | TS-032 | Firefox | Desktop | Price_Changed | High | Buyer | Empty |
| 13 | V00188 | TS-032 | Chrome | Tablet | Price_Changed | Medium | Buyer | Single_Item |
| 14 | V00228 | TS-032 | Firefox | Desktop | All_Available | Low | Buyer | Multiple_Items |
| 15 | V00253 | TS-032 | Chrome | Desktop | Some_Out_Of_Stock | High | Buyer | Multiple_Items |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
