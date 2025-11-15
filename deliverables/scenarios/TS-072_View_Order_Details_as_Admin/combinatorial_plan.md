# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:35

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Order_Details | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-072 | Chrome | Desktop | High | Basic | Admin |
| 2 | V00050 | TS-072 | Firefox | Mobile | Medium | With_Items | Admin |
| 3 | V00099 | TS-072 | Safari | Tablet | Low | With_Payment | Admin |
| 4 | V00033 | TS-072 | Edge | Mobile | Low | Basic | Admin |
| 5 | V00070 | TS-072 | Edge | Tablet | High | With_Items | Admin |
| 6 | V00101 | TS-072 | Edge | Desktop | Medium | With_Payment | Admin |
| 7 | V00008 | TS-072 | Chrome | Tablet | Medium | Basic | Admin |
| 8 | V00039 | TS-072 | Chrome | Desktop | Low | With_Items | Admin |
| 9 | V00076 | TS-072 | Chrome | Mobile | High | With_Payment | Admin |
| 10 | V00010 | TS-072 | Firefox | Desktop | High | Basic | Admin |
| 11 | V00019 | TS-072 | Safari | Desktop | High | Basic | Admin |
| 12 | V00059 | TS-072 | Safari | Mobile | Medium | With_Items | Admin |
| 13 | V00090 | TS-072 | Firefox | Tablet | Low | With_Payment | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
