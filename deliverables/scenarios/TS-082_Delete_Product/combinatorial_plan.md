# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:39

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 92
- **Covered Pairs:** 92
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 14

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Has_Orders | Network_Speed | Product_Status | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-082 | Chrome | Desktop | Yes | High | Any | Admin |
| 2 | V00050 | TS-082 | Firefox | Mobile | No | Medium | Any | Admin |
| 3 | V00027 | TS-082 | Safari | Tablet | Yes | Low | Any | Admin |
| 4 | V00066 | TS-082 | Edge | Desktop | No | Low | Any | Admin |
| 5 | V00031 | TS-082 | Edge | Mobile | Yes | High | Any | Admin |
| 6 | V00043 | TS-082 | Chrome | Tablet | No | High | Any | Admin |
| 7 | V00011 | TS-082 | Firefox | Desktop | Yes | Medium | Any | Admin |
| 8 | V00006 | TS-082 | Chrome | Mobile | Yes | Low | Any | Admin |
| 9 | V00035 | TS-082 | Edge | Tablet | Yes | Medium | Any | Admin |
| 10 | V00055 | TS-082 | Safari | Desktop | No | High | Any | Admin |
| 11 | V00016 | TS-082 | Firefox | Tablet | Yes | High | Any | Admin |
| 12 | V00023 | TS-082 | Safari | Mobile | Yes | Medium | Any | Admin |
| 13 | V00002 | TS-082 | Chrome | Desktop | Yes | Medium | Any | Admin |
| 14 | V00012 | TS-082 | Firefox | Desktop | Yes | Low | Any | Admin |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
