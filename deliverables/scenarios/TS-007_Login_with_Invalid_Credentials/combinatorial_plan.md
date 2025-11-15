# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:00

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 131
- **Covered Pairs:** 131
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 21

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Credential_Error | Device | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-007 | Chrome | Wrong_Email | Desktop | Invalid | High | Visitor |
| 2 | V00050 | TS-007 | Firefox | Wrong_Password | Mobile | Invalid | Medium | Visitor |
| 3 | V00099 | TS-007 | Safari | Both_Wrong | Tablet | Invalid | Low | Visitor |
| 4 | V00137 | TS-007 | Edge | Empty_Email | Desktop | Invalid | Medium | Visitor |
| 5 | V00150 | TS-007 | Chrome | Empty_Password | Mobile | Invalid | Low | Visitor |
| 6 | V00070 | TS-007 | Edge | Wrong_Password | Tablet | Invalid | High | Visitor |
| 7 | V00130 | TS-007 | Safari | Empty_Email | Mobile | Invalid | High | Visitor |
| 8 | V00008 | TS-007 | Chrome | Wrong_Email | Tablet | Invalid | Medium | Visitor |
| 9 | V00012 | TS-007 | Firefox | Wrong_Email | Desktop | Invalid | Low | Visitor |
| 10 | V00160 | TS-007 | Firefox | Empty_Password | Tablet | Invalid | High | Visitor |
| 11 | V00164 | TS-007 | Safari | Empty_Password | Desktop | Invalid | Medium | Visitor |
| 12 | V00033 | TS-007 | Edge | Wrong_Email | Mobile | Invalid | Low | Visitor |
| 13 | V00039 | TS-007 | Chrome | Wrong_Password | Desktop | Invalid | Low | Visitor |
| 14 | V00073 | TS-007 | Chrome | Both_Wrong | Desktop | Invalid | High | Visitor |
| 15 | V00086 | TS-007 | Firefox | Both_Wrong | Mobile | Invalid | Medium | Visitor |
| 16 | V00117 | TS-007 | Chrome | Empty_Email | Tablet | Invalid | Low | Visitor |
| 17 | V00019 | TS-007 | Safari | Wrong_Email | Desktop | Invalid | High | Visitor |
| 18 | V00055 | TS-007 | Safari | Wrong_Password | Desktop | Invalid | High | Visitor |
| 19 | V00100 | TS-007 | Edge | Both_Wrong | Desktop | Invalid | High | Visitor |
| 20 | V00118 | TS-007 | Firefox | Empty_Email | Desktop | Invalid | High | Visitor |
| 21 | V00172 | TS-007 | Edge | Empty_Password | Desktop | Invalid | High | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
