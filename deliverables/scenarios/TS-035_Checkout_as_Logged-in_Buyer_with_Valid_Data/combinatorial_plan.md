# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:16

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 173
- **Covered Pairs:** 173
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Address_State | Browser | Cart_Items | Device | Input_Validity | Network_Speed | Payment_Method | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-035 | New_Address | Chrome | Single | Desktop | Valid | High | Credit_Card | Buyer |
| 2 | V00266 | TS-035 | Saved_Address | Firefox | Multiple | Mobile | Valid | Medium | Debit_Card | Buyer |
| 3 | V00351 | TS-035 | New_Address | Safari | Multiple | Tablet | Valid | Low | Net_Banking | Buyer |
| 4 | V00105 | TS-035 | Saved_Address | Edge | Single | Mobile | Valid | Low | Credit_Card | Buyer |
| 5 | V00179 | TS-035 | New_Address | Edge | Single | Tablet | Valid | Medium | Debit_Card | Buyer |
| 6 | V00424 | TS-035 | Saved_Address | Edge | Multiple | Desktop | Valid | High | Net_Banking | Buyer |
| 7 | V00116 | TS-035 | Saved_Address | Chrome | Multiple | Tablet | Valid | Medium | Credit_Card | Buyer |
| 8 | V00301 | TS-035 | New_Address | Firefox | Single | Mobile | Valid | High | Net_Banking | Buyer |
| 9 | V00235 | TS-035 | Saved_Address | Safari | Single | Desktop | Valid | High | Debit_Card | Buyer |
| 10 | V00012 | TS-035 | New_Address | Firefox | Single | Desktop | Valid | Low | Credit_Card | Buyer |
| 11 | V00150 | TS-035 | New_Address | Chrome | Single | Mobile | Valid | Low | Debit_Card | Buyer |
| 12 | V00020 | TS-035 | New_Address | Safari | Single | Desktop | Valid | Medium | Credit_Card | Buyer |
| 13 | V00016 | TS-035 | New_Address | Firefox | Single | Tablet | Valid | High | Credit_Card | Buyer |
| 14 | V00290 | TS-035 | New_Address | Chrome | Single | Desktop | Valid | Medium | Net_Banking | Buyer |
| 15 | V00022 | TS-035 | New_Address | Safari | Single | Mobile | Valid | High | Credit_Card | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
