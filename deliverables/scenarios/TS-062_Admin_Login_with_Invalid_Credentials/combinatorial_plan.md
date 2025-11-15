# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:30

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 105
- **Covered Pairs:** 105
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Credential_Error | Device | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-062 | Chrome | Wrong_Username | Desktop | Invalid | High | Admin |
| 2 | V00050 | TS-062 | Firefox | Wrong_Password | Mobile | Invalid | Medium | Admin |
| 3 | V00099 | TS-062 | Safari | Both | Tablet | Invalid | Low | Admin |
| 4 | V00033 | TS-062 | Edge | Wrong_Username | Mobile | Invalid | Low | Admin |
| 5 | V00070 | TS-062 | Edge | Wrong_Password | Tablet | Invalid | High | Admin |
| 6 | V00101 | TS-062 | Edge | Both | Desktop | Invalid | Medium | Admin |
| 7 | V00008 | TS-062 | Chrome | Wrong_Username | Tablet | Invalid | Medium | Admin |
| 8 | V00039 | TS-062 | Chrome | Wrong_Password | Desktop | Invalid | Low | Admin |
| 9 | V00076 | TS-062 | Chrome | Both | Mobile | Invalid | High | Admin |
| 10 | V00010 | TS-062 | Firefox | Wrong_Username | Desktop | Invalid | High | Admin |
| 11 | V00019 | TS-062 | Safari | Wrong_Username | Desktop | Invalid | High | Admin |
| 12 | V00059 | TS-062 | Safari | Wrong_Password | Mobile | Invalid | Medium | Admin |
| 13 | V00090 | TS-062 | Firefox | Both | Tablet | Invalid | Low | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
