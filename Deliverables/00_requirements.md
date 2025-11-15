# Requirements Specification
## Ecommerce Website - Online Apparels Shopping Platform

**Source Document**: Business Requirements Document (BRD) v1.0, June 2019
**Extraction Date**: November 15, 2025
**Total Requirements**: 30 (26 Functional + 4 Non-Functional)
**Extraction Approach**: Approach A (Documented Requirements - extracted exactly as specified in source)

---

## Buyer Authentication and Registration

### REQ-001: Login
**Description**: User will be able to login into the website using the email and password. Reset password option for the users to reset the password in case of forgot password. User will also be able to login into website using Facebook and Google account.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

### REQ-002: Registration
**Description**: Buyers will be able to get registered on website with simple registration form with below details: First name, Last name, Email id, Contact number, Password, Conform password, Accept terms and conditions. Email id verification would be mandatory to get login into website. User will receive email verification link on registered email id to verify the email. Once email id verified successfully, user will be able login into website with email and password.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

---

## Product Discovery and Browsing

### REQ-003: Product Search
**Description**: Buyers will be able to search the products by keyword, by browsing through category/sub-category, using filters and sorting options. User would be able to search for the products without login into website.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer, Visitor

### REQ-004: Product Listing
**Description**: Buyers will be able to view the listing of the product with following details: Product title, Thumbnail image, Price, Ratings & reviews. By clicking on product title and image, user will be able to navigate on product detail page to view more details of the product. User should be able to view the products listing and details without login.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer, Visitor

### REQ-005: Product Details
**Description**: User would be able to view all product details on this page. Login will not be required to view the product details. User will be able to check the shipping availability by entering PIN code. User would be able to view following details about the product on product detail page: Product title, Thumbnail image, Product images, Product description, Price, Sizes/colors, Ratings & reviews. User will be able to add the product to his shopping cart. User will also be able to add the product to wishlist. User will be able to share product on social media. User will not be able to add the product to wishlist without login.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer, Visitor

---

## Shopping Features

### REQ-006: Wishlist
**Description**: Buyer will need to get registered and login into website to maintain his list of items in wishlist. Buyer will be able to view/add/delete products added into his wishlist. User will be able to proceed for checkout process of items available in wishlist.
**Priority**: High
**Type**: Functional
**Affected Roles**: Buyer

### REQ-007: Shopping Cart
**Description**: The products can be added into shopping cart from the product detail page. User is required to get register and login to manage the items in his shopping cart. User will be able to add items/remove items/update quantity of items in shopping cart. User will be able to proceed for checkout of any items/all items available in shopping cart. User will be able to view item price, sub-total and total price of the items available in shopping cart.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

---

## Checkout and Payment

### REQ-008: Checkout and Payment
**Description**: Payment and checkout process of the items selected from the shopping cart will be considered for placing the orders. Buyer is required to login into website for checkout and payment. Buyer will required to enter billing and shipping address before checkout and payment. Buyer will be required to select payment method for order payment: Credit card/debit card, Net banking. Buyer will be able to view the order summary on this page. Order summary will show following details: Item total, Sub-total, Shipping cost, Tax, Order total. Buyers will be able to receive email notifications for the orders status update.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

---

## Social and Engagement Features

### REQ-009: Social Media Sharing
**Description**: User will be able to share product on social media. Login is not mandatory to share products on social media.
**Priority**: Low
**Type**: Functional
**Affected Roles**: Buyer, Visitor

### REQ-011: Ratings and Reviews
**Description**: User will be able to give ratings and review to the items which he has ordered in past/recently. User will be able post rating and review only for the products which he has ordered from the website. Login and registration will be mandatory for the user to post ratings and review.
**Priority**: High
**Type**: Functional
**Affected Roles**: Buyer

---

## Buyer Account Management

### REQ-010: My Account
**Description**: Buyers will be able to manage their following details from account section: Profile details (email, phone number), Change password, Addresses. Buyer will be able to access below sections from My account: My Orders, MY wishlist, shopping cart, Ratings and reviews, Logout.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

### REQ-012: Order History
**Description**: Buyers will be able to view the orders list i.e. orders placed by the buyer on past. User will be able to view all details about the orders with total amount paid, shipping address, items quantity, price per unit etc. User will be able to reorder the items which are shown in the order details. User will be able to track his current orders from my orders section.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Buyer

---

## Customer Support

### REQ-013: Contact Support
**Description**: Buyers will be able to contact support team via email regarding any queries/complaints by simply posting name, email, contact number and message to the admin. Admin will be able to receive an email regarding complaint details posted by buyer.
**Priority**: High
**Type**: Functional
**Affected Roles**: Buyer, Admin

---

## Admin Authentication and Dashboard

### REQ-014: Admin Login
**Description**: The admin will be able to login to the admin panel. The admin will be asked to enter the user name and password in the given field. Reset password option for the admin to reset password in case of forgot password.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-015: Dashboard
**Description**: Admin user will be able to view following information on dashboard: Total no. of active and inactive registered buyers, Total no. of Products uploaded on website, Total Revenue: today/this month.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin Customer Management

### REQ-016: Buyers Management
**Description**: Admin user will be able to view/edit/active/inactive buyers account information from this section. Admin user will be able to view all detail of the buyer's account like profile details, address, orders, wishlist, items in cart.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin Order Management

### REQ-017: Orders Management
**Description**: Admin user will be able to view list of all orders placed by the buyers on website with current status of each order. Admin user will be able to view/edit order details. Admin user will be able to update the status of order placed by the buyer. Status of the orders will be as below: Open, Confirmed, In process, Shipped, Delivered. Admin user will be responsible for shipment of orders placed by the buyers. Admin user will be able to maintain the below shipment details into system for each order: Shipping carrier, Tracking ID, Current status of shipment, Delivery location/address, Shipping cost.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin Product Management

### REQ-018: Product Categories Management
**Description**: Admin user will be able add/edit/active/inactive product categories and sub-categories from this section. User will be able to add products under these categories & sub-categories from the product management section.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-019: Products Management
**Description**: Admin user will be able to Add/Edit/Active/Inactive products in catalog from this section. Admin user will also be able to manage following information of the products: Product name, Images, Description, Keywords, Variations (color, size).
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin Payment Management

### REQ-020: Payment Management
**Description**: Ability for the admin to view/edit payment information i.e. bank account details to receive orders payments from buyers. Admin user will be able to view payment status of each order placed by the buyers. Stripe payment gateway will be used for online payment gateway integration.
**Priority**: Medium
**Type**: Functional
**Affected Roles**: Admin

---

## Admin Content and Moderation

### REQ-021: Ratings and Review Management
**Description**: Admin user will be able to approve/reject ratings and reviews posted by the buyers for products.
**Priority**: Medium
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-024: CMS Management
**Description**: Admin user will be able to edit the content for below CMS pages: About us, Contact us, Privacy policy, Terms and conditions.
**Priority**: Critical
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-025: Email Management
**Description**: Admin user will be able to add/edit/delete content for emails to be sent to buyers regarding new product launch, offers, and promotions.
**Priority**: Medium
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-026: Complaints and Feedbacks
**Description**: Admin user will be able to view queries/complaints/feedbacks received from the buyers. Admin will also receive an email regarding the feedback/complaints and queries sent by the buyers.
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin Reporting and Analytics

### REQ-022: Statistics and Reports
**Description**: User will be able to view the following reports in system: Products uploaded (Date: From-To, Month, Year), Revenue/total sale (Today, Current week, Date: From-To, Month, Year). Admin user will be able to export reports into pdf and excel format.
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Admin System Management

### REQ-023: System Users Management
**Description**: Admin user will be able to create/edit/delete/active/inactive sub-users to operate the various sectional operations in system.
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

### REQ-027: Roles Management
**Description**: Ability to add/edit/delete/active/inactive sub-admin users with role based access.
**Priority**: High
**Type**: Functional
**Affected Roles**: Admin, Sub-Admin

---

## Non-Functional Requirements

### REQ-028: Scalability
**Description**: The website repository shall accommodate up to 100 users concurrently.
**Priority**: Critical
**Type**: Performance
**Affected Roles**: All Users

### REQ-029: Performance
**Description**: Web pages should not take more than 30 seconds to load in good speed of internet.
**Priority**: Critical
**Type**: Performance
**Affected Roles**: All Users

### REQ-030: Reliability
**Description**: Web pages should not get broken and display page not found error if page is not available.
**Priority**: High
**Type**: Non-Functional
**Affected Roles**: All Users

### REQ-031: Security
**Description**: SSL security and encryption for online payments.
**Priority**: Critical
**Type**: Security
**Affected Roles**: Buyer, Admin

---

## Requirements Summary

**Total Requirements**: 31
- **Functional Requirements**: 27 (REQ-001 to REQ-027)
- **Non-Functional Requirements**: 4 (REQ-028 to REQ-031)

**Priority Breakdown**:
- **Critical**: 19 requirements
- **High**: 8 requirements
- **Medium**: 3 requirements
- **Low**: 1 requirement

**Type Breakdown**:
- **Functional**: 27 requirements
- **Performance**: 2 requirements
- **Security**: 1 requirement
- **Non-Functional**: 1 requirement

**Role Coverage**:
- **Buyer**: 13 dedicated requirements
- **Admin/Sub-Admin**: 14 dedicated requirements
- **Visitor**: 3 requirements (guest access)
- **All Users**: 4 non-functional requirements

**Source Mapping**:
- FR-001 → REQ-001
- FR-002 → REQ-002
- FR-003 → REQ-003
- FR-004 → REQ-004
- FR-005 → REQ-005
- FR-006 → REQ-006
- FR-007 → REQ-007
- FR-008 → REQ-008
- FR-009 → REQ-009
- FR-010 → REQ-010
- FR-011 → REQ-011
- FR-012 → REQ-012
- FR-013 → REQ-013
- FR-014 → REQ-014
- FR-015 → REQ-015
- FR-016 → REQ-016
- FR-017 → REQ-017
- FR-018 → REQ-018
- FR-019 → REQ-019
- Payment Management (from FR-017 rationale) → REQ-020
- FR-020 → REQ-021
- FR-021 → REQ-022
- FR-022 → REQ-023
- FR-023 → REQ-024 (CMS)
- FR-024 → REQ-025 (Email, originally FR-025)
- FR-025 → REQ-026 (Complaints, originally FR-026)
- FR-026 → REQ-027 (Roles, originally FR-023)
- NFR-001 → REQ-028
- NFR-002 → REQ-029
- NFR-003 → REQ-030
- NFR-004 → REQ-031

**Note**: Requirements extracted exactly as documented in source BRD. No additional requirements derived. Minor renumbering applied for consistency (REQ-001 through REQ-031 sequential format).
