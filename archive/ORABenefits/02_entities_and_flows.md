# Entities and Flows: Oracle Fusion Cloud HR Benefits

## Document Information
- **Source**: Requirements Assessment and using-benefits.txt analysis
- **Date**: 2025-11-14
- **Purpose**: Identify key entities and primary user/system flows for test scenario development

---

## 1. Key Entities

### 1.1 User Roles

#### **Participant (Employee)**
- **Description**: Employee enrolled in or eligible for benefits
- **Attributes**: Person number, name, hire date, benefits relationship, employment status
- **Responsibilities**:
  - Enroll in benefits during life events
  - Report life events
  - Upload required documents
  - Designate beneficiaries and dependents
  - Review and confirm enrollments
  - Make payments for employee-paid plans

#### **Benefits Administrator**
- **Description**: HR staff managing benefits administration
- **Attributes**: User ID, assigned benefits groups, data role access
- **Responsibilities**:
  - Process life events
  - Enter enrollments on behalf of participants
  - Review and approve documents
  - Manage action items and suspensions
  - Override eligibility and enrollments
  - Generate and review reports
  - Manage court orders

#### **Benefits Specialist**
- **Description**: HR staff providing participant support
- **Attributes**: User ID, support tier level
- **Responsibilities**:
  - Assist participants with enrollment questions
  - Enter enrollments via Benefits Service Center
  - Resolve participant queries
  - Update contact information
  - Print enrollment documents

#### **Payroll Administrator**
- **Description**: Staff managing payroll integration
- **Attributes**: User ID, payroll system access
- **Responsibilities**:
  - Verify payroll deductions
  - Manage payroll calendars
  - Reconcile benefits deductions
  - Process arrears and credits

#### **IT Security Manager**
- **Description**: Technical staff managing system access
- **Attributes**: User ID, admin privileges
- **Responsibilities**:
  - Configure data roles
  - Manage security profiles
  - Set up access controls

---

### 1.2 Core Benefits Entities

#### **Benefits Relationship**
- **Description**: Links worker to benefits eligibility rules
- **Attributes**:
  - Benefits relationship ID
  - Legal entity
  - Benefit group
  - Assignment associations
  - Start/end dates
  - Default relationship indicator
- **Business Rules**:
  - One default per legal entity
  - Multiple assignments can share one relationship
  - Each legal entity requires separate relationship (for multiple)

#### **Program**
- **Description**: Grouping of related benefit plans (e.g., Health & Welfare)
- **Attributes**:
  - Program ID, name
  - Eligibility rules
  - Enrollment opportunities
  - Life event types
  - Start/end dates

#### **Plan**
- **Description**: Specific benefit offering (e.g., Medical Plan A, Dental Plan)
- **Attributes**:
  - Plan ID, name, type
  - Plan administrator (carrier)
  - Eligibility rules
  - Enrollment requirements
  - Coverage levels (employee, family, etc.)
  - Start/end dates

#### **Option**
- **Description**: Specific plan choice (e.g., HMO, PPO)
- **Attributes**:
  - Option ID, name
  - Parent plan
  - Coverage details
  - Rate information
  - Start/end dates

#### **Enrollment**
- **Description**: Participant's election in a specific plan/option
- **Attributes**:
  - Enrollment ID
  - Participant
  - Program, plan, option
  - Coverage level
  - Covered dependents
  - Coverage start/end dates
  - Original coverage start date
  - Enrollment status (active, suspended, ended)
  - Life event reference
  - Action items

#### **Rate**
- **Description**: Cost of benefit plan
- **Attributes**:
  - Rate ID
  - Plan/option
  - Rate type (activity, variable, flex credit, composite)
  - Amount
  - Coverage level
  - Rate start/end dates
  - Display frequency

---

### 1.3 Life Event Entities

#### **Life Event**
- **Description**: Event triggering benefits enrollment opportunity
- **Attributes**:
  - Life event ID
  - Event type (marriage, birth, termination, etc.)
  - Event category (administrative, scheduled, temporal, unrestricted)
  - Occurred date
  - Reported date
  - Status (detected, unprocessed, manual, started, processed, backed out, voided)
  - Status date
  - Timeliness status
  - Benefits relationship
  - Participant

#### **Life Event Reason**
- **Description**: Specific reason for life event (e.g., marriage, divorce)
- **Attributes**:
  - Reason code
  - Description
  - Event category
  - Timeliness rules

#### **Enrollment Opportunity**
- **Description**: Available actions during life event (e.g., enroll, change, end)
- **Attributes**:
  - Opportunity type (enrollment, change, end coverage)
  - Programs/plans impacted
  - Enrollment method (explicit, implicit, automatic)
  - Default enrollment rule

---

### 1.4 Participant Relationship Entities

#### **Contact**
- **Description**: Individual related to participant (dependent, beneficiary)
- **Attributes**:
  - Contact ID
  - Name, date of birth, SSN
  - Relationship type (spouse, child, domestic partner)
  - Contact start date
  - Address, phone, email
  - Eligibility status

#### **Dependent**
- **Description**: Contact eligible for benefit coverage
- **Attributes**:
  - Inherits from Contact
  - Eligibility certification
  - Age-out date
  - Designation in plans

#### **Beneficiary**
- **Description**: Contact designated to receive benefit proceeds
- **Attributes**:
  - Inherits from Contact
  - Beneficiary type (primary, contingent)
  - Allocation percentage
  - Plans designated

#### **Beneficiary Organization**
- **Description**: Non-person beneficiary (trust, estate, charity)
- **Attributes**:
  - Organization name
  - EIN
  - Beneficiary type
  - Allocation percentage

---

### 1.5 Action Item & Certification Entities

#### **Action Item**
- **Description**: Required participant action to complete enrollment
- **Attributes**:
  - Action item ID
  - Action type (certification, dependent verification, document upload)
  - Enrollment reference
  - Status (pending, completed, overdue)
  - Due date
  - Suspension enabled
  - Completion date

#### **Certification**
- **Description**: Document requirement for enrollment
- **Attributes**:
  - Certification ID
  - Certification type
  - Determination rule (always, initial only)
  - Plan/option
  - Required/optional indicator
  - Validity period

#### **Document**
- **Description**: Uploaded supporting document
- **Attributes**:
  - Document ID
  - Document type
  - Upload date
  - Uploaded by
  - Approval status (pending, approved, rejected)
  - Rejection reason
  - Validity start/end dates

---

### 1.6 Billing Entities

#### **Billing Period**
- **Description**: Time period for billing
- **Attributes**:
  - Period ID
  - Start/end dates
  - Payment due date
  - Overdue date
  - Billing status (open, closed)

#### **Charge**
- **Description**: Amount owed by participant
- **Attributes**:
  - Charge ID
  - Participant
  - Plan/option
  - Billing period
  - Charge amount
  - Charge type (regular, arrears, credit)
  - Status (unpaid, partially paid, fully paid)

#### **Payment**
- **Description**: Payment received from participant
- **Attributes**:
  - Payment ID
  - Participant
  - Payment amount
  - Payment date
  - Payment method
  - Allocation status

#### **Credit**
- **Description**: Overpayment or credit issued to participant
- **Attributes**:
  - Credit ID
  - Participant
  - Credit amount
  - Source (overpayment, refund, adjustment)
  - Applied/unapplied indicator

---

### 1.7 Configuration Entities

#### **Benefits Group**
- **Description**: Group of participants with common benefit rules
- **Attributes**:
  - Group ID, name
  - Legal entity
  - Programs available
  - Billing calendar

#### **Eligibility Profile**
- **Description**: Rules defining who is eligible for benefits
- **Attributes**:
  - Profile ID
  - Criteria (job, location, salary, service)
  - Include/exclude rules
  - Formula

#### **Enrollment Display**
- **Description**: Configuration for how enrollments display
- **Attributes**:
  - Display grouping
  - Rate display frequency
  - Sort order
  - Show/hide options

#### **Court Order**
- **Description**: QMCSO requiring dependent coverage
- **Attributes**:
  - Order ID
  - Order date
  - Designated dependent
  - Required plan/plan type
  - Enforcement start/end dates

---

### 1.8 Process Entities

#### **Batch Process**
- **Description**: Scheduled or on-demand system process
- **Attributes**:
  - Process ID
  - Process name
  - Status (running, completed, error)
  - Start/end time
  - Parameters
  - Log file location

#### **Audit Log**
- **Description**: Record of system actions
- **Attributes**:
  - Log ID
  - Timestamp
  - User
  - Action performed
  - Before/after values

#### **Staging Data**
- **Description**: Temporary data for batch processing
- **Attributes**:
  - Staging ID
  - Source (workbook, integration)
  - Validation status
  - Error messages
  - Created date

---

## 2. Primary User Flows

### 2.1 New Hire Initial Enrollment

**Actor**: Participant (Employee)
**Trigger**: Hire date reached
**Preconditions**:
- Person record created in HR system
- Benefits relationship assigned
- Eligibility evaluated

**Flow**:
1. System detects new hire event (temporal/administrative)
2. System runs "Evaluate Life Event Participation" process
3. System determines eligible programs and plans
4. System creates life event with "Started" status
5. Participant receives notification of enrollment opportunity
6. Participant logs into Benefits work area
7. Participant reviews "Me - Benefits" dashboard
8. Participant clicks "Enroll" for new hire event
9. System displays eligible programs and plans
10. Participant adds/verifies contacts (spouse, children)
11. Participant selects plans and coverage levels
12. Participant designates dependents for each plan
13. Participant designates beneficiaries (life insurance, retirement)
14. Participant uses FSA/HSA calculator (if applicable)
15. Participant reviews enrollment summary
16. Participant confirms selections
17. System generates action items (certifications, document uploads)
18. Participant uploads required documents
19. System suspends enrollment if documents not complete
20. Administrator reviews and approves documents
21. System completes action items
22. System runs "Close Enrollment" process
23. System activates enrollment
24. System creates payroll deduction elements
25. System sends confirmation to participant
26. Life event status changes to "Processed"

**Postconditions**:
- Enrollments active with coverage start dates
- Payroll deductions created
- Action items completed or suspended
- Life event closed

**Alternative Flows**:
- **Default Enrollment**: System auto-enrolls per configuration
- **Administrator-Assisted**: Administrator enters enrollment on behalf
- **Missed Deadline**: Enrollment window closes, default rules apply
- **Document Rejection**: Participant must resubmit documents

---

### 2.2 Life Event Processing (Marriage Example)

**Actor**: Participant (Employee)
**Trigger**: Participant gets married
**Preconditions**: Active employment with benefits

**Flow**:
1. Participant logs into Benefits work area
2. Participant clicks "Report Life Event"
3. Participant selects "Marriage" as life event reason
4. Participant enters event occurred date (marriage date)
5. System validates timeliness (within 30/60 days)
6. System saves life event with "Unprocessed" status
7. System runs "Evaluate Life Event Participation" process
8. System determines eligible programs and plans for change
9. System calculates coverage start date per plan rules
10. System updates life event status to "Started"
11. Participant receives notification to complete enrollment
12. Participant adds spouse as new contact
13. Participant enters spouse information (name, DOB, SSN, start date)
14. Participant reviews current enrollments
15. Participant adds spouse to medical plan
16. Participant adds spouse to dental plan
17. Participant updates life insurance beneficiary
18. Participant reviews rate changes (employee+spouse vs. employee only)
19. System displays prorated deduction amounts
20. Participant confirms changes
21. System generates certification action items (marriage certificate)
22. Participant uploads marriage certificate
23. Administrator reviews document
24. Administrator approves document
25. System completes action item
26. System runs "Close Enrollment" process
27. System ends previous enrollment (employee only)
28. System starts new enrollment (employee + spouse)
29. System updates payroll deductions
30. Life event status changes to "Processed"

**Postconditions**:
- Spouse added as contact
- Medical and dental coverage updated to employee+spouse
- Beneficiary designation updated
- New rates applied
- Previous coverage end-dated
- New coverage started

**Alternative Flows**:
- **Late Reporting**: Event outside timeliness, status set to "Manual"
- **Suspension**: Document not uploaded, enrollment suspended with interim coverage
- **Intervening Event**: Another event occurs, first event may back out
- **No Changes**: Participant chooses not to add spouse

---

### 2.3 Open Enrollment (Scheduled Event)

**Actor**: Benefits Administrator + All Participants
**Trigger**: Annual open enrollment period
**Preconditions**:
- Programs and plans configured for new year
- Rates updated
- In-progress life events resolved

**Flow**:

**Phase 1: Preparation (Admin)**
1. Administrator updates plan configuration
2. Administrator adds new plans for next year
3. Administrator ends plans being discontinued
4. Administrator updates rates (standard and variable)
5. Administrator configures enrollment display settings
6. Administrator resolves any in-progress life events
7. Administrator runs "Trial Open Enrollment"
8. System processes test enrollments
9. Administrator reviews trial results
10. Administrator investigates any errors
11. Administrator fixes configuration issues
12. Administrator runs trial again until clean

**Phase 2: Enrollment Period (Admin + Participants)**
13. Administrator runs "Evaluate Scheduled Event Participation"
14. System creates open enrollment event for all eligible participants
15. System evaluates eligibility as of assigned life event date
16. System determines enrollment opportunities per participant
17. Life events status set to "Started"
18. Administrator optionally runs "Enroll in Default Benefits"
19. System applies default enrollment rules
20. Participants receive notification of open enrollment
21. Participant logs into Benefits work area
22. Participant sees "Open Enrollment" event in progress
23. Participant clicks "Enroll"
24. System displays current enrollments and available plans
25. Participant reviews current elections
26. Participant compares plans (side-by-side comparison)
27. Participant keeps some plans (medical)
28. Participant changes some plans (dental - new carrier)
29. Participant enrolls in new FSA (must reelect annually)
30. Participant updates beneficiaries
31. Participant reviews enrollment summary
32. Participant confirms elections
33. System saves enrollment choices
34. System generates action items (if new plans require certs)
35. **Concurrent**: Administrator assists participants with questions
36. **Concurrent**: Administrator enters enrollments for participants without access
37. **Concurrent**: System processes intervening life events (marriages, births)
38. Intervening event may back out open event
39. System reprocesses open event after intervening event
40. System applies reinstatement rules

**Phase 3: Post-Enrollment (Admin)**
41. Enrollment period ends
42. Administrator runs "Close Enrollment" process
43. System closes all open enrollment events
44. System applies default rules for non-electing participants
45. System ends previous year enrollments (coverage end date)
46. System starts new year enrollments (coverage start date)
47. System generates final action items
48. Administrator runs "Enrollment Results" report
49. Administrator investigates incorrect enrollments
50. Administrator enters overrides as needed
51. Administrator runs "Close Enrollment Action Items"
52. System resolves outstanding certifications
53. Administrator inactivates ended plans (optional)
54. Life events status change to "Processed"
55. New plan year effective (January 1)

**Postconditions**:
- All eligible participants processed
- New year enrollments active
- Previous year enrollments ended
- Rates updated for new year
- Action items completed or pending
- Payroll deductions updated

**Alternative Flows**:
- **Extend Enrollment Window**: Administrator extends deadline for late participants
- **Process Errors**: Administrator restarts evaluation for failed participants
- **Back Out and Reprocess**: Administrator backs out enrollment to fix errors
- **Manual Processing**: Administrator manually processes participants set to "Manual" status

---

### 2.4 Administrator-Assisted Enrollment

**Actor**: Benefits Specialist (on behalf of Participant)
**Trigger**: Participant requests assistance or lacks system access
**Preconditions**:
- Participant has in-progress life event
- Administrator has data role access to participant

**Flow**:
1. Participant contacts Benefits Service Center (phone, email, in-person)
2. Benefits Specialist logs into Benefits Service Center
3. Specialist searches for participant by name or person number
4. Specialist selects participant from search results
5. System displays participant's Benefits Summary page
6. Specialist reviews participant's current enrollments
7. Specialist reviews participant's in-progress life event
8. Specialist clicks "Enroll" for life event
9. System displays enrollment wizard
10. Specialist discusses plan options with participant
11. Participant provides election choices verbally
12. Specialist selects plans per participant instructions
13. Specialist designates dependents per participant instructions
14. Specialist reviews enrollment summary with participant
15. Participant verbally confirms selections
16. Specialist submits enrollment
17. System generates action items
18. Specialist prints enrollment confirmation
19. Specialist provides confirmation to participant
20. Specialist notes interaction in participant record
21. System processes enrollment per standard flow

**Postconditions**:
- Enrollment entered on behalf of participant
- Confirmation provided to participant
- Action items generated
- Enrollment pending document uploads

**Alternative Flows**:
- **Override Eligibility**: Specialist overrides eligibility restrictions
- **Print for Offline Election**: Specialist prints forms, participant completes, specialist enters later
- **Update Contact Information**: Specialist updates participant contacts before enrolling

---

### 2.5 Action Item Resolution

**Actor**: Participant + Benefits Administrator
**Trigger**: Action item generated during enrollment
**Preconditions**:
- Enrollment submitted
- Certification requirement exists

**Flow**:
1. System generates action item (e.g., birth certificate for new dependent)
2. System determines if suspension enabled for this certification
3. If suspension enabled:
   - System suspends enrollment
   - System applies interim coverage (if configured)
   - System sends notification to participant
4. Participant receives email notification of pending action
5. Participant logs into Benefits work area
6. Participant navigates to "Pending Actions" page
7. Participant sees list of action items with due dates
8. Participant clicks action item to view details
9. Participant clicks "Upload Document"
10. Participant selects file (PDF, JPG) from computer
11. Participant uploads file
12. System validates file type and size
13. System creates document record
14. System sends notification to administrator
15. Administrator receives notification of document to review
16. Administrator logs into Benefits Service Center
17. Administrator navigates to "Documents to Review" work area
18. Administrator sees list of pending documents
19. Administrator opens participant's document
20. Administrator reviews document for authenticity and completeness
21. If acceptable:
    - Administrator clicks "Approve"
    - System marks action item "Completed"
    - System lifts enrollment suspension
    - System activates enrollment
    - System sends confirmation to participant
22. If not acceptable:
    - Administrator clicks "Reject"
    - Administrator enters rejection reason
    - System sends notification to participant with reason
    - Participant must upload new document
    - Process repeats from step 9

**Postconditions**:
- Action item completed
- Enrollment activated (if suspended)
- Document approved and stored
- Certification requirement satisfied

**Alternative Flows**:
- **Document Reuse**: System reuses previously approved document within validity period
- **Administrator Upload**: Administrator uploads document on behalf of participant
- **Third-Party Upload**: External system uploads document via integration
- **Missing Certification Declaration**: Participant declares unable to provide document
- **Due Date Passed**: Action item appears on audit reports, enrollment remains suspended

---

### 2.6 Billing and Payment Processing

**Actor**: Participant + Payroll Administrator
**Trigger**: Billing period ends
**Preconditions**:
- Active enrollments exist
- Billing calendar configured

**Flow**:
1. Benefits Administrator runs "Prepare Benefit Coverage Charge Data"
2. System calculates charges for all participants
3. System aggregates charges by billing period
4. System prorates for partial period enrollments
5. System creates charge records
6. Administrator reviews charge preparation report
7. Administrator edits charges if needed (adjustments)
8. Administrator runs "Generate Benefit Coverage Charges"
9. System finalizes charges
10. System sets billing period status to "Open"
11. System generates bills for participants
12. Participant receives billing statement (email, portal)
13. Participant reviews charges
14. Participant makes payment (check, online payment)
15. Payroll Administrator receives payment
16. Payroll Administrator records payment in system
17. System creates payment record
18. If batch payments (payroll deduction):
    - Payroll Administrator uploads payment file
    - Administrator runs "Allocate and Reconcile Payments"
19. System allocates payment to charges:
    - Earliest billing period first
    - Highest amount first within period
20. If payment = charges:
    - System marks billing period "Fully Paid"
21. If payment < charges:
    - System marks "Partially Paid"
    - System creates arrears for unpaid amount
    - Arrears added to next billing period
22. If payment > charges:
    - System marks "Fully Paid"
    - System creates credit for overpayment
    - Credit automatically applied to next period
23. If credit exceeds future charges:
    - Administrator issues refund
    - System creates refund transaction
24. System updates billing status
25. Participant receives payment confirmation

**Postconditions**:
- Charges generated and paid
- Billing period closed
- Arrears or credits created if applicable
- Payment allocated correctly

**Alternative Flows**:
- **Hold Billing**: Administrator places billing on hold for one period
- **Stop Billing**: Administrator stops billing permanently
- **Manual Adjustment**: Administrator manually adjusts charges (error correction)
- **Credit Application**: Administrator manually applies credit to specific charge

---

### 2.7 Data Management via Integrated Workbooks

**Actor**: Benefits Administrator
**Trigger**: Need to bulk update benefits data
**Preconditions**:
- Appropriate data role permissions
- Workbook template available

**Flow**:
1. Administrator navigates to Navigator > Tools > My Integrated Workbooks
2. Administrator selects workbook type (e.g., "Person Benefit Groups")
3. Administrator clicks "Create"
4. System prompts for selection criteria
5. Administrator enters person numbers or selection rule
6. System generates workbook with current data
7. Administrator downloads Excel file
8. Administrator opens file in Excel
9. Administrator reviews current data
10. Administrator makes changes (e.g., change benefit group)
11. Administrator saves file
12. Administrator uploads modified file
13. System validates data:
    - Required fields populated
    - Data types correct
    - Business rules satisfied
14. If validation errors:
    - System displays error messages
    - System sets status to "Upload Failed"
    - Administrator downloads failed rows
    - Administrator fixes errors
    - Administrator re-uploads (back to step 12)
15. If validation successful:
    - System previews changes
    - Administrator reviews changes
16. Administrator can choose mode:
    - **Roll Back**: Test mode, no changes committed
    - **Save**: Commit changes
17. If Roll Back:
    - System simulates changes
    - System shows what would happen
    - No data modified
    - Administrator reviews results
18. If Save:
    - System commits changes
    - System end-dates previous records
    - System creates new records with session effective date
    - System preserves history
19. System displays upload results
20. Administrator reviews success/failure counts
21. System sets status to "Upload Succeeded"

**Postconditions**:
- Bulk data updated
- History preserved
- Changes effective as of session date

**Alternative Flows**:
- **Large Data Set**: Administrator processes in batches of 500 rows
- **Delete Records**: Administrator deletes records (permanent, cannot recover)
- **Concurrent Updates**: System detects concurrent modification, last upload wins

---

### 2.8 Benefits Relationship Assignment

**Actor**: System (Automated) + Benefits Administrator
**Trigger**: New hire, assignment change, or manual assignment
**Preconditions**:
- Default benefits relationship configured
- Person record exists

**Flow**:

**Automatic Assignment (New Hire)**
1. Person hired in HR system
2. System detects new assignment
3. System checks "Configure Default Benefits Relationships"
4. If configuration exists for legal entity:
   - System creates benefits relationship for worker
   - System associates assignment to relationship
   - System sets default relationship indicator
5. If multiple assignments exist:
   - System checks "Enable Multiple Assignment Processing"
   - If enabled:
     - System determines primary assignment
     - System associates all assignments to relationship
   - If separate relationships required:
     - System creates relationship per legal entity
6. System runs "Assign and Update Benefits Relationships" process
7. System assigns relationship to worker
8. System triggers life event detection (new hire)

**Manual Assignment (Administrator)**
1. Administrator navigates to worker's Benefits Summary
2. Administrator clicks "Manage Benefits Relationship"
3. Administrator selects target benefits relationship
4. Administrator clicks "Assign"
5. System validates assignment
6. System creates association
7. System triggers reevaluation of benefits

**Refresh Processing (Maintenance)**
1. Administrator runs "Assign and Update Benefits Relationships" process
2. System checks all workers
3. For each worker:
   - If no relationship and configuration exists: Create relationship
   - If relationship exists: Update assignment associations
   - If termination: End-date relationship
   - If transfer: End current, start new
4. System updates all workers per configuration

**Postconditions**:
- Benefits relationship assigned to all workers
- Assignments associated correctly
- Life events can be processed

**Alternative Flows**:
- **Multiple Legal Entities**: Separate relationship per entity
- **Transfer Between Entities**: End one relationship, start another
- **Concurrent Relationships**: Multiple relationships processed independently

---

### 2.9 Document Upload and Approval

**Actor**: Participant + Benefits Administrator
**Trigger**: Certification requirement during enrollment
**Preconditions**:
- Enrollment submitted
- Certification configured for plan

**Flow**:
1. System generates certification action item
2. System determines certification type (marriage cert, birth cert, etc.)
3. System checks determination rule:
   - Always: Required every enrollment
   - Initial Enrollment Only: Required first time only
4. If "Initial Enrollment Only" and document previously approved:
   - System reuses previous document (within validity period)
   - System completes action item automatically
   - Flow ends
5. If document required:
   - System creates action item
   - System sends notification to participant
6. Participant logs into Benefits work area
7. Participant navigates to Pending Actions
8. Participant clicks action item
9. System displays upload form
10. Participant clicks "Choose File"
11. Participant selects file from computer
12. Participant clicks "Upload"
13. System validates file:
    - File type allowed (PDF, JPG, PNG)
    - File size under limit
14. System creates document record
15. System associates document to action item
16. System sets approval status to "Pending"
17. System sends notification to administrator
18. Administrator logs into Benefits Service Center
19. Administrator navigates to "Documents to Review"
20. Administrator filters by document type or participant
21. Administrator opens document
22. System displays document viewer
23. Administrator reviews document details
24. Administrator verifies authenticity
25. Administrator decides:
    **If Approve:**
    - Administrator clicks "Approve"
    - System sets approval status to "Approved"
    - System calculates validity end date
    - System completes action item
    - System sends confirmation to participant
    - If enrollment suspended: System lifts suspension
    - If enrollment suspended: System activates enrollment

    **If Reject:**
    - Administrator clicks "Reject"
    - Administrator enters rejection reason
    - System sets approval status to "Rejected"
    - System sends notification to participant with reason
    - System keeps action item pending
    - Participant must upload new document (back to step 10)

**Postconditions**:
- Document uploaded and approved/rejected
- Action item completed or remains pending
- Enrollment activated if suspension lifted

**Alternative Flows**:
- **Administrator Upload on Behalf**: Administrator uploads document for participant
- **Document Reuse**: System automatically reuses valid document
- **Validity Extension**: Administrator extends validity period for individual document
- **Multiple Documents**: Participant uploads multiple documents for same certification

---

### 2.10 Court Order (QMCSO) Processing

**Actor**: Benefits Administrator
**Trigger**: Court order received requiring dependent coverage
**Preconditions**:
- Court order document received
- Designated dependent exists or will be added

**Flow**:
1. Administrator receives court order (mail, fax, email)
2. Administrator reviews court order for requirements
3. Administrator navigates to Benefits Service Center
4. Administrator searches for participant
5. Administrator selects participant's Benefits Summary
6. Administrator clicks "Court Orders" section
7. Administrator clicks "Add Court Order"
8. Administrator enters court order details:
   - Order ID
   - Order date
   - Issuing court
   - Designated dependent
   - Required plan or plan type
   - Enforcement start date
9. If designated dependent doesn't exist:
   - Administrator adds dependent as contact
10. Administrator saves court order
11. System validates enforcement rules:
    - Designated dependent must be enrolled
    - Cannot opt out dependent
    - Cannot end-date dependent
    - Cannot delete dependent
12. If dependent not currently enrolled:
    - Administrator creates administrative life event
    - Administrator enrolls dependent per court order
13. System enforces court order requirements:
    - Participant cannot remove dependent during self-service
    - Administrator override required to end coverage
14. System displays court order on:
    - Administrator's Enrollment Results page
    - Participant's Confirmation Summary page
15. Court order remains enforced until:
    - Administrator enters enforcement end date
    - Court order expires

**Postconditions**:
- Court order recorded in system
- Designated dependent enrolled
- Coverage cannot be terminated without override
- Court order visible to administrators and participant

**Alternative Flows**:
- **Multiple Dependents**: Court order requires coverage for multiple children
- **Specific Plan**: Court order specifies exact plan, not just plan type
- **Coverage Already Exists**: Dependent already enrolled, system prevents opt-out
- **Court Order Modification**: Administrator updates court order with new details

---

## 3. Secondary System Flows

### 3.1 Temporal Event Detection
- System runs scheduled process
- System evaluates age changes, service milestones, salary changes
- System creates temporal life events
- System processes events per timeliness rules

### 3.2 Dependent Age-Out
- System detects dependent reaches age limit
- System creates loss of eligibility event
- System ends dependent coverage
- System notifies participant

### 3.3 Enrollment Back Out
- Administrator runs "Back Out Life Events" process
- System reverses enrollments
- System restores previous enrollments
- System updates life event status to "Backed Out"

### 3.4 Enrollment Reopen
- Administrator runs "Reopen Life Events" process
- System changes status from "Processed" to "Started"
- Enrollment window reopens
- Participant can make new elections

### 3.5 Data Purge
- Administrator runs purge process
- System validates data age (>6 months)
- System deletes staging/audit/voided event data
- System generates purge report

### 3.6 Benefits Health Check
- Administrator runs diagnostic report
- System evaluates participant's benefits configuration
- System identifies issues (missing data, configuration errors)
- System generates report with recommendations

### 3.7 Override Eligibility
- Administrator identifies participant incorrectly marked ineligible
- Administrator navigates to enrollment
- Administrator clicks "Override"
- Administrator enters override reason
- System allows enrollment despite eligibility rules

### 3.8 FSA/HSA Calculator Usage
- Participant considering FSA or HSA enrollment
- Participant clicks calculator link
- Participant enters income, tax filing status, expected medical expenses
- System calculates tax savings
- System displays comparison of FSA vs. HSA
- Participant uses results to inform election decision

---

## 4. Integration Flows

### 4.1 Payroll Integration Flow
1. Enrollment processed in Benefits
2. System creates deduction element entries
3. System sends element entries to Payroll
4. Payroll processes deductions
5. Payroll reports deduction actuals back to Benefits
6. Benefits reconciles expected vs. actual deductions

### 4.2 Vendor Integration Flow
1. Enrollment processed in Benefits
2. System generates vendor file (EDI 834)
3. System sends file to external vendor/carrier
4. Vendor processes enrollment
5. Vendor sends confirmation file back
6. System reconciles enrollment confirmations

### 4.3 HR Integration Flow
1. HR event occurs (hire, termination, personal data change)
2. HR system sends event data to Benefits
3. Benefits system detects life event
4. Benefits processes life event per configured rules

---

## 5. Error and Exception Flows

### 5.1 Process Error Handling
- Batch process encounters error
- System logs error details
- System continues processing remaining records
- Administrator reviews error log
- Administrator fixes data/configuration
- Administrator restarts process for failed records

### 5.2 Suspended Enrollment Management
- Enrollment suspended due to incomplete action items
- Participant attempts to process new life event
- System blocks new life event
- System displays message about suspended enrollment
- Participant must complete action items before proceeding

### 5.3 Intervening Life Event Handling
- Open enrollment in progress
- Participant reports marriage
- System backs out open enrollment event
- System processes marriage event
- System reprocesses open enrollment event
- System applies reinstatement rules to restore elections

### 5.4 Late Life Event Reporting
- Participant reports life event outside timeliness window
- System marks event status as "Manual"
- System notifies administrator
- Administrator manually evaluates timeliness
- Administrator manually processes event or denies

---

## 6. Entity Relationships

```
Participant
├── Benefits Relationships (1 to many)
│   ├── Life Events (1 to many)
│   │   ├── Enrollments (1 to many)
│   │   │   ├── Action Items (1 to many)
│   │   │   ├── Covered Dependents (0 to many)
│   │   │   └── Beneficiary Designations (0 to many)
│   │   └── Enrollment Opportunities (1 to many)
│   └── Benefits Group (many to 1)
│       └── Billing Calendar (many to 1)
│           └── Billing Periods (1 to many)
│               └── Charges (1 to many)
│                   └── Payments (many to many)
│
├── Contacts (1 to many)
│   ├── Dependents (subtype)
│   └── Beneficiaries (subtype)
│
├── Assignments (1 to many)
│   └── Benefits Relationship (many to 1)
│
└── Court Orders (1 to many)
    └── Designated Dependents (1 to 1)

Programs (1 to many Plans)
└── Plans (1 to many Options)
    ├── Eligibility Profiles (many to many)
    ├── Rates (1 to many)
    ├── Certifications (1 to many)
    └── Enrollment Opportunities (many to many)
```

---

## Summary

This document identifies:
- **18 key entities** across user roles, benefits objects, life events, relationships, billing, and configuration
- **10 primary user flows** covering the most common and critical business processes
- **8 secondary system flows** for maintenance and support activities
- **3 integration flows** for external system communication
- **4 error and exception flows** for handling special cases

These entities and flows form the foundation for deriving comprehensive test scenarios that will cover all critical paths through the Oracle Fusion Cloud HR Benefits system.

**Next Step**: Derive Test Scenarios (Step 3)
