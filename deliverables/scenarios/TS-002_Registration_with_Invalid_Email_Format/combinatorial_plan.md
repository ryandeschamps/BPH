# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:42:58

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 118
- **Covered Pairs:** 118
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 17

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Email_Format | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-002 | Chrome | Desktop | Missing_At | Invalid | High | Visitor |
| 2 | V00050 | TS-002 | Firefox | Mobile | Invalid_Domain | Invalid | Medium | Visitor |
| 3 | V00099 | TS-002 | Safari | Tablet | Special_Chars | Invalid | Low | Visitor |
| 4 | V00137 | TS-002 | Edge | Desktop | No_Domain | Invalid | Medium | Visitor |
| 5 | V00033 | TS-002 | Edge | Mobile | Missing_At | Invalid | Low | Visitor |
| 6 | V00070 | TS-002 | Edge | Tablet | Invalid_Domain | Invalid | High | Visitor |
| 7 | V00130 | TS-002 | Safari | Mobile | No_Domain | Invalid | High | Visitor |
| 8 | V00008 | TS-002 | Chrome | Tablet | Missing_At | Invalid | Medium | Visitor |
| 9 | V00039 | TS-002 | Chrome | Desktop | Invalid_Domain | Invalid | Low | Visitor |
| 10 | V00082 | TS-002 | Firefox | Desktop | Special_Chars | Invalid | High | Visitor |
| 11 | V00126 | TS-002 | Firefox | Tablet | No_Domain | Invalid | Low | Visitor |
| 12 | V00077 | TS-002 | Chrome | Mobile | Special_Chars | Invalid | Medium | Visitor |
| 13 | V00020 | TS-002 | Safari | Desktop | Missing_At | Invalid | Medium | Visitor |
| 14 | V00010 | TS-002 | Firefox | Desktop | Missing_At | Invalid | High | Visitor |
| 15 | V00055 | TS-002 | Safari | Desktop | Invalid_Domain | Invalid | High | Visitor |
| 16 | V00100 | TS-002 | Edge | Desktop | Special_Chars | Invalid | High | Visitor |
| 17 | V00109 | TS-002 | Chrome | Desktop | No_Domain | Invalid | High | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
