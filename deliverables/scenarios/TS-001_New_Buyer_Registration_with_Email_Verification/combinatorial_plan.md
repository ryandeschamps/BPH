# Combinatorial Test Execution Plan (Pairwise)

**Generated:** 2025-11-15 19:42:57

**Mode:** Variant Selection

## Coverage Statistics

- **Total Parameter Pairs:** 246
- **Covered Pairs:** 246
- **Coverage Percentage:** 100.00%
- **Test Cases Generated:** 48

## About This Plan

This plan selects an optimal subset of predefined variants to achieve maximum pairwise coverage. The selection ensures that all critical parameter interactions are tested while minimizing redundant test executions.

## Test Cases

| Test Case | Variant ID | Scenario_ID | Browser | Device | Field_Values | Input_Validity | Network_Speed | User_Type |
|-----------|------------|---|---|---|---|---|---|---|
| 1 | V00001 | TS-001 | Chrome | Desktop | All_Valid | Valid | High | Visitor |
| 2 | V00482 | TS-001 | Firefox | Mobile | Missing_FirstName | Invalid | Medium | Visitor |
| 3 | V00099 | TS-001 | Safari | Tablet | Missing_LastName | Valid | Low | Visitor |
| 4 | V00570 | TS-001 | Edge | Desktop | Missing_Email | Invalid | Low | Visitor |
| 5 | V00175 | TS-001 | Edge | Mobile | Invalid_Email | Valid | High | Visitor |
| 6 | V00619 | TS-001 | Chrome | Tablet | Missing_Contact | Invalid | High | Visitor |
| 7 | V00227 | TS-001 | Firefox | Desktop | Invalid_Contact | Valid | Medium | Visitor |
| 8 | V00258 | TS-001 | Chrome | Mobile | Missing_Password | Valid | Low | Visitor |
| 9 | V00323 | TS-001 | Edge | Tablet | Weak_Password | Valid | Medium | Visitor |
| 10 | V00775 | TS-001 | Safari | Desktop | Password_Mismatch | Invalid | High | Visitor |
| 11 | V00376 | TS-001 | Firefox | Tablet | Terms_Not_Accepted | Valid | High | Visitor |
| 12 | V00419 | TS-001 | Safari | Mobile | Duplicate_Email | Valid | Medium | Visitor |
| 13 | V00113 | TS-001 | Chrome | Mobile | Missing_Email | Valid | Medium | Visitor |
| 14 | V00192 | TS-001 | Firefox | Desktop | Missing_Contact | Valid | Low | Visitor |
| 15 | V00037 | TS-001 | Chrome | Desktop | Missing_FirstName | Valid | High | Visitor |
| 16 | V00329 | TS-001 | Chrome | Mobile | Password_Mismatch | Valid | Medium | Visitor |
| 17 | V00446 | TS-001 | Firefox | Mobile | All_Valid | Invalid | Medium | Visitor |
| 18 | V00505 | TS-001 | Chrome | Desktop | Missing_LastName | Invalid | High | Visitor |
| 19 | V00578 | TS-001 | Chrome | Desktop | Invalid_Email | Invalid | Medium | Visitor |
| 20 | V00652 | TS-001 | Chrome | Mobile | Invalid_Contact | Invalid | High | Visitor |
| 21 | V00694 | TS-001 | Firefox | Desktop | Missing_Password | Invalid | High | Visitor |
| 22 | V00721 | TS-001 | Chrome | Desktop | Weak_Password | Invalid | High | Visitor |
| 23 | V00794 | TS-001 | Chrome | Desktop | Terms_Not_Accepted | Invalid | Medium | Visitor |
| 24 | V00829 | TS-001 | Chrome | Desktop | Duplicate_Email | Invalid | High | Visitor |
| 25 | V00027 | TS-001 | Safari | Tablet | All_Valid | Valid | Low | Visitor |
| 26 | V00063 | TS-001 | Safari | Tablet | Missing_FirstName | Valid | Low | Visitor |
| 27 | V00086 | TS-001 | Firefox | Mobile | Missing_LastName | Valid | Medium | Visitor |
| 28 | V00124 | TS-001 | Firefox | Tablet | Missing_Email | Valid | High | Visitor |
| 29 | V00162 | TS-001 | Firefox | Tablet | Invalid_Email | Valid | Low | Visitor |
| 30 | V00203 | TS-001 | Safari | Mobile | Missing_Contact | Valid | Medium | Visitor |
| 31 | V00243 | TS-001 | Safari | Tablet | Invalid_Contact | Valid | Low | Visitor |
| 32 | V00278 | TS-001 | Safari | Tablet | Missing_Password | Valid | Medium | Visitor |
| 33 | V00303 | TS-001 | Firefox | Mobile | Weak_Password | Valid | Low | Visitor |
| 34 | V00342 | TS-001 | Firefox | Tablet | Password_Mismatch | Valid | Low | Visitor |
| 35 | V00384 | TS-001 | Safari | Mobile | Terms_Not_Accepted | Valid | Low | Visitor |
| 36 | V00414 | TS-001 | Firefox | Tablet | Duplicate_Email | Valid | Low | Visitor |
| 37 | V00028 | TS-001 | Edge | Desktop | All_Valid | Valid | High | Visitor |
| 38 | V00064 | TS-001 | Edge | Desktop | Missing_FirstName | Valid | High | Visitor |
| 39 | V00100 | TS-001 | Edge | Desktop | Missing_LastName | Valid | High | Visitor |
| 40 | V00127 | TS-001 | Safari | Desktop | Missing_Email | Valid | High | Visitor |
| 41 | V00163 | TS-001 | Safari | Desktop | Invalid_Email | Valid | High | Visitor |
| 42 | V00208 | TS-001 | Edge | Desktop | Missing_Contact | Valid | High | Visitor |
| 43 | V00244 | TS-001 | Edge | Desktop | Invalid_Contact | Valid | High | Visitor |
| 44 | V00280 | TS-001 | Edge | Desktop | Missing_Password | Valid | High | Visitor |
| 45 | V00307 | TS-001 | Safari | Desktop | Weak_Password | Valid | High | Visitor |
| 46 | V00352 | TS-001 | Edge | Desktop | Password_Mismatch | Valid | High | Visitor |
| 47 | V00388 | TS-001 | Edge | Desktop | Terms_Not_Accepted | Valid | High | Visitor |
| 48 | V00424 | TS-001 | Edge | Desktop | Duplicate_Email | Valid | High | Visitor |

---

**Note:** This is an automated test plan generated using pairwise combinatorial testing techniques. For complex scenarios or higher-order interactions (3-way, 4-way), consider using specialized tools like `allpairspy`, `PICT`, or `ACTS`.
