# Requirements Assessment
**Document**: BRD - Online Apparels Shopping Website
**Date**: 2025-11-15
**Version**: 1.0

## Executive Summary
This assessment analyzes the Business Requirements Document for an e-commerce apparel website. The BRD defines 26 functional requirements (FR-001 to FR-026) and 4 non-functional requirements (NFR-001 to NFR-004) across buyer and admin functionality. This assessment identifies gaps, ambiguities, contradictions, and unstated assumptions that may impact testing and implementation.

## 1. Gaps in Requirements

### 1.1 Security Requirements
- **Password complexity rules**: FR-002 mentions password fields but doesn't specify complexity requirements (minimum length, character types, special characters)
- **Session management**: No requirements for session timeout, concurrent login handling, or session expiration
- **Data encryption**: NFR-004 mentions SSL for payments but doesn't address data at rest encryption
- **GDPR/Privacy compliance**: No requirements for data privacy, right to deletion, data export
- **Authentication lockout**: No mention of failed login attempt limits or account lockout policies
- **Two-factor authentication**: Not mentioned as an option for enhanced security

### 1.2 Error Handling
- **Validation error messages**: No specification for error message formats or user guidance
- **Payment failure scenarios**: What happens when payment fails? Retry logic? Order state?
- **Out of stock handling**: Mentioned in scope but not detailed in requirements
- **Network errors**: How should the system behave during connectivity issues?

### 1.3 Guest User Functionality
- **Guest checkout**: FR-003, FR-004, FR-005 mention guest users can browse but FR-008 requires login for checkout - no guest checkout option specified
- **Guest cart persistence**: How long does a guest cart persist? Can it be recovered?
- **Guest to registered conversion**: No workflow for converting guest cart to registered user

### 1.4 Product Management
- **Product SKU format**: Mentioned in assumptions but format not defined
- **Inventory synchronization**: How does website inventory sync with physical warehouse?
- **Low stock warnings**: No requirement for low stock indicators to buyers or admin
- **Product variants**: FR-019 mentions color/size but no details on how many variants per product
- **Product images**: Number of images per product not specified

### 1.5 Order Processing
- **Order cancellation**: No requirement for buyers to cancel orders
- **Order modification**: Can buyers modify orders after placement?
- **Return/refund process**: Not mentioned anywhere
- **Partial shipments**: What if order contains multiple items shipped separately?

### 1.6 Shipping
- **Shipping carriers**: Not specified which carriers will be used
- **Shipping zones**: "US only" mentioned but no state/region restrictions or shipping zones defined
- **Delivery time estimates**: No requirement to show estimated delivery dates
- **International shipping**: Explicitly out of scope, but border cases (Alaska, Hawaii, territories) not addressed

### 1.7 Payment
- **Payment gateway**: Stripe mentioned but no fallback if Stripe is down
- **Partial payments**: Not addressed
- **Refund processing**: No requirements for refund workflow
- **Payment status reconciliation**: How to handle payment pending states?
- **Currency**: USD mentioned but no multi-currency support defined

### 1.8 Search and Filtering
- **Search algorithm**: Keyword search mentioned but no details on fuzzy matching, autocomplete, typo tolerance
- **Filter options**: "filters" mentioned in FR-003 but not defined (price range, brand, size, color, rating?)
- **Sorting options**: "sorting" mentioned but options not specified (price, popularity, newest, rating?)
- **Search result relevance**: No requirements for search result ranking

### 1.9 Performance
- **Response time**: NFR-002 mentions 30-second page load (extremely high - typically should be <3 seconds)
- **Concurrent users**: NFR-001 mentions 100 users (very low for e-commerce)
- **Database performance**: No requirements for query optimization or database response times
- **Image optimization**: No requirements for image compression, CDN usage

### 1.10 Email Notifications
- **Email templates**: FR-025 mentions promotional emails but notification emails not fully specified
- **Order confirmation**: Mentioned in FR-008 but content not defined
- **Email preferences**: Can users opt out of certain emails?
- **Email delivery guarantees**: What if email fails to send?

### 1.11 Accessibility
- **WCAG compliance**: No requirements for accessibility standards
- **Screen reader support**: Not mentioned
- **Keyboard navigation**: Not specified
- **Color contrast**: Not addressed

### 1.12 Mobile Responsiveness
- No requirements explicitly stating mobile-responsive design
- No mobile app mentioned (web only assumed)

### 1.13 Analytics and Tracking
- **User behavior tracking**: Not mentioned
- **Conversion tracking**: Not specified
- **A/B testing capability**: Not addressed

## 2. Ambiguities

### 2.1 User Roles Confusion
- **Visitor vs Guest User**: Used interchangeably in FR-003, FR-004, FR-005 - are these the same role?
- **Admin vs Owner vs Sub-users**: FR-023 mentions sub-admin with roles but distinction from main admin is unclear

### 2.2 Social Login
- **FR-001**: "User will also be able to login into website using Facebook and Google account"
  - Does this auto-create an account or require prior registration?
  - How is email verification handled for social logins?
  - What if social account has no email?

### 2.3 Email Verification
- **FR-002**: "Email id verification would be mandatory to get login into website"
  - What happens if user doesn't verify email? Can they still browse? Add to cart?
  - How long is the verification link valid?
  - Can user resend verification email?

### 2.4 Wishlist vs Cart
- **FR-006 vs FR-007**: Both allow "proceed for checkout" - can users checkout from wishlist directly or must items move to cart first?

### 2.5 Product Ratings and Reviews
- **FR-011**: "User will be able post rating and review only for the products which he has ordered"
  - What's the timeframe? Can they review years later?
  - Can users update/delete their reviews?
  - One review per product or per order?

### 2.6 Order Status Workflow
- **FR-017**: Order states listed (Open, Confirmed, In process, Shipped, Delivered)
  - Missing cancelled, failed, returned states
  - State transition rules not defined
  - Can orders skip states?

### 2.7 Payment Method
- **FR-008**: "Credit card/ debit card" and "Net banking" listed
  - What about digital wallets (PayPal, Apple Pay, Google Pay)?
  - Is net banking US-specific or international?

### 2.8 Admin Payment Management
- **Unnamed requirement in FR section**: "Payment Management" mentioned but no FR number assigned
  - Should this be FR-019A or separate requirement?

### 2.9 Shipping Availability Check
- **FR-005**: "User will be able to check the shipping availability by entering PIN code"
  - PIN code is Indian term; US uses ZIP code - clarification needed
  - What's displayed if shipping not available?

### 2.10 Product Sharing
- **FR-009**: "User will be able to share product on social media"
  - Which platforms? (Facebook, Twitter, Instagram, Pinterest?)
  - Share as link or integrated post?

## 3. Contradictions

### 3.1 Guest User Checkout
- **Contradiction**:
  - FR-003, FR-004, FR-005: "Buyer/Guest user" can view products without login
  - FR-007: "User is required to get register and login to manage the items in his shopping cart"
  - FR-008: "Buyer is required to login into website for checkout and payment"
- **Issue**: Guest users can add to cart but can't manage cart or checkout - creates dead-end user flow

### 3.2 Cash on Delivery
- **Contradiction**:
  - Section 3.2.2: "Cash on delivery option for buyers" is **OUT OF SCOPE**
  - FR-008: Only lists "Credit card/debit card" and "Net banking"
- **Resolution**: Consistent, but worth noting as customers may expect COD for apparel

### 3.3 Real-time Order Tracking
- **Contradiction**:
  - Section 3.2.2: "Real time order tracking" is **OUT OF SCOPE**
  - FR-012: "User will be able to track his current orders from my orders section"
- **Issue**: What does "track" mean if not real-time? Manual status updates only?

### 3.4 Priority Ratings
- **Inconsistency**:
  - Section 5: Priority scale defined as 1-5 (Critical, High, Medium, Low, Future)
  - FR-006 (Wishlist): Priority = 2 (High) but seems less critical than FR-001 (Login) = 1
  - FR-009 (Social sharing): Priority = 4 (Low) - appropriate
  - FR-011 (Ratings): Priority = 2 (High) but can't be done without orders (chicken-egg)

### 3.5 Registration Fields
- **FR-002**: Registration form includes "Contact number"
- **FR-010**: My Account allows editing "phone number"
- **Issue**: Terminology inconsistency - same field different names

## 4. Unstated Assumptions

### 4.1 Technical Assumptions
1. **Platform**: Web-based responsive website (not native mobile apps)
2. **Browser support**: No specified browsers; assuming modern browsers (Chrome, Firefox, Safari, Edge)
3. **Database**: Not specified (assumed SQL-based for product catalog, orders, users)
4. **Hosting**: Not specified (cloud vs on-premise)
5. **CDN**: Not mentioned but likely needed for product images
6. **Third-party integrations**:
   - Payment: Stripe (mentioned)
   - Shipping: Not specified
   - Email service: Not specified
   - Social media APIs: Assumed for social login and sharing

### 4.2 Business Assumptions
1. **Single vendor**: Admin = business owner (no multi-vendor marketplace)
2. **B2C model**: Direct to consumer (not B2B or wholesale)
3. **Tax calculation**: Not mentioned - assumed automatic based on shipping address
4. **Pricing**: Fixed prices (no dynamic pricing, discounts, or promotional pricing mentioned)
5. **Inventory model**: Finite inventory (not made-to-order)
6. **Shipping cost**: Mentioned in FR-008 order summary but calculation not defined

### 4.3 User Assumptions
1. **Age restriction**: No age verification (assumed 18+ or parental consent for minors)
2. **Account uniqueness**: One email = one account (no multi-account per email)
3. **Address book**: Unlimited addresses assumed (no limit specified)
4. **Order history retention**: Permanent retention assumed

### 4.4 Data Assumptions
1. **Product catalog size**: No limits specified
2. **Order volume**: NFR-001 suggests low volume (100 concurrent users)
3. **Image storage**: Assumed cloud storage
4. **Backup and recovery**: Not mentioned but assumed

### 4.5 Regulatory Assumptions
1. **PCI DSS compliance**: Assumed for payment handling
2. **ADA compliance**: Not mentioned
3. **COPPA**: Not addressed (children's privacy)
4. **State sales tax**: Not detailed

## 5. Missing Non-Functional Requirements

### 5.1 Availability
- No uptime SLA defined (99.9%? 99.99%?)
- No maintenance window specifications

### 5.2 Disaster Recovery
- No backup requirements
- No disaster recovery plan requirements
- No data retention policy

### 5.3 Monitoring
- No requirements for system monitoring, alerting, logging

### 5.4 Browser Compatibility
- No browser version specifications
- No device compatibility matrix

### 5.5 Usability
- No usability testing requirements
- No user experience metrics

## 6. Recommendations for Clarification

### High Priority
1. **Define guest checkout workflow** or explicitly state registration is mandatory before checkout
2. **Clarify real-time vs non-real-time order tracking** (what does "track" mean?)
3. **Specify password complexity rules** and authentication policies
4. **Define product variant limits** and structure
5. **Specify search filters and sorting options** explicitly
6. **Define refund/return policy and workflow** (critical for e-commerce)
7. **Reduce page load time NFR** from 30 seconds to realistic <3 seconds
8. **Increase concurrent user NFR** from 100 to realistic e-commerce scale (1000+)

### Medium Priority
9. Define order cancellation and modification workflows
10. Specify email notification templates and triggers
11. Define shipping carrier integration requirements
12. Clarify social login account creation and email handling
13. Define inventory synchronization with warehouse
14. Specify security requirements (session, encryption, lockout)

### Low Priority
15. Add accessibility requirements
16. Define analytics and tracking requirements
17. Specify mobile responsiveness requirements
18. Define A/B testing capabilities

## 7. Risk Assessment

### High Risk
- **Security gaps**: Missing password policies, session management, data protection could lead to breaches
- **Performance NFRs unrealistic**: 30-second load time and 100 concurrent users suggest requirements need revision
- **Guest checkout contradiction**: May frustrate users who can't complete purchase as guest
- **Missing refund/return process**: Major gap for e-commerce business

### Medium Risk
- **Payment gateway single point of failure**: No fallback if Stripe is unavailable
- **Order tracking ambiguity**: May not meet customer expectations if not truly real-time
- **Incomplete order workflow**: Missing cancellation, modification, returns

### Low Risk
- **Terminology inconsistencies**: Minor but should be standardized
- **Priority inconsistencies**: Won't block implementation but may affect sequencing

## 8. Conclusion

The BRD provides a solid foundation for a basic e-commerce apparel website with clear functional requirements for buyer and admin roles. However, several critical gaps exist:

**Critical Gaps**:
- Security and authentication policies
- Refund/return workflows
- Order modification/cancellation
- Guest checkout workflow
- Realistic performance requirements

**Major Ambiguities**:
- Order tracking implementation
- Social login handling
- Guest vs registered user workflows

**Key Contradictions**:
- Guest checkout capability
- Real-time order tracking scope

**Recommendation**: Conduct requirements review session with stakeholders to address high-priority gaps and ambiguities before proceeding to design and development. Particular focus needed on e-commerce standard features (returns, cancellations) and realistic non-functional requirements (performance, scalability).

---
**Assessment completed**: 2025-11-15
**Next steps**: Extract and number requirements for traceability matrix
