# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:22

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 171
- **Covered Pairs:** 171
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 17

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_Items | Device | Network_Speed | Shipping_Cost | Tax_Applicable | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-043 | Chrome | Single | Desktop | High | Standard | Yes | Buyer |
| 2 | V00338 | TS-043 | Firefox | Multiple | Mobile | Medium | Express | No | Buyer |
| 3 | V00603 | TS-043 | Safari | Mixed_Prices | Tablet | Low | Free | Yes | Buyer |
| 4 | V00069 | TS-043 | Edge | Single | Mobile | Low | Standard | No | Buyer |
| 5 | V00322 | TS-043 | Edge | Multiple | Tablet | High | Express | Yes | Buyer |
| 6 | V00614 | TS-043 | Chrome | Mixed_Prices | Desktop | Medium | Free | No | Buyer |
| 7 | V00017 | TS-043 | Firefox | Single | Tablet | Medium | Standard | Yes | Buyer |
| 8 | V00202 | TS-043 | Safari | Single | Mobile | High | Free | No | Buyer |
| 9 | V00291 | TS-043 | Chrome | Multiple | Desktop | Low | Express | Yes | Buyer |
| 10 | V00445 | TS-043 | Firefox | Mixed_Prices | Mobile | High | Standard | Yes | Buyer |
| 11 | V00236 | TS-043 | Safari | Multiple | Desktop | Medium | Standard | Yes | Buyer |
| 12 | V00372 | TS-043 | Firefox | Multiple | Desktop | Low | Free | Yes | Buyer |
| 13 | V00533 | TS-043 | Edge | Mixed_Prices | Desktop | Medium | Express | Yes | Buyer |
| 14 | V00115 | TS-043 | Chrome | Single | Tablet | High | Express | No | Buyer |
| 15 | V00004 | TS-043 | Chrome | Single | Mobile | High | Standard | Yes | Buyer |
| 16 | V00091 | TS-043 | Safari | Single | Desktop | High | Express | Yes | Buyer |
| 17 | V00172 | TS-043 | Edge | Single | Desktop | High | Free | Yes | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
