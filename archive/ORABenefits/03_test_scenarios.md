# Test Scenarios: Oracle Fusion Cloud HR Benefits

## Document Information
- **Source**: Requirements Assessment and Entities & Flows Analysis
- **Date**: 2025-11-14
- **Total Scenarios**: 75
- **Format**: User Story (As a [role], I want to [action], so that I can [benefit])

---

## 1. New Hire Enrollment Scenarios

### TS-001: New Hire Initial Enrollment - Self Service
**As a** new employee,
**I want to** enroll in benefits during my initial enrollment period,
**so that I can** select health, dental, and life insurance coverage for myself and my family.
Related Requirements: REQ-001, REQ-080, REQ-121

### TS-002: New Hire with Default Enrollment
**As a** new employee who doesn't make active elections,
**I want to** be automatically enrolled in default plans,
**so that I can** have basic coverage even if I miss the enrollment deadline.
Related Requirements: REQ-002, REQ-082, REQ-083

### TS-003: New Hire Multiple Dependents
**As a** new employee with a spouse and children,
**I want to** add multiple dependents and enroll them in my benefit plans,
**so that I can** provide coverage for my entire family.
Related Requirements: REQ-003, REQ-051, REQ-058

### TS-004: New Hire FSA Election
**As a** new employee,
**I want to** use the FSA calculator and enroll in a Flexible Spending Account,
**so that I can** save on taxes for anticipated medical expenses.
Related Requirements: REQ-004, REQ-122

### TS-005: New Hire HSA Election
**As a** new employee,
**I want to** enroll in a high-deductible health plan with an HSA,
**so that I can** save for future medical expenses tax-free.
Related Requirements: REQ-005, REQ-122

### TS-006: New Hire Administrator-Assisted Enrollment
**As a** benefits specialist,
**I want to** enroll a new hire on their behalf,
**so that I can** assist employees who lack computer access or need help navigating the system.
Related Requirements: REQ-006, REQ-081

### TS-007: New Hire with Court Order
**As a** benefits administrator,
**I want to** enroll a new hire's designated dependent per court order,
**so that I can** comply with QMCSO requirements.
Related Requirements: REQ-007, REQ-101, REQ-102, REQ-103

### TS-008: New Hire Waive Coverage
**As a** new employee with coverage through spouse,
**I want to** waive medical coverage while enrolling in other benefits,
**so that I can** avoid duplicate coverage and reduce costs.
Related Requirements: REQ-008

---

## 2. Life Event Scenarios

### TS-009: Marriage - Add Spouse
**As an** employee who just got married,
**I want to** add my spouse to my medical and dental plans,
**so that I can** provide health coverage for my new family member.
Related Requirements: REQ-009

### TS-010: Birth of Child
**As an** employee who had a baby,
**I want to** add my newborn to my benefit plans,
**so that I can** provide coverage for my child from birth.
Related Requirements: REQ-010

### TS-011: Adoption
**As an** employee adopting a child,
**I want to** add my adopted child to my benefit plans,
**so that I can** provide coverage for my new family member.
Related Requirements: REQ-011

### TS-012: Divorce - Remove Spouse
**As an** employee going through divorce,
**I want to** remove my ex-spouse from my benefit plans,
**so that I can** end their coverage and adjust my premium costs.
Related Requirements: REQ-012

### TS-013: Spouse Loss of Coverage
**As an** employee whose spouse lost their job,
**I want to** add my spouse to my employer's benefit plans,
**so that I can** ensure they have health coverage during their job transition.
Related Requirements: REQ-013

### TS-014: Dependent Age Out
**As an** employee,
**I want to** be notified when my dependent reaches the age limit,
**so that I can** understand when their coverage will end and explore extension options.
Related Requirements: REQ-014

### TS-015: Death of Dependent
**As an** employee whose dependent passed away,
**I want to** remove them from my benefit plans,
**so that I can** end their coverage and adjust my premium accordingly.
Related Requirements: REQ-015

### TS-016: Address Change
**As an** employee who relocated,
**I want to** update my address and change my HMO plan if needed,
**so that I can** have access to in-network providers in my new location.
Related Requirements: REQ-016

### TS-017: Termination of Employment
**As a** benefits administrator,
**I want to** process benefits termination when an employee leaves,
**so that I can** end their coverage on their last day and offer COBRA if eligible.
Related Requirements: REQ-017

### TS-018: Return from Leave
**As an** employee returning from unpaid leave,
**I want to** reinstate my benefit elections,
**so that I can** resume my coverage.
Related Requirements: REQ-018

### TS-019: Salary Change Triggering New Eligibility
**As an** employee who received a promotion with salary increase,
**I want to** be evaluated for additional benefit eligibility,
**so that I can** access executive benefits I now qualify for.
Related Requirements: REQ-019

### TS-020: Length of Service Milestone
**As an** employee who reached 5 years of service,
**I want to** be automatically eligible for enhanced benefits,
**so that I can** enroll in additional vacation purchase or other service-based benefits.
Related Requirements: REQ-020

### TS-021: Age Milestone (Turning 50)
**As an** employee turning 50,
**I want to** be eligible for catch-up contributions to retirement plans,
**so that I can** increase my retirement savings.
Related Requirements: REQ-021

### TS-022: Late Life Event Reporting
**As an** employee who forgot to report a life event timely,
**I want to** report the event outside the window for administrator review,
**so that I can** request an exception for late enrollment.
Related Requirements: REQ-022, REQ-035

---

## 3. Open Enrollment Scenarios

### TS-023: Open Enrollment - Keep Current Plans
**As an** employee during open enrollment,
**I want to** review and confirm my current benefit elections,
**so that I can** keep the same coverage for the next year.
Related Requirements: REQ-023

### TS-024: Open Enrollment - Change Medical Plan
**As an** employee during open enrollment,
**I want to** compare medical plans and switch to a different option,
**so that I can** find coverage that better fits my needs and budget.
Related Requirements: REQ-024, REQ-123

### TS-025: Open Enrollment - Add New Plans
**As an** employee during open enrollment,
**I want to** enroll in plans I didn't have before (like vision or disability),
**so that I can** expand my coverage.
Related Requirements: REQ-025

### TS-026: Open Enrollment - Drop Plans
**As an** employee during open enrollment,
**I want to** drop plans I no longer need,
**so that I can** reduce my premium costs.
Related Requirements: REQ-026

### TS-027: Open Enrollment - FSA Restart
**As an** employee with an FSA,
**I want to** re-elect my FSA contribution amount for the new year,
**so that I can** continue using pre-tax dollars for medical expenses.
Related Requirements: REQ-027, REQ-122

### TS-028: Open Enrollment - Update Beneficiaries
**As an** employee during open enrollment,
**I want to** review and update my life insurance beneficiaries,
**so that I can** ensure my designation reflects my current wishes.
Related Requirements: REQ-028, REQ-057

### TS-029: Open Enrollment - Default for Non-Participants
**As a** benefits administrator after open enrollment closes,
**I want to** apply default rules for employees who didn't make elections,
**so that I can** ensure all employees have appropriate coverage.
Related Requirements: REQ-029, REQ-083

### TS-030: Open Enrollment - Trial Run
**As a** benefits administrator preparing for open enrollment,
**I want to** run a trial open enrollment,
**so that I can** verify plan configurations and identify issues before the actual period.
Related Requirements: REQ-030

### TS-031: Open Enrollment - Extend Window
**As a** benefits administrator,
**I want to** extend the open enrollment window by one week,
**so that I can** accommodate employees who need additional time.
Related Requirements: REQ-031

### TS-032: Open Enrollment - Intervening Life Event
**As an** employee who gets married during open enrollment,
**I want to** have my life event processed without losing my open enrollment elections,
**so that I can** add my spouse and keep my other selections.
Related Requirements: REQ-032

### TS-033: Open Enrollment - Rate Comparison
**As an** employee during open enrollment,
**I want to** see side-by-side rate comparisons of different plans,
**so that I can** make an informed decision based on costs and coverage.
Related Requirements: REQ-033, REQ-123

---

## 4. Administrator Functions Scenarios

### TS-034: Administrator Override Eligibility
**As a** benefits administrator,
**I want to** override eligibility rules to enroll an ineligible employee,
**so that I can** handle special circumstances approved by management.
Related Requirements: REQ-034

### TS-035: Administrator Process Manual Life Event
**As a** benefits administrator,
**I want to** manually process a life event marked outside timeliness,
**so that I can** approve late enrollments on a case-by-case basis.
Related Requirements: REQ-035, REQ-087

### TS-036: Administrator Review Action Items
**As a** benefits administrator,
**I want to** view all pending action items for participants,
**so that I can** follow up on missing certifications and documents.
Related Requirements: REQ-036, REQ-084

### TS-037: Administrator Approve Documents
**As a** benefits administrator,
**I want to** review and approve uploaded documents,
**so that I can** verify authenticity and complete certification requirements.
Related Requirements: REQ-037, REQ-097

### TS-038: Administrator Reject Documents
**As a** benefits administrator,
**I want to** reject invalid documents with a reason,
**so that I can** notify participants what needs to be resubmitted.
Related Requirements: REQ-038, REQ-097, REQ-100

### TS-039: Administrator Back Out Life Event
**As a** benefits administrator,
**I want to** back out a processed life event,
**so that I can** reverse incorrect enrollments and reprocess correctly.
Related Requirements: REQ-039

### TS-040: Administrator Reopen Life Event
**As a** benefits administrator,
**I want to** reopen a closed life event,
**so that I can** allow a participant to make changes after the window closed.
Related Requirements: REQ-040

### TS-041: Administrator Enter Overrides
**As a** benefits administrator,
**I want to** manually override enrollment details,
**so that I can** correct errors discovered after processing.
Related Requirements: REQ-041

### TS-042: Administrator Assign Benefits Relationship
**As a** benefits administrator,
**I want to** manually assign a benefits relationship to a worker,
**so that I can** handle complex assignment scenarios not covered by defaults.
Related Requirements: REQ-042, REQ-076

### TS-043: Administrator Run Diagnostic Reports
**As a** benefits administrator,
**I want to** run benefits health check diagnostics for a participant,
**so that I can** troubleshoot enrollment issues and data problems.
Related Requirements: REQ-043, REQ-111

---

## 5. Action Items & Certifications Scenarios

### TS-044: Upload Required Document
**As an** employee,
**I want to** upload a birth certificate for my new dependent,
**so that I can** complete my enrollment and activate coverage.
Related Requirements: REQ-044, REQ-096

### TS-045: Enrollment Suspension Due to Missing Document
**As an** employee who didn't upload required documents,
**I want to** understand why my enrollment is suspended,
**so that I can** complete the requirements to activate coverage.
Related Requirements: REQ-045, REQ-084

### TS-046: Interim Coverage During Suspension
**As an** employee with a suspended enrollment,
**I want to** have interim coverage during the document review period,
**so that I can** have some protection while my documents are being verified.
Related Requirements: REQ-046

### TS-047: Document Reuse Within Validity Period
**As an** employee with previously approved documents,
**I want to** have my documents automatically reused for new enrollments,
**so that I can** avoid uploading the same document multiple times.
Related Requirements: REQ-047, REQ-098, REQ-099

### TS-048: Administrator Extend Document Validity
**As a** benefits administrator,
**I want to** extend the validity period of an approved document,
**so that I can** accommodate special circumstances without requiring new uploads.
Related Requirements: REQ-048, REQ-098

### TS-049: Missing Certification Declaration
**As an** employee unable to provide a required document,
**I want to** declare that I cannot provide certification,
**so that I can** complete my enrollment with an attestation instead.
Related Requirements: REQ-049

### TS-050: Close Action Items in Bulk
**As a** benefits administrator after open enrollment,
**I want to** close action items in bulk for employees who didn't complete them,
**so that I can** finalize enrollment processing.
Related Requirements: REQ-050

---

## 6. Contacts & Beneficiaries Scenarios

### TS-051: Add Dependent Contact
**As an** employee,
**I want to** add a new dependent with their personal information,
**so that I can** designate them for benefit coverage.
Related Requirements: REQ-051

### TS-052: Update Contact Information
**As an** employee,
**I want to** update my dependent's address and phone number,
**so that I can** keep their contact information current.
Related Requirements: REQ-052

### TS-053: Designate Primary Beneficiary
**As an** employee,
**I want to** designate my spouse as 100% primary beneficiary for life insurance,
**so that I can** ensure proceeds go to them in case of my death.
Related Requirements: REQ-053

### TS-054: Multiple Beneficiaries with Percentages
**As an** employee,
**I want to** designate multiple primary beneficiaries with specific percentages,
**so that I can** split proceeds among multiple people (e.g., 50% spouse, 25% child 1, 25% child 2).
Related Requirements: REQ-054

### TS-055: Contingent Beneficiary Designation
**As an** employee,
**I want to** designate contingent beneficiaries,
**so that I can** ensure proceeds have a backup recipient if primary beneficiaries predecease me.
Related Requirements: REQ-055

### TS-056: Beneficiary Organization (Trust)
**As an** employee,
**I want to** designate a trust as my beneficiary,
**so that I can** manage distribution of proceeds through my estate plan.
Related Requirements: REQ-056

### TS-057: Update Beneficiary Anytime
**As an** employee,
**I want to** update my beneficiary designations outside of life events,
**so that I can** keep my designations current as my circumstances change.
Related Requirements: REQ-057

### TS-058: Dependent Eligibility Verification
**As a** benefits administrator,
**I want to** verify dependent eligibility through certifications,
**so that I can** ensure only eligible family members receive coverage.
Related Requirements: REQ-058

---

## 7. Billing & Payment Scenarios

### TS-059: Generate Billing Charges
**As a** benefits administrator,
**I want to** prepare and generate billing charges for a billing period,
**so that I can** collect employee contributions for benefit plans.
Related Requirements: REQ-059

### TS-060: Record Individual Payment
**As a** payroll administrator,
**I want to** record a check payment from an employee,
**so that I can** apply it to their outstanding charges.
Related Requirements: REQ-060

### TS-061: Upload Batch Payments
**As a** payroll administrator,
**I want to** upload a file of payroll deduction payments,
**so that I can** efficiently process payments for all employees at once.
Related Requirements: REQ-061

### TS-062: Allocate Payments to Charges
**As a** payroll administrator,
**I want to** run payment allocation to automatically apply payments to charges,
**so that I can** ensure correct billing status updates.
Related Requirements: REQ-062

### TS-063: Create Credit for Overpayment
**As a** payroll administrator,
**I want to** have overpayments automatically create credits,
**so that I can** apply them to future charges.
Related Requirements: REQ-063

### TS-064: Refund Excess Credit
**As a** benefits administrator,
**I want to** issue a refund for credits exceeding future charges,
**so that I can** return overpayments to employees.
Related Requirements: REQ-064

### TS-065: Create Arrears for Underpayment
**As a** payroll administrator,
**I want to** have underpayments automatically create arrears,
**so that I can** track and collect outstanding balances.
Related Requirements: REQ-065

### TS-066: Place Billing on Hold
**As a** benefits administrator,
**I want to** place an employee's billing on hold for one period,
**so that I can** accommodate temporary payment difficulties.
Related Requirements: REQ-066

### TS-067: Stop Billing Permanently
**As a** benefits administrator,
**I want to** stop billing for a termed employee,
**so that I can** prevent future charge generation.
Related Requirements: REQ-067

### TS-068: Prorated Charges for Mid-Period Changes
**As a** benefits administrator,
**I want to** have charges prorated when enrollments change mid-period,
**so that I can** ensure accurate billing for partial coverage periods.
Related Requirements: REQ-068

---

## 8. Data Management Scenarios

### TS-069: Bulk Update Benefits Groups via Workbook
**As a** benefits administrator,
**I want to** upload a spreadsheet to change benefits groups for multiple employees,
**so that I can** efficiently process organizational changes.
Related Requirements: REQ-069

### TS-070: Bulk Update Balances via Workbook
**As a** benefits administrator,
**I want to** upload a spreadsheet to update FSA or other benefit balances,
**so that I can** correct balance discrepancies in bulk.
Related Requirements: REQ-070

### TS-071: Test Data Changes in Roll Back Mode
**As a** benefits administrator,
**I want to** upload a workbook in roll back mode,
**so that I can** preview changes without committing them.
Related Requirements: REQ-071

### TS-072: Fix and Reupload Failed Rows
**As a** benefits administrator,
**I want to** download failed rows from a workbook upload,
**so that I can** correct errors and reupload successfully.
Related Requirements: REQ-072

### TS-073: Purge Staging Data
**As a** benefits administrator,
**I want to** purge staging data older than 6 months,
**so that I can** maintain system performance and remove obsolete data.
Related Requirements: REQ-073

### TS-074: Purge Voided Life Events
**As a** benefits administrator,
**I want to** purge voided life event data,
**so that I can** clean up events that were marked invalid and never processed.
Related Requirements: REQ-074

### TS-075: Delete Person Data in Non-Production
**As a** benefits administrator in a test environment,
**I want to** delete a person's benefits data completely,
**so that I can** reset test scenarios without residual data.
Related Requirements: REQ-075

---

## Scenario Categories Summary

| Category | Scenario IDs | Count |
|----------|-------------|-------|
| New Hire Enrollment | TS-001 to TS-008 | 8 |
| Life Events | TS-009 to TS-022 | 14 |
| Open Enrollment | TS-023 to TS-033 | 11 |
| Administrator Functions | TS-034 to TS-043 | 10 |
| Action Items & Certifications | TS-044 to TS-050 | 7 |
| Contacts & Beneficiaries | TS-051 to TS-058 | 8 |
| Billing & Payment | TS-059 to TS-068 | 10 |
| Data Management | TS-069 to TS-075 | 7 |
| **Total** | | **75** |

---

## Scenario Priority Classification

### Critical Priority (Must Test - 28 scenarios)
TS-001, TS-002, TS-003, TS-009, TS-010, TS-012, TS-017, TS-023, TS-024, TS-025, TS-027, TS-029, TS-030, TS-034, TS-035, TS-036, TS-037, TS-039, TS-040, TS-044, TS-045, TS-051, TS-053, TS-059, TS-062, TS-069, TS-070, TS-073

### High Priority (Comprehensive Test - 27 scenarios)
TS-004, TS-005, TS-006, TS-011, TS-013, TS-014, TS-016, TS-018, TS-019, TS-020, TS-022, TS-026, TS-028, TS-031, TS-032, TS-038, TS-041, TS-042, TS-046, TS-047, TS-052, TS-054, TS-057, TS-060, TS-063, TS-065, TS-071

### Medium Priority (Standard Test - 15 scenarios)
TS-007, TS-008, TS-015, TS-021, TS-033, TS-043, TS-048, TS-049, TS-050, TS-055, TS-056, TS-058, TS-064, TS-066, TS-074

### Low Priority (Basic Test - 5 scenarios)
TS-061, TS-067, TS-068, TS-072, TS-075

---

## Traceability to Requirements

Each scenario maps to requirements documented in:
- `01_requirements_assessment.md` - Functional requirements
- `02_entities_and_flows.md` - Entity relationships and user flows
- `using-benefits.txt` - Original Oracle documentation

---

## Next Steps

1. Define test variants with parameters (Step 4)
2. Create test data for each variant (Step 5)
3. Generate detailed test scripts for each scenario (Step 6)
4. Produce combinatorial test plan (Step 7)
5. Draft comprehensive test plan (Step 8)
6. Build requirements traceability matrix (Step 9)

---

**Document Prepared By**: QA Automation Process
**Date**: 2025-11-14
**Status**: Complete - Ready for Variant Definition
