# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:42:59

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 92
- **Covered Pairs:** 92
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 14

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Account_State | Browser | Device | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-006 | Active_Verified | Chrome | Desktop | Valid | High | Buyer |
| 2 | V00050 | TS-006 | Active_Multiple_Sessions | Firefox | Mobile | Valid | Medium | Buyer |
| 3 | V00027 | TS-006 | Active_Verified | Safari | Tablet | Valid | Low | Buyer |
| 4 | V00066 | TS-006 | Active_Multiple_Sessions | Edge | Desktop | Valid | Low | Buyer |
| 5 | V00031 | TS-006 | Active_Verified | Edge | Mobile | Valid | High | Buyer |
| 6 | V00043 | TS-006 | Active_Multiple_Sessions | Chrome | Tablet | Valid | High | Buyer |
| 7 | V00011 | TS-006 | Active_Verified | Firefox | Desktop | Valid | Medium | Buyer |
| 8 | V00006 | TS-006 | Active_Verified | Chrome | Mobile | Valid | Low | Buyer |
| 9 | V00035 | TS-006 | Active_Verified | Edge | Tablet | Valid | Medium | Buyer |
| 10 | V00055 | TS-006 | Active_Multiple_Sessions | Safari | Desktop | Valid | High | Buyer |
| 11 | V00016 | TS-006 | Active_Verified | Firefox | Tablet | Valid | High | Buyer |
| 12 | V00023 | TS-006 | Active_Verified | Safari | Mobile | Valid | Medium | Buyer |
| 13 | V00002 | TS-006 | Active_Verified | Chrome | Desktop | Valid | Medium | Buyer |
| 14 | V00012 | TS-006 | Active_Verified | Firefox | Desktop | Valid | Low | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
