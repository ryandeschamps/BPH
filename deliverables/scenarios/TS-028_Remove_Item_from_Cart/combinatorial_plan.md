# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:13

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 120
- **Covered Pairs:** 120
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_State | Device | Network_Speed | Removal_Action | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-028 | Chrome | Single_Item | Desktop | High | Remove_One | Buyer |
| 2 | V00158 | TS-028 | Firefox | Multiple_Items | Mobile | Medium | Remove_All | Buyer |
| 3 | V00099 | TS-028 | Safari | Single_Item | Tablet | Low | Remove_Last_Item | Buyer |
| 4 | V00138 | TS-028 | Edge | Multiple_Items | Desktop | Low | Remove_One | Buyer |
| 5 | V00067 | TS-028 | Edge | Single_Item | Mobile | High | Remove_All | Buyer |
| 6 | V00187 | TS-028 | Chrome | Multiple_Items | Tablet | High | Remove_Last_Item | Buyer |
| 7 | V00017 | TS-028 | Firefox | Single_Item | Tablet | Medium | Remove_One | Buyer |
| 8 | V00164 | TS-028 | Safari | Multiple_Items | Desktop | Medium | Remove_All | Buyer |
| 9 | V00042 | TS-028 | Chrome | Single_Item | Mobile | Low | Remove_All | Buyer |
| 10 | V00022 | TS-028 | Safari | Single_Item | Mobile | High | Remove_One | Buyer |
| 11 | V00082 | TS-028 | Firefox | Single_Item | Desktop | High | Remove_Last_Item | Buyer |
| 12 | V00104 | TS-028 | Edge | Single_Item | Mobile | Medium | Remove_Last_Item | Buyer |
| 13 | V00044 | TS-028 | Chrome | Single_Item | Tablet | Medium | Remove_All | Buyer |
| 14 | V00012 | TS-028 | Firefox | Single_Item | Desktop | Low | Remove_One | Buyer |
| 15 | V00034 | TS-028 | Edge | Single_Item | Tablet | High | Remove_One | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
