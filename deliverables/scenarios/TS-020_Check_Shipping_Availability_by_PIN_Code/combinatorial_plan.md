# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:08

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 136
- **Covered Pairs:** 136
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Input_Validity | Network_Speed | PIN_Code_State | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-020 | Chrome | Desktop | Valid | High | Available | Visitor |
| 2 | V00374 | TS-020 | Firefox | Mobile | Invalid | Medium | Not_Available | Buyer |
| 3 | V00207 | TS-020 | Safari | Tablet | Invalid | Low | Invalid_Format | Visitor |
| 4 | V00249 | TS-020 | Edge | Mobile | Valid | Low | Available | Buyer |
| 5 | V00071 | TS-020 | Edge | Tablet | Valid | Medium | Not_Available | Visitor |
| 6 | V00424 | TS-020 | Edge | Desktop | Invalid | High | Invalid_Format | Buyer |
| 7 | V00085 | TS-020 | Firefox | Mobile | Valid | High | Invalid_Format | Visitor |
| 8 | V00332 | TS-020 | Chrome | Tablet | Invalid | Medium | Available | Buyer |
| 9 | V00271 | TS-020 | Safari | Desktop | Valid | High | Not_Available | Buyer |
| 10 | V00012 | TS-020 | Firefox | Desktop | Valid | Low | Available | Visitor |
| 11 | V00042 | TS-020 | Chrome | Mobile | Valid | Low | Not_Available | Visitor |
| 12 | V00020 | TS-020 | Safari | Desktop | Valid | Medium | Available | Visitor |
| 13 | V00016 | TS-020 | Firefox | Tablet | Valid | High | Available | Visitor |
| 14 | V00074 | TS-020 | Chrome | Desktop | Valid | Medium | Invalid_Format | Visitor |
| 15 | V00022 | TS-020 | Safari | Mobile | Valid | High | Available | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
