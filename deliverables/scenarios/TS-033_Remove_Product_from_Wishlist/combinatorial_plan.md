# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:15

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 106
- **Covered Pairs:** 106
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 14

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Removal_Action | User_Type | Wishlist_State |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-033 | Chrome | Desktop | High | Remove_One | Buyer | Single_Item |
| 2 | V00122 | TS-033 | Firefox | Mobile | Medium | Remove_All | Buyer | Multiple_Items |
| 3 | V00063 | TS-033 | Safari | Tablet | Low | Remove_All | Buyer | Single_Item |
| 4 | V00102 | TS-033 | Edge | Desktop | Low | Remove_One | Buyer | Multiple_Items |
| 5 | V00017 | TS-033 | Firefox | Tablet | Medium | Remove_One | Buyer | Single_Item |
| 6 | V00067 | TS-033 | Edge | Mobile | High | Remove_All | Buyer | Single_Item |
| 7 | V00094 | TS-033 | Safari | Mobile | High | Remove_One | Buyer | Multiple_Items |
| 8 | V00110 | TS-033 | Chrome | Desktop | Medium | Remove_All | Buyer | Multiple_Items |
| 9 | V00006 | TS-033 | Chrome | Mobile | Low | Remove_One | Buyer | Single_Item |
| 10 | V00079 | TS-033 | Chrome | Tablet | High | Remove_One | Buyer | Multiple_Items |
| 11 | V00010 | TS-033 | Firefox | Desktop | High | Remove_One | Buyer | Single_Item |
| 12 | V00020 | TS-033 | Safari | Desktop | Medium | Remove_One | Buyer | Single_Item |
| 13 | V00035 | TS-033 | Edge | Tablet | Medium | Remove_One | Buyer | Single_Item |
| 14 | V00012 | TS-033 | Firefox | Desktop | Low | Remove_One | Buyer | Single_Item |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
