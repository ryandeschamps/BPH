# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:21

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 225
- **Covered Pairs:** 225
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 23

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Failure_Reason | Network_Speed | Payment_Method | Retry_Action | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-042 | Chrome | Desktop | Insufficient_Funds | High | Credit_Card | Retry_Same_Method | Buyer |
| 2 | V00698 | TS-042 | Firefox | Mobile | Invalid_Card | Medium | Debit_Card | Change_Method | Buyer |
| 3 | V01395 | TS-042 | Safari | Tablet | Declined | Low | Net_Banking | Cancel | Buyer |
| 4 | V00357 | TS-042 | Edge | Mobile | Timeout | Low | Credit_Card | Retry_Same_Method | Buyer |
| 5 | V01042 | TS-042 | Edge | Tablet | Network_Error | High | Debit_Card | Change_Method | Buyer |
| 6 | V00515 | TS-042 | Firefox | Desktop | Network_Error | Medium | Credit_Card | Cancel | Buyer |
| 7 | V00597 | TS-042 | Safari | Desktop | Insufficient_Funds | Low | Debit_Card | Change_Method | Buyer |
| 8 | V01097 | TS-042 | Firefox | Tablet | Insufficient_Funds | Medium | Net_Banking | Retry_Same_Method | Buyer |
| 9 | V01264 | TS-042 | Chrome | Mobile | Invalid_Card | High | Net_Banking | Cancel | Buyer |
| 10 | V00260 | TS-042 | Chrome | Tablet | Declined | Medium | Credit_Card | Change_Method | Buyer |
| 11 | V01469 | TS-042 | Edge | Desktop | Timeout | Medium | Net_Banking | Change_Method | Buyer |
| 12 | V00778 | TS-042 | Safari | Mobile | Declined | High | Debit_Card | Retry_Same_Method | Buyer |
| 13 | V00943 | TS-042 | Chrome | Tablet | Timeout | High | Debit_Card | Cancel | Buyer |
| 14 | V00128 | TS-042 | Safari | Desktop | Invalid_Card | Medium | Credit_Card | Retry_Same_Method | Buyer |
| 15 | V01518 | TS-042 | Chrome | Mobile | Network_Error | Low | Net_Banking | Retry_Same_Method | Buyer |
| 16 | V00103 | TS-042 | Edge | Mobile | Insufficient_Funds | High | Credit_Card | Cancel | Buyer |
| 17 | V00126 | TS-042 | Firefox | Tablet | Invalid_Card | Low | Credit_Card | Retry_Same_Method | Buyer |
| 18 | V00226 | TS-042 | Firefox | Desktop | Declined | High | Credit_Card | Retry_Same_Method | Buyer |
| 19 | V00136 | TS-042 | Edge | Desktop | Invalid_Card | High | Credit_Card | Retry_Same_Method | Buyer |
| 20 | V00244 | TS-042 | Edge | Desktop | Declined | High | Credit_Card | Retry_Same_Method | Buyer |
| 21 | V00334 | TS-042 | Firefox | Desktop | Timeout | High | Credit_Card | Retry_Same_Method | Buyer |
| 22 | V00343 | TS-042 | Safari | Desktop | Timeout | High | Credit_Card | Retry_Same_Method | Buyer |
| 23 | V00451 | TS-042 | Safari | Desktop | Network_Error | High | Credit_Card | Retry_Same_Method | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
