# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:23

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 150
- **Covered Pairs:** 150
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 19

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Email_Delivery | Network_Speed | Order_Status | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-044 | Chrome | Desktop | Immediate | High | Confirmed | Buyer |
| 2 | V00158 | TS-044 | Firefox | Mobile | Delayed | Medium | In_Process | Buyer |
| 3 | V00315 | TS-044 | Safari | Tablet | Failed | Low | Shipped | Buyer |
| 4 | V00357 | TS-044 | Edge | Mobile | Immediate | Low | Delivered | Buyer |
| 5 | V00070 | TS-044 | Edge | Tablet | Delayed | High | Confirmed | Buyer |
| 6 | V00209 | TS-044 | Edge | Desktop | Failed | Medium | In_Process | Buyer |
| 7 | V00085 | TS-044 | Firefox | Mobile | Failed | High | Confirmed | Buyer |
| 8 | V00116 | TS-044 | Chrome | Tablet | Immediate | Medium | In_Process | Buyer |
| 9 | V00255 | TS-044 | Chrome | Desktop | Delayed | Low | Shipped | Buyer |
| 10 | V00379 | TS-044 | Safari | Desktop | Delayed | High | Delivered | Buyer |
| 11 | V00239 | TS-044 | Safari | Mobile | Immediate | Medium | Shipped | Buyer |
| 12 | V00341 | TS-044 | Firefox | Tablet | Immediate | Medium | Delivered | Buyer |
| 13 | V00400 | TS-044 | Chrome | Mobile | Failed | High | Delivered | Buyer |
| 14 | V00012 | TS-044 | Firefox | Desktop | Immediate | Low | Confirmed | Buyer |
| 15 | V00020 | TS-044 | Safari | Desktop | Immediate | Medium | Confirmed | Buyer |
| 16 | V00127 | TS-044 | Safari | Desktop | Immediate | High | In_Process | Buyer |
| 17 | V00226 | TS-044 | Firefox | Desktop | Immediate | High | Shipped | Buyer |
| 18 | V00111 | TS-044 | Chrome | Desktop | Immediate | Low | In_Process | Buyer |
| 19 | V00244 | TS-044 | Edge | Desktop | Immediate | High | Shipped | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
