# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:11

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Network_Speed | Redirect_Action | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-024 | Chrome | Desktop | High | Login | Visitor |
| 2 | V00050 | TS-024 | Firefox | Mobile | Medium | Register | Visitor |
| 3 | V00099 | TS-024 | Safari | Tablet | Low | Cancel | Visitor |
| 4 | V00033 | TS-024 | Edge | Mobile | Low | Login | Visitor |
| 5 | V00070 | TS-024 | Edge | Tablet | High | Register | Visitor |
| 6 | V00101 | TS-024 | Edge | Desktop | Medium | Cancel | Visitor |
| 7 | V00008 | TS-024 | Chrome | Tablet | Medium | Login | Visitor |
| 8 | V00039 | TS-024 | Chrome | Desktop | Low | Register | Visitor |
| 9 | V00076 | TS-024 | Chrome | Mobile | High | Cancel | Visitor |
| 10 | V00010 | TS-024 | Firefox | Desktop | High | Login | Visitor |
| 11 | V00019 | TS-024 | Safari | Desktop | High | Login | Visitor |
| 12 | V00059 | TS-024 | Safari | Mobile | Medium | Register | Visitor |
| 13 | V00090 | TS-024 | Firefox | Tablet | Low | Cancel | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
