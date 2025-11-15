# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:32

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 102
- **Covered Pairs:** 102
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 17

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Buyer_Status | Device | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-066 | Chrome | Active | Desktop | High | Admin |
| 2 | V00050 | TS-066 | Firefox | Inactive | Mobile | Medium | Admin |
| 3 | V00099 | TS-066 | Safari | Has_Orders | Tablet | Low | Admin |
| 4 | V00137 | TS-066 | Edge | No_Orders | Desktop | Medium | Admin |
| 5 | V00033 | TS-066 | Edge | Active | Mobile | Low | Admin |
| 6 | V00070 | TS-066 | Edge | Inactive | Tablet | High | Admin |
| 7 | V00130 | TS-066 | Safari | No_Orders | Mobile | High | Admin |
| 8 | V00008 | TS-066 | Chrome | Active | Tablet | Medium | Admin |
| 9 | V00039 | TS-066 | Chrome | Inactive | Desktop | Low | Admin |
| 10 | V00082 | TS-066 | Firefox | Has_Orders | Desktop | High | Admin |
| 11 | V00126 | TS-066 | Firefox | No_Orders | Tablet | Low | Admin |
| 12 | V00077 | TS-066 | Chrome | Has_Orders | Mobile | Medium | Admin |
| 13 | V00020 | TS-066 | Safari | Active | Desktop | Medium | Admin |
| 14 | V00010 | TS-066 | Firefox | Active | Desktop | High | Admin |
| 15 | V00055 | TS-066 | Safari | Inactive | Desktop | High | Admin |
| 16 | V00100 | TS-066 | Edge | Has_Orders | Desktop | High | Admin |
| 17 | V00109 | TS-066 | Chrome | No_Orders | Desktop | High | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
