# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:02

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 137
- **Covered Pairs:** 137
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Email_State | Input_Validity | Network_Speed | Reset_Link_State | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-011 | Chrome | Desktop | Registered | Valid | High | Valid | Buyer |
| 2 | V00158 | TS-011 | Firefox | Mobile | Verified | Valid | Medium | Expired | Buyer |
| 3 | V00099 | TS-011 | Safari | Tablet | Registered | Valid | Low | Already_Used | Buyer |
| 4 | V00138 | TS-011 | Edge | Desktop | Verified | Valid | Low | Valid | Buyer |
| 5 | V00067 | TS-011 | Edge | Mobile | Registered | Valid | High | Expired | Buyer |
| 6 | V00187 | TS-011 | Chrome | Tablet | Verified | Valid | High | Already_Used | Buyer |
| 7 | V00017 | TS-011 | Firefox | Tablet | Registered | Valid | Medium | Valid | Buyer |
| 8 | V00164 | TS-011 | Safari | Desktop | Verified | Valid | Medium | Expired | Buyer |
| 9 | V00042 | TS-011 | Chrome | Mobile | Registered | Valid | Low | Expired | Buyer |
| 10 | V00022 | TS-011 | Safari | Mobile | Registered | Valid | High | Valid | Buyer |
| 11 | V00082 | TS-011 | Firefox | Desktop | Registered | Valid | High | Already_Used | Buyer |
| 12 | V00104 | TS-011 | Edge | Mobile | Registered | Valid | Medium | Already_Used | Buyer |
| 13 | V00044 | TS-011 | Chrome | Tablet | Registered | Valid | Medium | Expired | Buyer |
| 14 | V00012 | TS-011 | Firefox | Desktop | Registered | Valid | Low | Valid | Buyer |
| 15 | V00034 | TS-011 | Edge | Tablet | Registered | Valid | High | Valid | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
