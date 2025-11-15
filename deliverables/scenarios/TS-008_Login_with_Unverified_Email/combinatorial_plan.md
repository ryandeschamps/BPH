# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:00

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 107
- **Covered Pairs:** 107
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 14

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Account_State | Browser | Device | Email_Verification | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-008 | Unverified | Chrome | Desktop | Not_Clicked | Valid | High | Buyer |
| 2 | V00050 | TS-008 | Unverified | Firefox | Mobile | Link_Expired | Valid | Medium | Buyer |
| 3 | V00027 | TS-008 | Unverified | Safari | Tablet | Not_Clicked | Valid | Low | Buyer |
| 4 | V00066 | TS-008 | Unverified | Edge | Desktop | Link_Expired | Valid | Low | Buyer |
| 5 | V00031 | TS-008 | Unverified | Edge | Mobile | Not_Clicked | Valid | High | Buyer |
| 6 | V00043 | TS-008 | Unverified | Chrome | Tablet | Link_Expired | Valid | High | Buyer |
| 7 | V00011 | TS-008 | Unverified | Firefox | Desktop | Not_Clicked | Valid | Medium | Buyer |
| 8 | V00006 | TS-008 | Unverified | Chrome | Mobile | Not_Clicked | Valid | Low | Buyer |
| 9 | V00035 | TS-008 | Unverified | Edge | Tablet | Not_Clicked | Valid | Medium | Buyer |
| 10 | V00055 | TS-008 | Unverified | Safari | Desktop | Link_Expired | Valid | High | Buyer |
| 11 | V00016 | TS-008 | Unverified | Firefox | Tablet | Not_Clicked | Valid | High | Buyer |
| 12 | V00023 | TS-008 | Unverified | Safari | Mobile | Not_Clicked | Valid | Medium | Buyer |
| 13 | V00002 | TS-008 | Unverified | Chrome | Desktop | Not_Clicked | Valid | Medium | Buyer |
| 14 | V00012 | TS-008 | Unverified | Firefox | Desktop | Not_Clicked | Valid | Low | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
