# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:13

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 90
- **Covered Pairs:** 90
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 13

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Cart_State | Device | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|
| 1 | V00001 | TS-029 | Chrome | Never_Had_Items | Desktop | High | Buyer |
| 2 | V00050 | TS-029 | Firefox | Previously_Had_Items | Mobile | Medium | Buyer |
| 3 | V00099 | TS-029 | Safari | Items_Removed | Tablet | Low | Buyer |
| 4 | V00033 | TS-029 | Edge | Never_Had_Items | Mobile | Low | Buyer |
| 5 | V00070 | TS-029 | Edge | Previously_Had_Items | Tablet | High | Buyer |
| 6 | V00101 | TS-029 | Edge | Items_Removed | Desktop | Medium | Buyer |
| 7 | V00008 | TS-029 | Chrome | Never_Had_Items | Tablet | Medium | Buyer |
| 8 | V00039 | TS-029 | Chrome | Previously_Had_Items | Desktop | Low | Buyer |
| 9 | V00076 | TS-029 | Chrome | Items_Removed | Mobile | High | Buyer |
| 10 | V00010 | TS-029 | Firefox | Never_Had_Items | Desktop | High | Buyer |
| 11 | V00019 | TS-029 | Safari | Never_Had_Items | Desktop | High | Buyer |
| 12 | V00059 | TS-029 | Safari | Previously_Had_Items | Mobile | Medium | Buyer |
| 13 | V00090 | TS-029 | Firefox | Items_Removed | Tablet | Low | Buyer |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
