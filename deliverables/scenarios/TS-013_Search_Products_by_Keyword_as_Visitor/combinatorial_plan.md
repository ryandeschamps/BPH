# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:43:03

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 188
- **Covered Pairs:** 188
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 18

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Input_Validity | Network_Speed | Results_Count | Search_Query | User_Type |
|-----------|------------|---|---|---|---|---|---|---|---|
| 1 | V00001 | TS-013 | Chrome | Desktop | Valid | High | Many_Results | Single_Keyword | Visitor |
| 2 | V00590 | TS-013 | Firefox | Mobile | Valid | Medium | Few_Results | Multiple_Keywords | Buyer |
| 3 | V00315 | TS-013 | Safari | Tablet | Valid | Low | One_Result | Partial_Match | Visitor |
| 4 | V00786 | TS-013 | Edge | Desktop | Valid | Low | Many_Results | Exact_Match | Buyer |
| 5 | V00071 | TS-013 | Edge | Tablet | Valid | Medium | Few_Results | Single_Keyword | Visitor |
| 6 | V00409 | TS-013 | Firefox | Mobile | Valid | High | One_Result | Exact_Match | Visitor |
| 7 | V00565 | TS-013 | Safari | Tablet | Valid | High | Many_Results | Multiple_Keywords | Buyer |
| 8 | V00722 | TS-013 | Chrome | Desktop | Valid | Medium | One_Result | Partial_Match | Buyer |
| 9 | V00147 | TS-013 | Chrome | Desktop | Valid | Low | Few_Results | Multiple_Keywords | Visitor |
| 10 | V00447 | TS-013 | Firefox | Mobile | Valid | Low | Many_Results | Single_Keyword | Buyer |
| 11 | V00283 | TS-013 | Edge | Mobile | Valid | High | Few_Results | Partial_Match | Visitor |
| 12 | V00380 | TS-013 | Safari | Desktop | Valid | Medium | Few_Results | Exact_Match | Visitor |
| 13 | V00227 | TS-013 | Firefox | Desktop | Valid | Medium | Many_Results | Partial_Match | Visitor |
| 14 | V00094 | TS-013 | Safari | Mobile | Valid | High | One_Result | Single_Keyword | Visitor |
| 15 | V00208 | TS-013 | Edge | Desktop | Valid | High | One_Result | Multiple_Keywords | Visitor |
| 16 | V00331 | TS-013 | Chrome | Tablet | Valid | High | Many_Results | Exact_Match | Visitor |
| 17 | V00004 | TS-013 | Chrome | Mobile | Valid | High | Many_Results | Single_Keyword | Visitor |
| 18 | V00016 | TS-013 | Firefox | Tablet | Valid | High | Many_Results | Single_Keyword | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
