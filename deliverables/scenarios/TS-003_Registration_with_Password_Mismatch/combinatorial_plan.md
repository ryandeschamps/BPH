# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:42:58

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 105
- **Covered Pairs:** 105
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Input_Validity | Network_Speed | Password_State | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-003 | Chrome | Desktop | Invalid | High | Mismatch_One_Char | Visitor |
| 2 | V00050 | TS-003 | Firefox | Mobile | Invalid | Medium | Mismatch_Multiple_Chars | Visitor |
| 3 | V00099 | TS-003 | Safari | Tablet | Invalid | Low | Empty_Confirm | Visitor |
| 4 | V00033 | TS-003 | Edge | Mobile | Invalid | Low | Mismatch_One_Char | Visitor |
| 5 | V00070 | TS-003 | Edge | Tablet | Invalid | High | Mismatch_Multiple_Chars | Visitor |
| 6 | V00101 | TS-003 | Edge | Desktop | Invalid | Medium | Empty_Confirm | Visitor |
| 7 | V00008 | TS-003 | Chrome | Tablet | Invalid | Medium | Mismatch_One_Char | Visitor |
| 8 | V00039 | TS-003 | Chrome | Desktop | Invalid | Low | Mismatch_Multiple_Chars | Visitor |
| 9 | V00076 | TS-003 | Chrome | Mobile | Invalid | High | Empty_Confirm | Visitor |
| 10 | V00010 | TS-003 | Firefox | Desktop | Invalid | High | Mismatch_One_Char | Visitor |
| 11 | V00019 | TS-003 | Safari | Desktop | Invalid | High | Mismatch_One_Char | Visitor |
| 12 | V00059 | TS-003 | Safari | Mobile | Invalid | Medium | Mismatch_Multiple_Chars | Visitor |
| 13 | V00090 | TS-003 | Firefox | Tablet | Invalid | Low | Empty_Confirm | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
