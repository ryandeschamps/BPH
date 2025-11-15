# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:26

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Password_Validity | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-052 | Chrome | Desktop | High | Valid | Buyer |
| 2 | V00050 | TS-052 | Firefox | Mobile | Medium | Invalid | Buyer |
| 3 | V00099 | TS-052 | Safari | Tablet | Low | Weak | Buyer |
| 4 | V00033 | TS-052 | Edge | Mobile | Low | Valid | Buyer |
| 5 | V00070 | TS-052 | Edge | Tablet | High | Invalid | Buyer |
| 6 | V00101 | TS-052 | Edge | Desktop | Medium | Weak | Buyer |
| 7 | V00008 | TS-052 | Chrome | Tablet | Medium | Valid | Buyer |
| 8 | V00039 | TS-052 | Chrome | Desktop | Low | Invalid | Buyer |
| 9 | V00076 | TS-052 | Chrome | Mobile | High | Weak | Buyer |
| 10 | V00010 | TS-052 | Firefox | Desktop | High | Valid | Buyer |
| 11 | V00019 | TS-052 | Safari | Desktop | High | Valid | Buyer |
| 12 | V00059 | TS-052 | Safari | Mobile | Medium | Invalid | Buyer |
| 13 | V00090 | TS-052 | Firefox | Tablet | Low | Weak | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
