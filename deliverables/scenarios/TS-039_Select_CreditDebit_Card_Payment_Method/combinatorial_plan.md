# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:19

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 188
- **Covered Pairs:** 188
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 18

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Card_Type | Device | Network_Speed | Payment_Method | Payment_Status | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-039 | Chrome | Visa | Desktop | High | Credit_Card | Success | Buyer |
| 2 | V00590 | TS-039 | Firefox | Mastercard | Mobile | Medium | Debit_Card | Declined | Buyer |
| 3 | V00315 | TS-039 | Safari | Amex | Tablet | Low | Credit_Card | Timeout | Buyer |
| 4 | V00786 | TS-039 | Edge | Discover | Desktop | Low | Debit_Card | Success | Buyer |
| 5 | V00071 | TS-039 | Edge | Visa | Tablet | Medium | Credit_Card | Declined | Buyer |
| 6 | V00409 | TS-039 | Firefox | Discover | Mobile | High | Credit_Card | Timeout | Buyer |
| 7 | V00565 | TS-039 | Safari | Mastercard | Tablet | High | Debit_Card | Success | Buyer |
| 8 | V00722 | TS-039 | Chrome | Amex | Desktop | Medium | Debit_Card | Timeout | Buyer |
| 9 | V00147 | TS-039 | Chrome | Mastercard | Desktop | Low | Credit_Card | Declined | Buyer |
| 10 | V00447 | TS-039 | Firefox | Visa | Mobile | Low | Debit_Card | Success | Buyer |
| 11 | V00283 | TS-039 | Edge | Amex | Mobile | High | Credit_Card | Declined | Buyer |
| 12 | V00380 | TS-039 | Safari | Discover | Desktop | Medium | Credit_Card | Declined | Buyer |
| 13 | V00227 | TS-039 | Firefox | Amex | Desktop | Medium | Credit_Card | Success | Buyer |
| 14 | V00094 | TS-039 | Safari | Visa | Mobile | High | Credit_Card | Timeout | Buyer |
| 15 | V00208 | TS-039 | Edge | Mastercard | Desktop | High | Credit_Card | Timeout | Buyer |
| 16 | V00331 | TS-039 | Chrome | Discover | Tablet | High | Credit_Card | Success | Buyer |
| 17 | V00004 | TS-039 | Chrome | Visa | Mobile | High | Credit_Card | Success | Buyer |
| 18 | V00016 | TS-039 | Firefox | Visa | Tablet | High | Credit_Card | Success | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
