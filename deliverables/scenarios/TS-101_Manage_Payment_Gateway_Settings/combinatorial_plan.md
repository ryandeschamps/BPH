# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:47

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Payment_Status | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-101 | Chrome | Desktop | High | Pending | Admin |
| 2 | V00050 | TS-101 | Firefox | Mobile | Medium | Completed | Admin |
| 3 | V00099 | TS-101 | Safari | Tablet | Low | Failed | Admin |
| 4 | V00033 | TS-101 | Edge | Mobile | Low | Pending | Admin |
| 5 | V00070 | TS-101 | Edge | Tablet | High | Completed | Admin |
| 6 | V00101 | TS-101 | Edge | Desktop | Medium | Failed | Admin |
| 7 | V00008 | TS-101 | Chrome | Tablet | Medium | Pending | Admin |
| 8 | V00039 | TS-101 | Chrome | Desktop | Low | Completed | Admin |
| 9 | V00076 | TS-101 | Chrome | Mobile | High | Failed | Admin |
| 10 | V00010 | TS-101 | Firefox | Desktop | High | Pending | Admin |
| 11 | V00019 | TS-101 | Safari | Desktop | High | Pending | Admin |
| 12 | V00059 | TS-101 | Safari | Mobile | Medium | Completed | Admin |
| 13 | V00090 | TS-101 | Firefox | Tablet | Low | Failed | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
