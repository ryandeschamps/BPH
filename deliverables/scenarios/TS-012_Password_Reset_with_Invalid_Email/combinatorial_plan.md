# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:02

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 92
- **Covered Pairs:** 92
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 14

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Email_State | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-012 | Chrome | Desktop | Not_Registered | Invalid | High | Visitor |
| 2 | V00050 | TS-012 | Firefox | Mobile | Invalid_Format | Invalid | Medium | Visitor |
| 3 | V00027 | TS-012 | Safari | Tablet | Not_Registered | Invalid | Low | Visitor |
| 4 | V00066 | TS-012 | Edge | Desktop | Invalid_Format | Invalid | Low | Visitor |
| 5 | V00031 | TS-012 | Edge | Mobile | Not_Registered | Invalid | High | Visitor |
| 6 | V00043 | TS-012 | Chrome | Tablet | Invalid_Format | Invalid | High | Visitor |
| 7 | V00011 | TS-012 | Firefox | Desktop | Not_Registered | Invalid | Medium | Visitor |
| 8 | V00006 | TS-012 | Chrome | Mobile | Not_Registered | Invalid | Low | Visitor |
| 9 | V00035 | TS-012 | Edge | Tablet | Not_Registered | Invalid | Medium | Visitor |
| 10 | V00055 | TS-012 | Safari | Desktop | Invalid_Format | Invalid | High | Visitor |
| 11 | V00016 | TS-012 | Firefox | Tablet | Not_Registered | Invalid | High | Visitor |
| 12 | V00023 | TS-012 | Safari | Mobile | Not_Registered | Invalid | Medium | Visitor |
| 13 | V00002 | TS-012 | Chrome | Desktop | Not_Registered | Invalid | Medium | Visitor |
| 14 | V00012 | TS-012 | Firefox | Desktop | Not_Registered | Invalid | Low | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
