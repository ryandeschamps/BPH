# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:20

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 154
- **Covered Pairs:** 154
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 15

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Email_Delivery | Network_Speed | Order_Size | Payment_Method | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-041 | Chrome | Desktop | Delivered | High | Single_Item | Credit_Card | Buyer |
| 2 | V00266 | TS-041 | Firefox | Mobile | Delayed | Medium | Multiple_Items | Debit_Card | Buyer |
| 3 | V00351 | TS-041 | Safari | Tablet | Delayed | Low | Single_Item | Net_Banking | Buyer |
| 4 | V00105 | TS-041 | Edge | Mobile | Delivered | Low | Multiple_Items | Credit_Card | Buyer |
| 5 | V00179 | TS-041 | Edge | Tablet | Delivered | Medium | Single_Item | Debit_Card | Buyer |
| 6 | V00424 | TS-041 | Edge | Desktop | Delayed | High | Multiple_Items | Net_Banking | Buyer |
| 7 | V00116 | TS-041 | Chrome | Tablet | Delayed | Medium | Multiple_Items | Credit_Card | Buyer |
| 8 | V00301 | TS-041 | Firefox | Mobile | Delivered | High | Single_Item | Net_Banking | Buyer |
| 9 | V00235 | TS-041 | Safari | Desktop | Delivered | High | Multiple_Items | Debit_Card | Buyer |
| 10 | V00012 | TS-041 | Firefox | Desktop | Delivered | Low | Single_Item | Credit_Card | Buyer |
| 11 | V00150 | TS-041 | Chrome | Mobile | Delivered | Low | Single_Item | Debit_Card | Buyer |
| 12 | V00020 | TS-041 | Safari | Desktop | Delivered | Medium | Single_Item | Credit_Card | Buyer |
| 13 | V00016 | TS-041 | Firefox | Tablet | Delivered | High | Single_Item | Credit_Card | Buyer |
| 14 | V00290 | TS-041 | Chrome | Desktop | Delivered | Medium | Single_Item | Net_Banking | Buyer |
| 15 | V00022 | TS-041 | Safari | Mobile | Delivered | High | Single_Item | Credit_Card | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
