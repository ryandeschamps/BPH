# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:01

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 152
- **Covered Pairs:** 152
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 16

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Auth_Method | Browser | Device | Input_Validity | Network_Speed | OAuth_State | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-010 | Google | Chrome | Desktop | Valid | High | Authorized | Visitor |
| 2 | V00194 | TS-010 | Google | Firefox | Mobile | Invalid | Medium | Denied | Visitor |
| 3 | V00099 | TS-010 | Google | Safari | Tablet | Valid | Low | Already_Linked | Visitor |
| 4 | V00282 | TS-010 | Google | Edge | Desktop | Invalid | Low | New_Account | Visitor |
| 5 | V00032 | TS-010 | Google | Edge | Mobile | Valid | Medium | Authorized | Visitor |
| 6 | V00124 | TS-010 | Google | Firefox | Tablet | Valid | High | New_Account | Visitor |
| 7 | V00220 | TS-010 | Google | Chrome | Mobile | Invalid | High | Already_Linked | Visitor |
| 8 | V00170 | TS-010 | Google | Safari | Tablet | Invalid | Medium | Authorized | Visitor |
| 9 | V00045 | TS-010 | Google | Chrome | Tablet | Valid | Low | Denied | Visitor |
| 10 | V00055 | TS-010 | Google | Safari | Desktop | Valid | High | Denied | Visitor |
| 11 | V00083 | TS-010 | Google | Firefox | Desktop | Valid | Medium | Already_Linked | Visitor |
| 12 | V00015 | TS-010 | Google | Firefox | Mobile | Valid | Low | Authorized | Visitor |
| 13 | V00113 | TS-010 | Google | Chrome | Mobile | Valid | Medium | New_Account | Visitor |
| 14 | V00070 | TS-010 | Google | Edge | Tablet | Valid | High | Denied | Visitor |
| 15 | V00130 | TS-010 | Google | Safari | Mobile | Valid | High | New_Account | Visitor |
| 16 | V00100 | TS-010 | Google | Edge | Desktop | Valid | High | Already_Linked | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
