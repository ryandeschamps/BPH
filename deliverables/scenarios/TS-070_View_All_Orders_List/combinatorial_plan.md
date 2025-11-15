# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:34

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Order_Filter | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-070 | Chrome | Desktop | High | All | Admin |
| 2 | V00050 | TS-070 | Firefox | Mobile | Medium | By_Status | Admin |
| 3 | V00099 | TS-070 | Safari | Tablet | Low | By_Date | Admin |
| 4 | V00033 | TS-070 | Edge | Mobile | Low | All | Admin |
| 5 | V00070 | TS-070 | Edge | Tablet | High | By_Status | Admin |
| 6 | V00101 | TS-070 | Edge | Desktop | Medium | By_Date | Admin |
| 7 | V00008 | TS-070 | Chrome | Tablet | Medium | All | Admin |
| 8 | V00039 | TS-070 | Chrome | Desktop | Low | By_Status | Admin |
| 9 | V00076 | TS-070 | Chrome | Mobile | High | By_Date | Admin |
| 10 | V00010 | TS-070 | Firefox | Desktop | High | All | Admin |
| 11 | V00019 | TS-070 | Safari | Desktop | High | All | Admin |
| 12 | V00059 | TS-070 | Safari | Mobile | Medium | By_Status | Admin |
| 13 | V00090 | TS-070 | Firefox | Tablet | Low | By_Date | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
