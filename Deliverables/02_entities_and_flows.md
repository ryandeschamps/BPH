# Entities and Flows
## Ecommerce Website - Online Apparels Shopping Platform

**Source Document**: Business Requirements Document (BRD) v1.0, June 2019
**Extraction Date**: November 15, 2025

---

## 1. User Roles (Entities)

### 1.1 Visitor (Guest User)
**Description**: Unauthenticated users browsing the website
**Capabilities**:
- Search for products using keyword and category search
- View product descriptions
- View product ratings and reviews
- Share products on social media
- Check shipping availability by PIN code
- Check product variations (color, size)
- Contact support

**Restrictions**:
- Cannot add products to wishlist
- Cannot add products to cart (requires login per REQ-007)
- Cannot checkout or place orders
- Cannot post ratings/reviews

**Count**: Unlimited (open web access)

### 1.2 Buyer (Registered Customer)
**Description**: Registered and authenticated users who can purchase products
**Capabilities**:
- All Visitor capabilities PLUS:
- Customer login and registration
- Search products by keyword, categories & sub-categories
- View product listing with sorting and filter options
- Add products to wishlist
- Manage shopping cart
- Checkout and make payments
- Post ratings and reviews (only for purchased products)
- View order history
- Track orders
- Manage account settings (profile, addresses, password)
- Contact support

**Authentication Methods**:
- Email/password
- Facebook OAuth
- Google OAuth

**Data Attributes**:
- First name
- Last name
- Email address (unique, verified)
- Contact number
- Password (encrypted)
- Account status (active/inactive)
- Registration date
- Email verification status

**Count**: Variable (business goal: grow customer base)

### 1.3 Admin / Business Owner
**Description**: Primary system administrator with full access
**Capabilities**:
- Login to admin panel (username/password)
- View dashboard with business metrics
- Manage customers (view/edit/activate/deactivate)
- Manage products (add/edit/activate/deactivate)
- Manage product categories and sub-categories
- Manage orders and update order status
- Manage shipping and shipment tracking
- Manage payments and view payment status
- Manage CMS pages
- Approve/reject product ratings and reviews
- View statistics and reports (export to PDF/Excel)
- Manage roles and permissions
- Create/manage sub-admin users
- View customer complaints and feedback

**Data Attributes**:
- Username
- Password (encrypted)
- Full access permissions
- Contact information

**Count**: 1 primary owner

### 1.4 Sub-Admin Users
**Description**: Limited-access admin users with role-based permissions
**Capabilities**:
- Subset of admin capabilities based on assigned role
- Possible roles (inferred):
  - Content Manager (CMS, email templates)
  - Order Fulfillment Manager (orders, shipping)
  - Customer Service (buyer management, complaints)
  - Product Manager (products, categories)
  - Report Viewer (statistics, analytics)

**Data Attributes**:
- Username
- Password (encrypted)
- Assigned role/permissions
- Created by admin
- Status (active/inactive)

**Count**: Variable (as needed by business)

---

## 2. System Components (Technical Entities)

### 2.1 Frontend Website
**Description**: Customer-facing ecommerce application
**Technologies**: Web-based (browser access)
**Key Pages/Modules**:
- Home page
- Product listing/search results
- Product detail page
- Shopping cart
- Wishlist
- Checkout and payment
- User registration/login
- My Account dashboard
- Order history
- Order tracking
- Contact support
- CMS pages (About Us, Contact Us, Privacy Policy, Terms & Conditions)

### 2.2 Admin Panel
**Description**: Backend system for business operations
**Access**: Username/password authentication
**Key Modules**:
- Dashboard (metrics and KPIs)
- Buyers management
- Products management
- Categories management
- Orders management
- Payments management
- Shipping management
- Ratings & reviews moderation
- System users and roles management
- CMS content editor
- Email template manager
- Reports and statistics
- Complaints/feedback inbox

### 2.3 Database System
**Description**: Data storage and persistence layer
**Key Data Tables** (inferred):
- Users (buyers, admins, sub-admins)
- Products
- Product_Categories
- Product_Variations (size, color)
- Shopping_Carts
- Wishlists
- Orders
- Order_Items
- Payments
- Shipments
- Addresses
- Ratings_Reviews
- CMS_Pages
- Email_Templates
- System_Logs

---

## 3. Data Objects (Business Entities)

### 3.1 Product
**Description**: Apparel items available for purchase
**Attributes**:
- Product ID (SKU)
- Product name/title
- Description
- Category ID (foreign key)
- Sub-category ID (foreign key)
- Price (USD)
- Images (thumbnail + multiple product images)
- Keywords (for search)
- Variations (size, color)
- Ratings (aggregate score)
- Review count
- Status (active/inactive)
- Created date
- Modified date

**Relationships**:
- Belongs to Category
- Belongs to Sub-category
- Has many Variations
- Has many Ratings/Reviews
- Appears in many Carts
- Appears in many Wishlists
- Appears in many Orders

**Business Rules**:
- No custom sizes/colors (standard variations only)
- SKU managed by admin
- Must have at least one image
- Price in USD only

### 3.2 Category / Sub-Category
**Description**: Product classification hierarchy
**Attributes**:
- Category ID
- Category name
- Parent category ID (for sub-categories)
- Description
- Status (active/inactive)
- Sort order

**Relationships**:
- Has many Products
- Has many Sub-categories (for parent categories)
- Belongs to Parent Category (for sub-categories)

**Examples** (inferred from apparels domain):
- Categories: Men, Women, Kids
- Sub-categories: Shirts, Jeans, T-Shirts, Dresses, Accessories

### 3.3 Shopping Cart
**Description**: Temporary collection of products buyer intends to purchase
**Attributes**:
- Cart ID
- Buyer ID (foreign key)
- Created date
- Modified date
- Cart status (active/converted/abandoned)

**Related Entity - Cart Items**:
- Cart Item ID
- Cart ID
- Product ID
- Product variation (size, color)
- Quantity
- Unit price (at time of add)
- Subtotal

**Business Rules**:
- Requires user login to manage
- Persists across sessions
- Quantity can be updated
- Items can be removed
- Can proceed to checkout

### 3.4 Wishlist
**Description**: Saved products for future purchase consideration
**Attributes**:
- Wishlist ID
- Buyer ID (foreign key)
- Product ID (foreign key)
- Added date

**Relationships**:
- Belongs to Buyer
- Contains Products

**Business Rules**:
- Requires user login
- Products can be added/removed
- Can move items from wishlist to cart
- Can checkout directly from wishlist

### 3.5 Order
**Description**: Confirmed purchase transaction
**Attributes**:
- Order ID (unique)
- Buyer ID (foreign key)
- Order date/time
- Order status (Open, Confirmed, In Process, Shipped, Delivered)
- Billing address
- Shipping address
- Payment method (credit/debit card, net banking)
- Payment status (pending/completed/failed)
- Item total
- Shipping cost
- Tax amount
- Order total
- Shipment tracking ID
- Shipping carrier
- Estimated delivery date
- Actual delivery date

**Related Entity - Order Items**:
- Order Item ID
- Order ID
- Product ID
- Product variation (size, color)
- Quantity
- Unit price
- Subtotal

**Relationships**:
- Belongs to Buyer
- Has many Order Items
- Has one Payment
- Has one Shipment

**Business Rules**:
- Requires completed payment
- Buyer receives email notification for status changes
- Admin manages order status transitions
- Order can be reordered from history

### 3.6 Payment
**Description**: Financial transaction for order
**Attributes**:
- Payment ID
- Order ID (foreign key)
- Payment method (credit card, debit card, net banking)
- Payment gateway (Stripe)
- Transaction ID (from gateway)
- Payment amount
- Payment status (pending/completed/failed/refunded)
- Payment date/time
- Card last 4 digits (if card payment)
- Bank account details (admin's receiving account)

**Relationships**:
- Belongs to Order
- Processed through Payment Gateway (Stripe)

**Business Rules**:
- SSL encryption required
- Stripe payment gateway integration
- Admin can view payment status
- No cash on delivery (out of scope)

### 3.7 Shipment
**Description**: Physical delivery of ordered products
**Attributes**:
- Shipment ID
- Order ID (foreign key)
- Shipping carrier
- Tracking ID
- Shipment status (pending/in_transit/delivered)
- Shipping address
- Shipping cost
- Estimated delivery date
- Actual delivery date
- Delivery notes

**Relationships**:
- Belongs to Order
- Managed by Admin

**Business Rules**:
- US orders only
- Shipping availability checked by PIN code
- Buyer can track shipment status
- Admin maintains shipment details

### 3.8 Address
**Description**: Buyer's billing and shipping locations
**Attributes**:
- Address ID
- Buyer ID (foreign key)
- Address type (billing/shipping)
- Street address
- City
- State
- ZIP/PIN code
- Country (default: USA)
- Phone number
- Is default (boolean)

**Relationships**:
- Belongs to Buyer
- Used in Orders

**Business Rules**:
- Buyer can manage address book
- Multiple addresses allowed per buyer
- PIN code determines shipping availability

### 3.9 Rating and Review
**Description**: Customer feedback on purchased products
**Attributes**:
- Review ID
- Product ID (foreign key)
- Buyer ID (foreign key)
- Order ID (foreign key - proves purchase)
- Rating (numeric score, e.g., 1-5 stars)
- Review text
- Review date
- Status (pending/approved/rejected)
- Approved by (admin user ID)
- Approval date

**Relationships**:
- Belongs to Product
- Created by Buyer
- Moderated by Admin

**Business Rules**:
- Login required to post
- Can only review purchased products
- Admin approval required before display
- Aggregate ratings displayed on product listing/details

---

## 4. External Integrations (System Entities)

### 4.1 Stripe Payment Gateway
**Description**: Third-party payment processing service
**Integration Type**: API
**Purpose**: Process credit/debit card and net banking payments
**Data Exchange**:
- Outbound: Payment amount, order details, customer info
- Inbound: Transaction ID, payment status, confirmation

**Requirements**: REQ-020, REQ-008

### 4.2 Facebook OAuth
**Description**: Social login authentication
**Integration Type**: OAuth 2.0
**Purpose**: Allow users to login using Facebook account
**Data Exchange**:
- Inbound: User profile (name, email)
- Account linking with buyer record

**Requirements**: REQ-001

### 4.3 Google OAuth
**Description**: Social login authentication
**Integration Type**: OAuth 2.0
**Purpose**: Allow users to login using Google account
**Data Exchange**:
- Inbound: User profile (name, email)
- Account linking with buyer record

**Requirements**: REQ-001

### 4.4 Email Service (SMTP)
**Description**: Email notification system
**Purpose**: Send transactional and promotional emails
**Email Types**:
- Registration confirmation / email verification
- Password reset
- Order confirmation
- Order status updates
- Shipment tracking
- Promotional campaigns (admin-managed)
- Contact form submissions

**Requirements**: REQ-002, REQ-008, REQ-013, REQ-025, REQ-026

### 4.5 Social Media Platforms
**Description**: Social sharing integrations
**Platforms** (inferred): Facebook, Twitter, Pinterest, Instagram
**Purpose**: Allow users to share products
**Integration Type**: Social share APIs/widgets

**Requirements**: REQ-009

### 4.6 Shipping Carrier System
**Description**: Logistics and tracking integration
**Purpose**: Shipment tracking and delivery status
**Data Exchange**:
- Outbound: Order details, shipping address
- Inbound: Tracking ID, shipment status updates

**Requirements**: REQ-017

---

## 5. Primary User Flows

### 5.1 Buyer Registration and Login Flow

**Flow BR-001: New Buyer Registration**
```
1. Visitor navigates to Registration page
2. Visitor fills registration form:
   - First name
   - Last name
   - Email address
   - Contact number
   - Password
   - Confirm password
   - Accept terms and conditions checkbox
3. System validates form inputs
4. System creates buyer account (status: unverified)
5. System sends email verification link to registered email
6. Buyer clicks verification link in email
7. System activates buyer account (status: verified)
8. Buyer can now login with email and password
```
**Requirements**: REQ-002
**Entities**: Buyer, Email Service
**Success Criteria**: Account created and email verified

**Flow BR-002: Social Login (Facebook/Google)**
```
1. Visitor clicks "Login with Facebook" or "Login with Google"
2. System redirects to OAuth provider (Facebook/Google)
3. User authorizes app access
4. OAuth provider returns user profile data
5. System checks if email exists in database
   - If exists: Link account and login
   - If new: Create buyer account automatically
6. Buyer logged in and redirected to home/previous page
```
**Requirements**: REQ-001
**Entities**: Buyer, Facebook OAuth, Google OAuth
**Success Criteria**: Successful authentication via social account

**Flow BR-003: Buyer Login**
```
1. Visitor navigates to Login page
2. Visitor enters email and password
3. System validates credentials
4. If valid:
   - System creates session
   - Buyer redirected to home/previous page
5. If invalid:
   - Error message displayed
   - Option to reset password
```
**Requirements**: REQ-001
**Entities**: Buyer
**Success Criteria**: Authenticated session established

**Flow BR-004: Password Reset**
```
1. Visitor clicks "Forgot Password"
2. Visitor enters registered email address
3. System sends password reset link to email
4. Visitor clicks reset link
5. Visitor enters new password and confirms
6. System updates password
7. Visitor redirected to login page
```
**Requirements**: REQ-001
**Entities**: Buyer, Email Service
**Success Criteria**: Password successfully reset

---

### 5.2 Product Discovery and Browsing Flow

**Flow PD-001: Product Search by Keyword**
```
1. User (Visitor or Buyer) enters keyword in search box
2. User submits search
3. System queries product database
4. System displays product listing matching keyword
5. Results include: product title, thumbnail, price, ratings
6. User can apply filters and sorting
7. User clicks product to view details
```
**Requirements**: REQ-003, REQ-004
**Entities**: Product, Category
**Success Criteria**: Relevant products displayed

**Flow PD-002: Browse Products by Category**
```
1. User clicks category/sub-category from navigation
2. System displays all products in selected category
3. Product listing shows: title, thumbnail, price, ratings
4. User can apply filters (size, color, price range)
5. User can sort (price, rating, newest)
6. User clicks product to view details
```
**Requirements**: REQ-003, REQ-004
**Entities**: Product, Category, Sub-Category
**Success Criteria**: Category products displayed correctly

**Flow PD-003: View Product Details**
```
1. User clicks product from listing
2. System displays product detail page:
   - Product title
   - Multiple images (thumbnail + gallery)
   - Price
   - Description
   - Available sizes and colors
   - Aggregate ratings and reviews
3. User can:
   - Check shipping availability (enter PIN code)
   - Select size/color variation
   - Add to cart
   - Add to wishlist (if logged in)
   - Share on social media
4. User scrolls to view customer ratings and reviews
```
**Requirements**: REQ-005
**Entities**: Product, Rating/Review, Address (PIN code)
**Success Criteria**: Complete product information displayed

---

### 5.3 Shopping and Checkout Flow

**Flow SC-001: Add Product to Cart**
```
1. User on product detail page
2. User selects size and color (if applicable)
3. User clicks "Add to Cart"
4. If not logged in:
   - System prompts login/registration
5. If logged in:
   - System adds product to buyer's cart
   - Success message displayed
   - Cart icon updated with item count
```
**Requirements**: REQ-007
**Entities**: Buyer, Shopping Cart, Product
**Success Criteria**: Product added to cart successfully

**Flow SC-002: Manage Shopping Cart**
```
1. Buyer clicks cart icon
2. System displays cart page with items:
   - Product image, name, variation
   - Unit price
   - Quantity (editable)
   - Subtotal
3. Buyer can:
   - Update quantity
   - Remove items
   - Continue shopping
   - Proceed to checkout
4. Cart displays:
   - Item total
   - Subtotal
   - Total price
```
**Requirements**: REQ-007
**Entities**: Shopping Cart, Cart Items
**Success Criteria**: Cart accurately reflects buyer selections

**Flow SC-003: Add Product to Wishlist**
```
1. User on product detail page
2. User clicks "Add to Wishlist"
3. If not logged in:
   - System prompts login/registration
4. If logged in:
   - System adds product to buyer's wishlist
   - Success message displayed
   - User can view wishlist from My Account
```
**Requirements**: REQ-006
**Entities**: Buyer, Wishlist, Product
**Success Criteria**: Product saved to wishlist

**Flow SC-004: Checkout and Payment**
```
1. Buyer clicks "Proceed to Checkout" from cart
2. System verifies buyer is logged in
3. Checkout page displays:
   - Order summary (items, prices, shipping, tax, total)
   - Billing address form
   - Shipping address form (option to use billing address)
   - Payment method selection (credit/debit card or net banking)
4. Buyer enters/selects addresses
5. Buyer selects payment method
6. Buyer reviews order summary
7. Buyer clicks "Place Order"
8. System redirects to payment gateway (Stripe)
9. Buyer enters payment details on Stripe
10. Stripe processes payment
11. If payment successful:
    - System creates order with status "Open"
    - System sends order confirmation email
    - Buyer redirected to order confirmation page
12. If payment failed:
    - Error message displayed
    - Buyer can retry payment
```
**Requirements**: REQ-008, REQ-020
**Entities**: Buyer, Order, Payment, Stripe, Email Service, Address
**Success Criteria**: Order placed and payment confirmed

---

### 5.4 Post-Purchase Flow

**Flow PP-001: View Order History**
```
1. Buyer navigates to My Account > My Orders
2. System displays list of all buyer's orders:
   - Order ID
   - Order date
   - Order total
   - Order status
3. Buyer clicks order to view details:
   - Items ordered (name, quantity, price)
   - Shipping address
   - Payment status
   - Shipment tracking (if shipped)
4. Buyer can:
   - Track order
   - Reorder items
   - Contact support
```
**Requirements**: REQ-012
**Entities**: Buyer, Order, Order Items
**Success Criteria**: Order history accurately displayed

**Flow PP-002: Track Order Shipment**
```
1. Buyer navigates to My Orders
2. Buyer selects order to track
3. System displays:
   - Current order status (Open/Confirmed/In Process/Shipped/Delivered)
   - Shipping carrier
   - Tracking ID
   - Estimated delivery date
4. If shipped:
   - Buyer can click tracking link to carrier website
   - Real-time tracking status available
```
**Requirements**: REQ-012, REQ-017
**Entities**: Order, Shipment
**Success Criteria**: Tracking information available and accurate

**Flow PP-003: Post Rating and Review**
```
1. Buyer navigates to My Account > Ratings and Reviews
2. System displays list of purchased products eligible for review
3. Buyer selects product to review
4. Buyer enters:
   - Rating (1-5 stars)
   - Review text
5. Buyer submits review
6. System saves review with status "Pending"
7. Review awaits admin approval before displaying on product page
```
**Requirements**: REQ-011, REQ-021
**Entities**: Buyer, Product, Rating/Review, Order
**Success Criteria**: Review submitted and pending approval

---

### 5.5 Buyer Account Management Flow

**Flow AM-001: Manage Profile**
```
1. Buyer logs in
2. Buyer navigates to My Account
3. Buyer can view/edit:
   - Profile details (email, phone number)
   - Change password
   - Manage addresses (add/edit/delete/set default)
4. Buyer submits changes
5. System validates and updates data
6. Confirmation message displayed
```
**Requirements**: REQ-010
**Entities**: Buyer, Address
**Success Criteria**: Profile updated successfully

**Flow AM-002: Contact Support**
```
1. User (Visitor or Buyer) navigates to Contact Us page
2. User fills contact form:
   - Name
   - Email
   - Contact number
   - Message
3. User submits form
4. System sends email to admin with contact details
5. System displays confirmation message to user
6. Admin receives email and can respond
```
**Requirements**: REQ-013
**Entities**: Buyer/Visitor, Admin, Email Service
**Success Criteria**: Support request submitted and admin notified

---

### 5.6 Admin Product Management Flow

**Flow APM-001: Create New Product**
```
1. Admin logs into admin panel
2. Admin navigates to Products Management
3. Admin clicks "Add New Product"
4. Admin enters product details:
   - Product name
   - Description
   - SKU code
   - Price (USD)
   - Category and sub-category
   - Keywords
   - Upload images
   - Add variations (sizes, colors)
5. Admin saves product
6. System creates product with status "Active"
7. Product appears on frontend website
```
**Requirements**: REQ-019
**Entities**: Admin, Product, Category, Product Variations
**Success Criteria**: Product created and visible on website

**Flow APM-002: Manage Product Categories**
```
1. Admin navigates to Product Categories Management
2. Admin can:
   - Add new category/sub-category
   - Edit category name/description
   - Activate/deactivate category
   - Delete category (if no products assigned)
3. Admin submits changes
4. System updates category structure
5. Changes reflected in frontend navigation
```
**Requirements**: REQ-018
**Entities**: Admin, Category, Sub-Category
**Success Criteria**: Category structure updated correctly

**Flow APM-003: Edit/Deactivate Product**
```
1. Admin navigates to Products Management
2. Admin searches/filters to find product
3. Admin clicks product to edit
4. Admin can:
   - Update product details
   - Change images
   - Modify variations
   - Activate/deactivate product
5. Admin saves changes
6. System updates product
7. If deactivated:
   - Product hidden from frontend
   - Existing carts retain item (with out-of-stock notice)
```
**Requirements**: REQ-019
**Entities**: Admin, Product
**Success Criteria**: Product updated/deactivated as intended

---

### 5.7 Admin Order Fulfillment Flow

**Flow AOF-001: View and Manage Orders**
```
1. Admin logs into admin panel
2. Admin navigates to Orders Management
3. System displays list of all orders:
   - Order ID
   - Buyer name
   - Order date
   - Order status
   - Order total
4. Admin can filter by status (Open/Confirmed/In Process/Shipped/Delivered)
5. Admin clicks order to view full details
```
**Requirements**: REQ-017
**Entities**: Admin, Order
**Success Criteria**: Orders list displayed accurately

**Flow AOF-002: Update Order Status and Shipment**
```
1. Admin opens order details
2. Admin reviews order items and buyer information
3. Admin updates order status:
   - Open → Confirmed (order verified)
   - Confirmed → In Process (preparing shipment)
   - In Process → Shipped (package dispatched)
   - Shipped → Delivered (delivery confirmed)
4. When status changed to "Shipped":
   - Admin enters shipment details:
     - Shipping carrier
     - Tracking ID
     - Estimated delivery date
5. Admin saves changes
6. System updates order status
7. System sends email notification to buyer
8. Buyer can track shipment from My Orders
```
**Requirements**: REQ-017
**Entities**: Admin, Order, Shipment, Email Service
**Success Criteria**: Order status updated and buyer notified

**Flow AOF-003: Manage Payments**
```
1. Admin navigates to Payment Management or Orders
2. Admin views payment status for each order:
   - Pending
   - Completed
   - Failed
3. Admin can:
   - View transaction details
   - Update bank account information for receiving payments
4. Stripe integration provides payment reconciliation
```
**Requirements**: REQ-020
**Entities**: Admin, Payment, Stripe
**Success Criteria**: Payment information accurate and accessible

---

### 5.8 Admin Customer Management Flow

**Flow ACM-001: Manage Buyers**
```
1. Admin navigates to Buyers Management
2. System displays list of all registered buyers:
   - Name
   - Email
   - Registration date
   - Account status (active/inactive)
3. Admin can search/filter buyers
4. Admin clicks buyer to view details:
   - Profile information
   - Address book
   - Order history
   - Wishlist items
   - Cart items
5. Admin can:
   - Edit buyer information
   - Activate/deactivate account
   - View complete buyer activity
```
**Requirements**: REQ-016
**Entities**: Admin, Buyer, Order, Wishlist, Cart
**Success Criteria**: Buyer information accessible and manageable

---

### 5.9 Admin Content and Moderation Flow

**Flow ACMF-001: Manage CMS Pages**
```
1. Admin navigates to CMS Management
2. System displays list of CMS pages:
   - About Us
   - Contact Us
   - Privacy Policy
   - Terms and Conditions
3. Admin selects page to edit
4. Admin edits content using editor
5. Admin saves changes
6. Updated content appears on frontend website
```
**Requirements**: REQ-024
**Entities**: Admin, CMS Pages
**Success Criteria**: CMS content updated on website

**Flow ACMF-002: Moderate Ratings and Reviews**
```
1. Admin navigates to Ratings & Reviews Management
2. System displays list of pending reviews:
   - Product name
   - Buyer name
   - Rating
   - Review text
   - Submission date
3. Admin reviews content
4. Admin can:
   - Approve review (displays on product page)
   - Reject review (does not display)
5. Admin saves decision
6. If approved:
   - Review appears on product detail page
   - Product aggregate rating updated
```
**Requirements**: REQ-021
**Entities**: Admin, Rating/Review, Product
**Success Criteria**: Reviews moderated and appropriate ones displayed

**Flow ACMF-003: Manage Email Campaigns**
```
1. Admin navigates to Email Management
2. Admin can:
   - Create new email template
   - Edit existing templates
   - Delete unused templates
3. Admin creates promotional email:
   - Subject line
   - Email body content
   - Target audience (all buyers or filtered segment)
4. Admin sends/schedules email
5. System sends emails to selected buyers
```
**Requirements**: REQ-025
**Entities**: Admin, Email Service, Email Templates, Buyers
**Success Criteria**: Promotional emails sent to target audience

---

### 5.10 Admin Reporting and System Management Flow

**Flow ARSM-001: View Dashboard Metrics**
```
1. Admin logs into admin panel
2. Admin lands on Dashboard
3. Dashboard displays:
   - Total active buyers
   - Total inactive buyers
   - Total products uploaded
   - Total revenue (today)
   - Total revenue (this month)
4. Admin can click metrics for detailed reports
```
**Requirements**: REQ-015
**Entities**: Admin, Dashboard
**Success Criteria**: Accurate metrics displayed in real-time

**Flow ARSM-002: Generate and Export Reports**
```
1. Admin navigates to Statistics & Reports
2. Admin selects report type:
   - Products uploaded (by date range, month, year)
   - Revenue/sales (today, current week, date range, month, year)
3. Admin applies filters (date range, category, etc.)
4. System generates report
5. Admin can:
   - View report on screen
   - Export to PDF
   - Export to Excel
6. System downloads report file
```
**Requirements**: REQ-022
**Entities**: Admin, Reports
**Success Criteria**: Accurate reports generated and exported

**Flow ARSM-003: Manage Sub-Admin Users**
```
1. Admin navigates to System Users Management
2. System displays list of sub-admin users
3. Admin can:
   - Create new sub-admin user
   - Edit user details
   - Activate/deactivate user
   - Delete user
   - Assign roles/permissions (via Roles Management)
4. Admin enters user details:
   - Username
   - Password
   - Assigned role
5. Admin saves user
6. Sub-admin can login with credentials
```
**Requirements**: REQ-023, REQ-027
**Entities**: Admin, Sub-Admin, Roles
**Success Criteria**: Sub-admin created with appropriate permissions

**Flow ARSM-004: View Customer Feedback**
```
1. Admin navigates to Complaints/Feedbacks
2. System displays list of customer inquiries from Contact Us form
3. Admin can view:
   - Customer name
   - Email
   - Contact number
   - Message
   - Submission date
4. Admin receives email notification for each new submission
5. Admin can respond via email
```
**Requirements**: REQ-026
**Entities**: Admin, Customer Feedback, Email Service
**Success Criteria**: All customer inquiries accessible and tracked

---

## 6. Entity Count Summary

| Entity Type | Count | Notes |
|-------------|-------|-------|
| **User Roles** | 4 | Visitor, Buyer, Admin, Sub-Admin |
| **System Components** | 3 | Frontend, Admin Panel, Database |
| **Data Objects** | 9 | Product, Category, Cart, Wishlist, Order, Payment, Shipment, Address, Rating/Review |
| **External Integrations** | 6 | Stripe, Facebook OAuth, Google OAuth, Email, Social Media, Shipping Carrier |
| **Total Entities** | 22 | |

## 7. User Flow Count Summary

| Flow Category | Count | Flow IDs |
|---------------|-------|----------|
| **Buyer Registration and Login** | 4 | BR-001 to BR-004 |
| **Product Discovery and Browsing** | 3 | PD-001 to PD-003 |
| **Shopping and Checkout** | 4 | SC-001 to SC-004 |
| **Post-Purchase** | 3 | PP-001 to PP-003 |
| **Buyer Account Management** | 2 | AM-001 to AM-002 |
| **Admin Product Management** | 3 | APM-001 to APM-003 |
| **Admin Order Fulfillment** | 3 | AOF-001 to AOF-003 |
| **Admin Customer Management** | 1 | ACM-001 |
| **Admin Content and Moderation** | 3 | ACMF-001 to ACMF-003 |
| **Admin Reporting and System Management** | 4 | ARSM-001 to ARSM-004 |
| **Total Flows** | 30 | |

---

**Document Status**: Complete
**Next Step**: Step 4 - Derive Test Scenarios based on these entities and flows
