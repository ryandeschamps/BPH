# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:17

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 137
- **Covered Pairs:** 137
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Address_State | Address_Type | Browser | Device | Network_Speed | Payment_Method | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-037 | New | Same_Address | Chrome | Desktop | High | Credit_Card | Buyer |
| 2 | V00158 | TS-037 | Saved | Same_Address | Firefox | Mobile | Medium | Debit_Card | Buyer |
| 3 | V00099 | TS-037 | New | Same_Address | Safari | Tablet | Low | Net_Banking | Buyer |
| 4 | V00138 | TS-037 | Saved | Same_Address | Edge | Desktop | Low | Credit_Card | Buyer |
| 5 | V00067 | TS-037 | New | Same_Address | Edge | Mobile | High | Debit_Card | Buyer |
| 6 | V00187 | TS-037 | Saved | Same_Address | Chrome | Tablet | High | Net_Banking | Buyer |
| 7 | V00017 | TS-037 | New | Same_Address | Firefox | Tablet | Medium | Credit_Card | Buyer |
| 8 | V00164 | TS-037 | Saved | Same_Address | Safari | Desktop | Medium | Debit_Card | Buyer |
| 9 | V00042 | TS-037 | New | Same_Address | Chrome | Mobile | Low | Debit_Card | Buyer |
| 10 | V00022 | TS-037 | New | Same_Address | Safari | Mobile | High | Credit_Card | Buyer |
| 11 | V00082 | TS-037 | New | Same_Address | Firefox | Desktop | High | Net_Banking | Buyer |
| 12 | V00104 | TS-037 | New | Same_Address | Edge | Mobile | Medium | Net_Banking | Buyer |
| 13 | V00044 | TS-037 | New | Same_Address | Chrome | Tablet | Medium | Debit_Card | Buyer |
| 14 | V00012 | TS-037 | New | Same_Address | Firefox | Desktop | Low | Credit_Card | Buyer |
| 15 | V00034 | TS-037 | New | Same_Address | Edge | Tablet | High | Credit_Card | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
