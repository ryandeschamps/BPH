# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:32

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Buyer_Filter | Device | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-065 | Chrome | All | Desktop | High | Admin |
| 2 | V00050 | TS-065 | Firefox | Active | Mobile | Medium | Admin |
| 3 | V00099 | TS-065 | Safari | Inactive | Tablet | Low | Admin |
| 4 | V00033 | TS-065 | Edge | All | Mobile | Low | Admin |
| 5 | V00070 | TS-065 | Edge | Active | Tablet | High | Admin |
| 6 | V00101 | TS-065 | Edge | Inactive | Desktop | Medium | Admin |
| 7 | V00008 | TS-065 | Chrome | All | Tablet | Medium | Admin |
| 8 | V00039 | TS-065 | Chrome | Active | Desktop | Low | Admin |
| 9 | V00076 | TS-065 | Chrome | Inactive | Mobile | High | Admin |
| 10 | V00010 | TS-065 | Firefox | All | Desktop | High | Admin |
| 11 | V00019 | TS-065 | Safari | All | Desktop | High | Admin |
| 12 | V00059 | TS-065 | Safari | Active | Mobile | Medium | Admin |
| 13 | V00090 | TS-065 | Firefox | Inactive | Tablet | Low | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
