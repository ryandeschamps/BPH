# Requirements Assessment - Ecommerce Website BRD

## Document Information
- **Document Title**: Business Requirements Document (BRD) - Online Apparels Shopping Website
- **Version**: 1.0
- **Date**: June 2019
- **Assessment Date**: November 13, 2025

## Executive Summary
This assessment analyzes the BRD for an ecommerce apparel website, identifying gaps, ambiguities, contradictions, and unstated assumptions that may impact development and testing efforts.

---

## 1. GAPS IN REQUIREMENTS

### 1.1 Security Requirements
- **GAP-001**: No authentication security requirements specified (password complexity, account lockout policies, session management)
- **GAP-002**: Missing data privacy/GDPR compliance requirements despite collecting personal information
- **GAP-003**: No mention of PCI-DSS compliance despite handling payment card data
- **GAP-004**: Missing encryption requirements for data at rest (only SSL for transmission mentioned in NFR-004)

### 1.2 User Experience Requirements
- **GAP-005**: No accessibility requirements (WCAG compliance, screen reader support)
- **GAP-006**: Missing mobile responsiveness or responsive design requirements
- **GAP-007**: No browser compatibility requirements specified
- **GAP-008**: Search functionality details not specified (fuzzy search, autocomplete, filters, sorting criteria)

### 1.3 Inventory Management
- **GAP-009**: No requirements for inventory tracking and stock level management
- **GAP-010**: Missing handling of out-of-stock items
- **GAP-011**: No requirement for low stock alerts or notifications
- **GAP-012**: Product SKU management not detailed

### 1.4 Order Management
- **GAP-013**: No order cancellation or modification requirements
- **GAP-014**: Missing return/refund policy and process requirements
- **GAP-015**: No requirements for partial order fulfillment
- **GAP-016**: Missing order status notification preferences (email, SMS, push)

### 1.5 Payment Processing
- **GAP-017**: No requirement for payment failure handling
- **GAP-018**: Missing refund processing requirements
- **GAP-019**: No mention of currency conversion or multi-currency support (only USD mentioned)
- **GAP-020**: Transaction history/invoice generation not specified

### 1.6 Shipping
- **GAP-021**: Multiple shipping addresses per user not addressed
- **GAP-022**: International shipping requirements not specified
- **GAP-023**: Shipping cost calculation methodology not defined
- **GAP-024**: Expedited shipping options not mentioned

### 1.7 Data & Reporting
- **GAP-025**: Data backup and recovery requirements missing
- **GAP-026**: Audit trail requirements not specified
- **GAP-027**: Customer analytics and behavior tracking not mentioned
- **GAP-028**: Export format details for reports not specified beyond "pdf and excel"

### 1.8 Integration Requirements
- **GAP-029**: Third-party integration requirements not specified (shipping carriers, email service providers)
- **GAP-030**: Social media login integration details missing (OAuth specifics)
- **GAP-031**: Payment gateway integration specifics not detailed

---

## 2. AMBIGUITIES

### 2.1 Functional Ambiguities
- **AMB-001**: FR-003 states users can search "without login" but FR-007 requires "register and login" for shopping cart - unclear when authentication becomes mandatory
- **AMB-002**: "Order tracking" mentioned multiple times but specifics are unclear - what information is visible? What statuses?
- **AMB-003**: FR-005 mentions "check shipping availability by PIN code" but no definition of what constitutes "available" vs "unavailable"
- **AMB-004**: FR-008 mentions "checkout and online payment" but relationship to "Place the order" is unclear - are these separate actions?

### 2.2 User Role Ambiguities
- **AMB-005**: Distinction between "Visitors" and "Buyers" is unclear - when does a visitor become a buyer?
- **AMB-006**: Sub-users vs Admin user permissions not clearly delineated
- **AMB-007**: FR-023 mentions "role based access" but no roles are defined

### 2.3 Data Ambiguities
- **AMB-008**: Product "variations" mentioned (color, size) but unclear if these are separate SKUs or attributes
- **AMB-009**: "PIN code" used for shipping - unclear if this is US ZIP code or Indian PIN code given US-only requirement
- **AMB-010**: Email verification requirement (FR-002) - what happens if email is not verified? Can user still browse?

### 2.4 Business Logic Ambiguities
- **AMB-011**: Ratings and reviews require "orders placed by buyer" (FR-011) but timing is unclear - immediately after order or after delivery?
- **AMB-012**: FR-020 states admin can "approve/reject" reviews - criteria for approval/rejection not specified
- **AMB-013**: NFR-002 states "30 seconds to load" - unclear if this is per page or entire site, and under what conditions

---

## 3. CONTRADICTIONS

### 3.1 Scope Contradictions
- **CON-001**: Section 3.2.2 lists "Cash on delivery option" as OUT OF SCOPE, but FR-008 only mentions credit/debit card and net banking, not explicitly excluding COD in functional requirements
- **CON-002**: Section 3.4.1 states "Website will accept orders from US country only" but assumes "US country" without defining international restrictions elsewhere

### 3.2 Functional Contradictions
- **CON-003**: FR-005 allows viewing product details "without login" but FR-006 requires login to add to wishlist - inconsistent authentication requirements
- **CON-004**: FR-002 states "email verification mandatory to login" but FR-001 mentions "login with Facebook and Google account" - unclear if social logins bypass email verification

### 3.3 User Role Contradictions
- **CON-005**: Section 3.3 shows Visitors can "Contact support" but FR-013 only mentions "Buyers" can contact support

### 3.4 Priority Contradictions
- **CON-006**: FR-020 (Payment Management) has no priority listed in the table but is critical functionality
- **CON-007**: Social media sharing is Priority 4 (Low) but mentioned as important for product discovery

---

## 4. UNSTATED ASSUMPTIONS

### 4.1 Business Assumptions
- **ASM-001**: Assumes single business owner/admin (no multi-vendor marketplace)
- **ASM-002**: Assumes all products ship from single warehouse location
- **ASM-003**: Assumes business operates in US time zones (no timezone requirements specified)
- **ASM-004**: Assumes English as the only language
- **ASM-005**: Assumes business has established shipping partnerships

### 4.2 Technical Assumptions
- **ASM-006**: Assumes stable internet connectivity for all users
- **ASM-007**: Assumes users have modern web browsers
- **ASM-008**: Assumes Stripe payment gateway will be used (mentioned in FR-020 but not as formal requirement)
- **ASM-009**: Assumes relational database for product catalog
- **ASM-010**: Assumes synchronous order processing

### 4.3 User Assumptions
- **ASM-011**: Assumes users have valid email addresses
- **ASM-012**: Assumes users understand ecommerce shopping process
- **ASM-013**: Assumes users have access to credit/debit cards or net banking
- **ASM-014**: Assumes users can receive email notifications

### 4.4 Data Assumptions
- **ASM-015**: Assumes product data is entered manually by admin
- **ASM-016**: Assumes product images are provided by admin
- **ASM-017**: Assumes customer data can be stored indefinitely
- **ASM-018**: Assumes email addresses are unique per user account

### 4.5 Process Assumptions
- **ASM-019**: Assumes linear checkout process (cart → checkout → payment → order)
- **ASM-020**: Assumes orders cannot be modified after placement
- **ASM-021**: Assumes admin manually updates order statuses
- **ASM-022**: Assumes ratings/reviews are moderated before publication

---

## 5. QUALITY CONCERNS

### 5.1 Non-Functional Requirements Issues
- **QC-001**: NFR-001 specifies only 100 concurrent users - very low for ecommerce site
- **QC-002**: NFR-002 allows 30 seconds page load time - industry standard is 2-3 seconds
- **QC-003**: No performance requirements for search, payment processing, or database queries
- **QC-004**: No availability/uptime requirements specified

### 5.2 Testability Concerns
- **QC-005**: Success criteria not defined for most requirements
- **QC-006**: No acceptance criteria provided
- **QC-007**: Measurement criteria for reports and statistics not specified
- **QC-008**: No error handling requirements defined

---

## 6. CRITICAL RISKS IDENTIFIED

### 6.1 High-Risk Gaps
1. **RISK-001**: Security requirements are severely lacking, exposing the application to potential vulnerabilities
2. **RISK-002**: Payment processing details are insufficient for PCI compliance
3. **RISK-003**: No error handling or edge case requirements defined
4. **RISK-004**: Inventory management gaps could lead to overselling

### 6.2 Medium-Risk Gaps
1. **RISK-005**: Missing mobile requirements in mobile-first shopping era
2. **RISK-006**: Inadequate search functionality definition may lead to poor user experience
3. **RISK-007**: No return/refund process could violate consumer protection laws
4. **RISK-008**: Missing accessibility requirements could limit market reach

---

## 7. RECOMMENDATIONS

### 7.1 Immediate Actions Required
1. Define comprehensive security requirements including authentication, authorization, and data protection
2. Specify PCI-DSS compliance requirements for payment processing
3. Add detailed inventory management requirements
4. Define error handling and edge case requirements
5. Clarify all identified ambiguities with stakeholders

### 7.2 Enhancement Recommendations
1. Add mobile responsiveness requirements
2. Define accessibility standards (WCAG 2.1 Level AA minimum)
3. Specify browser compatibility matrix
4. Add return/refund policy requirements
5. Define customer service and support requirements
6. Add performance benchmarks aligned with industry standards

### 7.3 Documentation Improvements
1. Add acceptance criteria for each functional requirement
2. Create data dictionary for key terms
3. Add user journey maps
4. Include wireframes or UI mockups reference
5. Add integration architecture diagram

---

## 8. CONCLUSION

The BRD provides a solid foundation for an ecommerce apparel website but requires significant refinement before development begins. Key areas needing immediate attention:

- **Security and Compliance**: Critical gaps in security, privacy, and payment compliance
- **User Experience**: Missing mobile, accessibility, and browser compatibility requirements
- **Business Processes**: Incomplete order management, inventory, and customer service requirements
- **Technical Specifications**: Insufficient detail on integrations, performance, and error handling

**Recommended Next Steps**:
1. Schedule requirements review session with stakeholders to address ambiguities and contradictions
2. Engage security team to define security requirements
3. Consult legal team regarding compliance requirements (PCI-DSS, data privacy)
4. Work with UX team to define user experience requirements
5. Update BRD with findings and obtain re-approval before proceeding to design phase

**Overall Assessment**: The BRD is approximately 60% complete and requires substantial additions before it can serve as a comprehensive basis for development and testing.
