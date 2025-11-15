# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:14

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 120
- **Covered Pairs:** 120
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Product_State | User_Type | Wishlist_State |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-030 | Chrome | Desktop | High | In_Stock | Buyer | Empty |
| 2 | V00122 | TS-030 | Firefox | Mobile | Medium | Out_Of_Stock | Buyer | Has_Items |
| 3 | V00171 | TS-030 | Safari | Tablet | Low | In_Stock | Buyer | Product_Already_In_Wishlist |
| 4 | V00066 | TS-030 | Edge | Desktop | Low | Out_Of_Stock | Buyer | Empty |
| 5 | V00103 | TS-030 | Edge | Mobile | High | In_Stock | Buyer | Has_Items |
| 6 | V00187 | TS-030 | Chrome | Tablet | High | Out_Of_Stock | Buyer | Product_Already_In_Wishlist |
| 7 | V00017 | TS-030 | Firefox | Tablet | Medium | In_Stock | Buyer | Empty |
| 8 | V00128 | TS-030 | Safari | Desktop | Medium | Out_Of_Stock | Buyer | Has_Items |
| 9 | V00078 | TS-030 | Chrome | Mobile | Low | In_Stock | Buyer | Has_Items |
| 10 | V00022 | TS-030 | Safari | Mobile | High | In_Stock | Buyer | Empty |
| 11 | V00154 | TS-030 | Firefox | Desktop | High | In_Stock | Buyer | Product_Already_In_Wishlist |
| 12 | V00176 | TS-030 | Edge | Mobile | Medium | In_Stock | Buyer | Product_Already_In_Wishlist |
| 13 | V00080 | TS-030 | Chrome | Tablet | Medium | In_Stock | Buyer | Has_Items |
| 14 | V00012 | TS-030 | Firefox | Desktop | Low | In_Stock | Buyer | Empty |
| 15 | V00034 | TS-030 | Edge | Tablet | High | In_Stock | Buyer | Empty |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
