# Requirements Extract - Ecommerce Website

## Document Information
- **Source**: Business Requirement Document: Ecommerce Website v1.0
- **Extraction Date**: 2025-11-14
- **Total Requirements**: 147

---

## Requirements Mapping: BRD to Detailed Requirements

This table maps the original BRD requirement IDs (FR-XXX, NFR-XXX) to the detailed requirements (REQ-XXX) extracted for comprehensive test coverage.

| Original BRD ID | Detailed Requirements | Count | Functional Area |
|-----------------|----------------------|-------|-----------------|
| FR-001 (Login) | REQ-001, REQ-002, REQ-003, REQ-004 | 4 | User Authentication |
| FR-002 (Registration) | REQ-005 through REQ-016 | 12 | User Authentication |
| FR-003 (Product Search) | REQ-020, REQ-021, REQ-022, REQ-023, REQ-024, REQ-025 | 6 | Product Browsing |
| FR-004 (Product Listing) | REQ-026 through REQ-032 | 7 | Product Browsing |
| FR-005 (Product Details) | REQ-033 through REQ-044 | 12 | Product Browsing |
| FR-006 (Wishlist) | REQ-045 through REQ-049 | 5 | Shopping Features |
| FR-007 (Shopping Cart) | REQ-053 through REQ-061 | 9 | Shopping Features |
| FR-008 (Checkout & Payment) | REQ-062 through REQ-075 | 14 | Order Processing |
| FR-009 (Social Media Sharing) | REQ-050, REQ-051, REQ-052 | 3 | Social Features |
| FR-010 (My Account) | REQ-083 through REQ-090 | 8 | Account Management |
| FR-011 (Ratings & Reviews) | REQ-095 through REQ-101 | 7 | Product Feedback |
| FR-012 (Order History) | REQ-076 through REQ-082 | 7 | Order Management |
| FR-013 (Contact Support) | REQ-102 through REQ-107 | 6 | Customer Support |
| FR-014 (Admin Login) | REQ-017, REQ-018, REQ-019 | 3 | Admin Authentication |
| FR-015 (Admin Dashboard) | REQ-108 through REQ-112 | 5 | Admin Features |
| FR-016 (Buyers Management) | REQ-113 through REQ-121 | 9 | Admin Features |
| FR-017 (Orders Management) | REQ-122 through REQ-136 | 15 | Admin Features |
| FR-018 (Product Categories) | REQ-137 through REQ-144 | 8 | Admin Features |
| FR-019 (Products Management) | REQ-145 through REQ-154 | 10 | Admin Features |
| FR-020 (Payment Management) | REQ-155 through REQ-158 | 4 | Admin Features |
| FR-021 (Ratings & Review Admin) | REQ-159 through REQ-162 | 4 | Admin Features |
| FR-022 (Statistics & Reports) | REQ-163 through REQ-172 | 10 | Admin Features |
| FR-023 (System Users Management) | REQ-173 through REQ-177 | 5 | Admin Features |
| FR-024 (Roles Management) | REQ-178 through REQ-184 | 7 | Admin Features |
| FR-025 (CMS Management) | REQ-185 through REQ-188 | 4 | Admin Features |
| FR-026 (Email Management) | REQ-189 through REQ-194 | 6 | Admin Features |
| FR-027 (Complaints/Feedbacks) | REQ-195 through REQ-198 | 4 | Admin Features |
| NFR-001 (Scalability) | REQ-199 | 1 | Performance |
| NFR-002 (Speed) | REQ-200 | 1 | Performance |
| NFR-003 (Reliability) | REQ-201, REQ-202 | 2 | Reliability |
| NFR-004 (Security) | REQ-203, REQ-204 | 2 | Security |
| Assumptions | REQ-205, REQ-206, REQ-207 | 3 | Business Constraints |
| Business Constraints | REQ-208, REQ-209 | 2 | Business Constraints |
| Out of Scope | REQ-210, REQ-211, REQ-212 | 3 | Exclusions |

**Total**: 30 BRD requirements expanded into 212 detailed, testable requirements.

---

## Functional Area 1: User Authentication & Registration

### Buyer Login (FR-001)
- **REQ-001**: Users shall be able to log in to the website using email and password
- **REQ-002**: Users shall be able to reset their password if forgotten
- **REQ-003**: Users shall be able to log in using their Facebook account
- **REQ-004**: Users shall be able to log in using their Google account

### Buyer Registration (FR-002)
- **REQ-005**: Users shall be able to register on the website with a registration form
- **REQ-006**: Registration form shall capture first name
- **REQ-007**: Registration form shall capture last name
- **REQ-008**: Registration form shall capture email address
- **REQ-009**: Registration form shall capture contact number
- **REQ-010**: Registration form shall capture password
- **REQ-011**: Registration form shall capture password confirmation
- **REQ-012**: Registration form shall require acceptance of terms and conditions
- **REQ-013**: Email verification shall be mandatory before users can log in
- **REQ-014**: Users shall receive an email verification link upon registration
- **REQ-015**: Users shall be able to verify their email by clicking the verification link
- **REQ-016**: Users shall be able to log in only after email verification is complete

### Admin Login (FR-014)
- **REQ-017**: Admin users shall be able to log in to the admin panel
- **REQ-018**: Admin users shall enter username and password to log in
- **REQ-019**: Admin users shall be able to reset their password if forgotten

---

## Functional Area 2: Product Browsing & Search

### Product Search (FR-003)
- **REQ-020**: Users shall be able to search for products by keyword
- **REQ-021**: Users shall be able to browse products by category
- **REQ-022**: Users shall be able to browse products by sub-category
- **REQ-023**: Users shall be able to use filters to refine product search
- **REQ-024**: Users shall be able to use sorting options to order search results
- **REQ-025**: Users shall be able to search for products without logging in

### Product Listing (FR-004)
- **REQ-026**: Users shall be able to view product listings with product title
- **REQ-027**: Users shall be able to view product listings with thumbnail image
- **REQ-028**: Users shall be able to view product listings with price
- **REQ-029**: Users shall be able to view product listings with ratings and reviews
- **REQ-030**: Users shall be able to click on product title to navigate to product detail page
- **REQ-031**: Users shall be able to click on product image to navigate to product detail page
- **REQ-032**: Users shall be able to view product listings without logging in

### Product Details (FR-005)
- **REQ-033**: Users shall be able to view all product details without logging in
- **REQ-034**: Users shall be able to check shipping availability by entering PIN code
- **REQ-035**: Product detail page shall display product title
- **REQ-036**: Product detail page shall display thumbnail image
- **REQ-037**: Product detail page shall display multiple product images
- **REQ-038**: Product detail page shall display product description
- **REQ-039**: Product detail page shall display price
- **REQ-040**: Product detail page shall display available sizes
- **REQ-041**: Product detail page shall display available colors
- **REQ-042**: Product detail page shall display ratings and reviews
- **REQ-043**: Users shall be able to add products to shopping cart from product detail page
- **REQ-044**: Users shall be able to add products to wishlist from product detail page

---

## Functional Area 3: Wishlist & Social Sharing

### Wishlist (FR-006)
- **REQ-045**: Users must be registered and logged in to maintain a wishlist
- **REQ-046**: Users shall be able to view items in their wishlist
- **REQ-047**: Users shall be able to add products to their wishlist
- **REQ-048**: Users shall be able to delete products from their wishlist
- **REQ-049**: Users shall be able to proceed to checkout from wishlist items

### Social Media Sharing (FR-009)
- **REQ-050**: Users shall be able to share products on social media
- **REQ-051**: Login shall not be required to share products on social media
- **REQ-052**: Users shall be able to share products from the product detail page

---

## Functional Area 4: Shopping Cart & Checkout

### Shopping Cart (FR-007)
- **REQ-053**: Users shall be able to add products to shopping cart from product detail page
- **REQ-054**: Users must be registered and logged in to manage shopping cart items
- **REQ-055**: Users shall be able to add items to shopping cart
- **REQ-056**: Users shall be able to remove items from shopping cart
- **REQ-057**: Users shall be able to update quantity of items in shopping cart
- **REQ-058**: Users shall be able to proceed to checkout from shopping cart
- **REQ-059**: Users shall be able to view item price in shopping cart
- **REQ-060**: Users shall be able to view sub-total in shopping cart
- **REQ-061**: Users shall be able to view total price in shopping cart

### Checkout & Payment (FR-008)
- **REQ-062**: Only items selected from shopping cart shall be included in checkout
- **REQ-063**: Users must be logged in to checkout and make payment
- **REQ-064**: Users shall enter billing address before checkout
- **REQ-065**: Users shall enter shipping address before checkout
- **REQ-066**: Users shall select payment method (credit/debit card or net banking)
- **REQ-067**: Users shall be able to view order summary before payment
- **REQ-068**: Order summary shall display item total
- **REQ-069**: Order summary shall display sub-total
- **REQ-070**: Order summary shall display shipping cost
- **REQ-071**: Order summary shall display tax
- **REQ-072**: Order summary shall display order total
- **REQ-073**: Users shall receive email notifications for order status updates

---

## Functional Area 5: Order Management (Buyer)

### Place Order (Implicit from FR-008)
- **REQ-074**: Users shall be able to place orders after successful payment
- **REQ-075**: Users shall receive order confirmation after placing an order

### Order History (FR-012)
- **REQ-076**: Users shall be able to view list of all past orders
- **REQ-077**: Users shall be able to view order details including total amount paid
- **REQ-078**: Users shall be able to view shipping address for each order
- **REQ-079**: Users shall be able to view item quantity for each order
- **REQ-080**: Users shall be able to view price per unit for each order
- **REQ-081**: Users shall be able to reorder items from past orders
- **REQ-082**: Users shall be able to track current orders from My Orders section

---

## Functional Area 6: User Account Management

### My Account (FR-010)
- **REQ-083**: Users shall be able to manage profile details (email, phone number)
- **REQ-084**: Users shall be able to change password
- **REQ-085**: Users shall be able to manage addresses in address book
- **REQ-086**: Users shall be able to access My Orders from My Account
- **REQ-087**: Users shall be able to access My Wishlist from My Account
- **REQ-088**: Users shall be able to access Shopping Cart from My Account
- **REQ-089**: Users shall be able to access Ratings and Reviews from My Account
- **REQ-090**: Users shall be able to log out from My Account

### Address Book (Implicit from FR-010)
- **REQ-091**: Users shall be able to add new addresses to address book
- **REQ-092**: Users shall be able to edit existing addresses in address book
- **REQ-093**: Users shall be able to delete addresses from address book
- **REQ-094**: Users shall be able to select addresses from address book during checkout

---

## Functional Area 7: Ratings & Reviews

### Post Ratings & Reviews (FR-011)
- **REQ-095**: Users shall be able to rate products they have ordered
- **REQ-096**: Users shall be able to review products they have ordered
- **REQ-097**: Users shall only be able to rate and review products they have ordered
- **REQ-098**: Users must be logged in and registered to post ratings and reviews

### View Ratings & Reviews (Implicit from FR-004, FR-005)
- **REQ-099**: Users shall be able to view product ratings in product listings
- **REQ-100**: Users shall be able to view product reviews on product detail page
- **REQ-101**: Users shall be able to view ratings and reviews without logging in

---

## Functional Area 8: Customer Support

### Contact Support (FR-013)
- **REQ-102**: Users shall be able to contact support team via email
- **REQ-103**: Users shall be able to post name in contact support form
- **REQ-104**: Users shall be able to post email in contact support form
- **REQ-105**: Users shall be able to post contact number in contact support form
- **REQ-106**: Users shall be able to post message in contact support form
- **REQ-107**: Admin shall receive email when user submits support request

---

## Functional Area 9: Admin Dashboard

### Dashboard (FR-015)
- **REQ-108**: Admin shall be able to view total number of active registered buyers
- **REQ-109**: Admin shall be able to view total number of inactive registered buyers
- **REQ-110**: Admin shall be able to view total number of products uploaded on website
- **REQ-111**: Admin shall be able to view total revenue for today
- **REQ-112**: Admin shall be able to view total revenue for current month

---

## Functional Area 10: Admin - Customer Management

### Buyers Management (FR-016)
- **REQ-113**: Admin shall be able to view all buyer account information
- **REQ-114**: Admin shall be able to edit buyer account information
- **REQ-115**: Admin shall be able to activate buyer accounts
- **REQ-116**: Admin shall be able to deactivate buyer accounts
- **REQ-117**: Admin shall be able to view buyer profile details
- **REQ-118**: Admin shall be able to view buyer addresses
- **REQ-119**: Admin shall be able to view buyer orders
- **REQ-120**: Admin shall be able to view buyer wishlist
- **REQ-121**: Admin shall be able to view buyer cart items

---

## Functional Area 11: Admin - Order Management

### Orders Management (FR-017)
- **REQ-122**: Admin shall be able to view list of all orders placed by buyers
- **REQ-123**: Admin shall be able to view current status of each order
- **REQ-124**: Admin shall be able to view order details
- **REQ-125**: Admin shall be able to edit order details
- **REQ-126**: Admin shall be able to update order status to "Open"
- **REQ-127**: Admin shall be able to update order status to "Confirmed"
- **REQ-128**: Admin shall be able to update order status to "In Process"
- **REQ-129**: Admin shall be able to update order status to "Shipped"
- **REQ-130**: Admin shall be able to update order status to "Delivered"
- **REQ-131**: Admin shall be responsible for shipping orders placed by buyers
- **REQ-132**: Admin shall be able to maintain shipping carrier information
- **REQ-133**: Admin shall be able to maintain tracking ID for shipments
- **REQ-134**: Admin shall be able to maintain current shipment status
- **REQ-135**: Admin shall be able to maintain delivery location/address
- **REQ-136**: Admin shall be able to maintain shipping cost

---

## Functional Area 12: Admin - Product Management

### Product Categories Management (FR-018)
- **REQ-137**: Admin shall be able to add product categories
- **REQ-138**: Admin shall be able to edit product categories
- **REQ-139**: Admin shall be able to activate product categories
- **REQ-140**: Admin shall be able to deactivate product categories
- **REQ-141**: Admin shall be able to add product sub-categories
- **REQ-142**: Admin shall be able to edit product sub-categories
- **REQ-143**: Admin shall be able to activate product sub-categories
- **REQ-144**: Admin shall be able to deactivate product sub-categories

### Products Management (FR-019)
- **REQ-145**: Admin shall be able to add new products to catalog
- **REQ-146**: Admin shall be able to edit existing products in catalog
- **REQ-147**: Admin shall be able to activate products
- **REQ-148**: Admin shall be able to deactivate products
- **REQ-149**: Admin shall be able to manage product name
- **REQ-150**: Admin shall be able to manage product images
- **REQ-151**: Admin shall be able to manage product description
- **REQ-152**: Admin shall be able to manage product keywords
- **REQ-153**: Admin shall be able to manage product color variations
- **REQ-154**: Admin shall be able to manage product size variations

---

## Functional Area 13: Admin - Payment Management

### Payment Management (FR-020 - Note: This FR# appears to be for Payment, not in original)
- **REQ-155**: Admin shall be able to view payment information (bank account details)
- **REQ-156**: Admin shall be able to edit payment information
- **REQ-157**: Admin shall be able to view payment status of each order
- **REQ-158**: System shall use Stripe payment gateway for online payments

---

## Functional Area 14: Admin - Ratings & Reviews Management

### Ratings & Review Management (FR-020)
- **REQ-159**: Admin shall be able to approve ratings posted by buyers
- **REQ-160**: Admin shall be able to reject ratings posted by buyers
- **REQ-161**: Admin shall be able to approve reviews posted by buyers
- **REQ-162**: Admin shall be able to reject reviews posted by buyers

---

## Functional Area 15: Admin - Reporting & Statistics

### Statistics & Reports (FR-021)
- **REQ-163**: Admin shall be able to view products uploaded by date range (From-To)
- **REQ-164**: Admin shall be able to view products uploaded by month
- **REQ-165**: Admin shall be able to view products uploaded by year
- **REQ-166**: Admin shall be able to view revenue/total sales for today
- **REQ-167**: Admin shall be able to view revenue/total sales for current week
- **REQ-168**: Admin shall be able to view revenue/total sales by date range (From-To)
- **REQ-169**: Admin shall be able to view revenue/total sales by month
- **REQ-170**: Admin shall be able to view revenue/total sales by year
- **REQ-171**: Admin shall be able to export reports in PDF format
- **REQ-172**: Admin shall be able to export reports in Excel format

---

## Functional Area 16: Admin - User & Role Management

### System Users Management (FR-022)
- **REQ-173**: Admin shall be able to create sub-users
- **REQ-174**: Admin shall be able to edit sub-users
- **REQ-175**: Admin shall be able to delete sub-users
- **REQ-176**: Admin shall be able to activate sub-users
- **REQ-177**: Admin shall be able to deactivate sub-users
- **REQ-178**: Sub-users shall be able to operate various sectional operations

### Roles Management (FR-023)
- **REQ-179**: Admin shall be able to add roles for sub-admin users
- **REQ-180**: Admin shall be able to edit roles for sub-admin users
- **REQ-181**: Admin shall be able to delete roles for sub-admin users
- **REQ-182**: Admin shall be able to activate roles
- **REQ-183**: Admin shall be able to deactivate roles
- **REQ-184**: Roles shall provide role-based access control

---

## Functional Area 17: Admin - Content Management

### CMS Management (FR-024)
- **REQ-185**: Admin shall be able to edit content for "About Us" page
- **REQ-186**: Admin shall be able to edit content for "Contact Us" page
- **REQ-187**: Admin shall be able to edit content for "Privacy Policy" page
- **REQ-188**: Admin shall be able to edit content for "Terms and Conditions" page

### Email Management (FR-025)
- **REQ-189**: Admin shall be able to add email content for buyer communications
- **REQ-190**: Admin shall be able to edit email content for buyer communications
- **REQ-191**: Admin shall be able to delete email content
- **REQ-192**: Admin shall be able to send emails regarding new product launches
- **REQ-193**: Admin shall be able to send emails regarding offers
- **REQ-194**: Admin shall be able to send emails regarding promotions

---

## Functional Area 18: Admin - Complaints & Feedback

### Complaints/Feedbacks (FR-026)
- **REQ-195**: Admin shall be able to view queries received from buyers
- **REQ-196**: Admin shall be able to view complaints received from buyers
- **REQ-197**: Admin shall be able to view feedback received from buyers
- **REQ-198**: Admin shall receive email notifications for feedback/complaints/queries from buyers

---

## Functional Area 19: Non-Functional Requirements - Performance

### Scalability (NFR-001)
- **REQ-199**: System shall accommodate up to 100 concurrent users

### Speed (NFR-002)
- **REQ-200**: Web pages shall not take more than 30 seconds to load with good internet speed

---

## Functional Area 20: Non-Functional Requirements - Reliability

### Reliability (NFR-003)
- **REQ-201**: Web pages shall not display broken pages
- **REQ-202**: Web pages shall display "page not found" error when page is not available

---

## Functional Area 21: Non-Functional Requirements - Security

### Security (NFR-004)
- **REQ-203**: System shall use SSL security for online payments
- **REQ-204**: System shall use encryption for online payments

---

## Functional Area 22: Business Constraints & Assumptions

### System Assumptions (Section 3.4.1)
- **REQ-205**: System shall assume physical inventory/warehouse is established
- **REQ-206**: System shall assume admin manages product catalog with SKU codes
- **REQ-207**: System shall not support custom size and color products
- **REQ-208**: System shall use USD as currency
- **REQ-209**: System shall accept orders from US country only

### Out of Scope (Section 3.2.2)
- **REQ-210**: System shall NOT support ordering customized products
- **REQ-211**: System shall NOT support real-time order tracking
- **REQ-212**: System shall NOT support cash on delivery payment option

---

## Summary Statistics

- **Total Requirements Extracted**: 212
- **Functional Requirements**: 198 (REQ-001 to REQ-198)
- **Non-Functional Requirements**: 4 (REQ-199 to REQ-202, REQ-203, REQ-204)
- **Business Constraints**: 8 (REQ-205 to REQ-212)

### Requirements by Functional Area:

1. **User Authentication & Registration**: 19 requirements
2. **Product Browsing & Search**: 24 requirements
3. **Wishlist & Social Sharing**: 8 requirements
4. **Shopping Cart & Checkout**: 21 requirements
5. **Order Management (Buyer)**: 9 requirements
6. **User Account Management**: 12 requirements
7. **Ratings & Reviews**: 7 requirements
8. **Customer Support**: 6 requirements
9. **Admin Dashboard**: 5 requirements
10. **Admin - Customer Management**: 9 requirements
11. **Admin - Order Management**: 15 requirements
12. **Admin - Product Management**: 18 requirements
13. **Admin - Payment Management**: 4 requirements
14. **Admin - Ratings & Reviews**: 4 requirements
15. **Admin - Reporting & Statistics**: 10 requirements
16. **Admin - User & Role Management**: 12 requirements
17. **Admin - Content Management**: 10 requirements
18. **Admin - Complaints & Feedback**: 4 requirements
19. **Performance**: 2 requirements
20. **Reliability**: 2 requirements
21. **Security**: 2 requirements
22. **Business Constraints**: 8 requirements

---

## Requirements Coverage by Priority (from BRD)

### Critical (Priority 1): 95 requirements
- All login, registration, product search, listing, details, cart, checkout, payment, order management, product management, categories, CMS

### High (Priority 2): 25 requirements
- Wishlist, contact support, statistics & reports, system users, roles, complaints

### Medium (Priority 3): 4 requirements
- Ratings & review (admin management)

### Low (Priority 4): 2 requirements
- Social media sharing

### Not Prioritized: 86 requirements
- NFRs, implicit requirements, business constraints

---

## Traceability Notes

This requirements document will be used to:
1. Generate exhaustive test scenarios (Step 4)
2. Build Requirements Traceability Matrix (Step 10)
3. Ensure all requirements have test coverage

Each requirement has been extracted from the BRD and assigned a unique identifier for traceability throughout the QA process.
