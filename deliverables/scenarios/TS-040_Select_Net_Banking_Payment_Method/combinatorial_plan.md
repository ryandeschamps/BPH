# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:19

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 169
- **Covered Pairs:** 169
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 19

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Bank | Browser | Device | Network_Speed | Payment_Method | Payment_Status | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-040 | Chase | Chrome | Desktop | High | Net_Banking | Success | Buyer |
| 2 | V00158 | TS-040 | BofA | Firefox | Mobile | Medium | Net_Banking | Failed | Buyer |
| 3 | V00315 | TS-040 | Wells_Fargo | Safari | Tablet | Low | Net_Banking | Timeout | Buyer |
| 4 | V00357 | TS-040 | Citi | Edge | Mobile | Low | Net_Banking | Success | Buyer |
| 5 | V00070 | TS-040 | Chase | Edge | Tablet | High | Net_Banking | Failed | Buyer |
| 6 | V00209 | TS-040 | BofA | Edge | Desktop | Medium | Net_Banking | Timeout | Buyer |
| 7 | V00085 | TS-040 | Chase | Firefox | Mobile | High | Net_Banking | Timeout | Buyer |
| 8 | V00116 | TS-040 | BofA | Chrome | Tablet | Medium | Net_Banking | Success | Buyer |
| 9 | V00255 | TS-040 | Wells_Fargo | Chrome | Desktop | Low | Net_Banking | Failed | Buyer |
| 10 | V00379 | TS-040 | Citi | Safari | Desktop | High | Net_Banking | Failed | Buyer |
| 11 | V00239 | TS-040 | Wells_Fargo | Safari | Mobile | Medium | Net_Banking | Success | Buyer |
| 12 | V00341 | TS-040 | Citi | Firefox | Tablet | Medium | Net_Banking | Success | Buyer |
| 13 | V00400 | TS-040 | Citi | Chrome | Mobile | High | Net_Banking | Timeout | Buyer |
| 14 | V00012 | TS-040 | Chase | Firefox | Desktop | Low | Net_Banking | Success | Buyer |
| 15 | V00020 | TS-040 | Chase | Safari | Desktop | Medium | Net_Banking | Success | Buyer |
| 16 | V00127 | TS-040 | BofA | Safari | Desktop | High | Net_Banking | Success | Buyer |
| 17 | V00226 | TS-040 | Wells_Fargo | Firefox | Desktop | High | Net_Banking | Success | Buyer |
| 18 | V00111 | TS-040 | BofA | Chrome | Desktop | Low | Net_Banking | Success | Buyer |
| 19 | V00244 | TS-040 | Wells_Fargo | Edge | Desktop | High | Net_Banking | Success | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
