# Entities and Flows - Ecommerce Website

## Document Information
- **Source Document**: BRD v1.0 - Online Apparels Shopping Website
- **Date**: November 13, 2025

---

## 1. KEY ENTITIES

### 1.1 User Entities

#### 1.1.1 Visitor (Guest User)
**Description**: Unauthenticated user browsing the website

**Attributes**:
- Session ID (temporary)
- IP Address
- Browser information

**Capabilities**:
- Search products (keyword, category)
- View product listings
- View product details
- View ratings and reviews
- Check shipping availability by PIN code
- Check product variations (size, color)
- Share products on social media
- Contact support

**Source Requirements**: Section 3.3 User Roles

---

#### 1.1.2 Buyer (Registered Customer)
**Description**: Authenticated user who can make purchases

**Attributes**:
- User ID (unique)
- First name
- Last name
- Email address (unique, verified)
- Contact number
- Password (encrypted)
- Registration date
- Email verification status
- Account status (active/inactive)

**Capabilities**:
- All Visitor capabilities, plus:
- Login/Logout
- Manage profile
- Change password
- Manage address book (billing/shipping addresses)
- Add products to cart
- Add products to wishlist
- Checkout and make payments
- View order history
- Track orders
- Post ratings and reviews
- Manage account settings

**Source Requirements**: FR-001, FR-002, FR-010, Section 3.3

---

#### 1.1.3 Admin User (Business Owner)
**Description**: Primary administrator with full system access

**Attributes**:
- Admin ID (unique)
- Username
- Password (encrypted)
- Role (Admin)
- Permissions (full access)

**Capabilities**:
- Login/Logout
- View dashboard with statistics
- Manage customers (view/edit/activate/deactivate)
- Manage products (create/edit/delete/activate/deactivate)
- Manage product categories and sub-categories
- Manage product catalog
- Manage orders (view/edit/update status)
- Manage shipping details
- Manage payment information
- Manage CMS pages
- Manage ratings and reviews (approve/reject)
- View statistics and reports
- Export reports (PDF, Excel)
- Manage sub-users
- Manage roles and permissions
- View customer complaints/feedback
- Receive email notifications

**Source Requirements**: FR-014 through FR-026, Section 3.3

---

#### 1.1.4 Sub-User (Admin Staff)
**Description**: User with limited administrative access based on assigned role

**Attributes**:
- Sub-user ID (unique)
- Username
- Password (encrypted)
- Assigned role
- Permissions (role-based)
- Status (active/inactive)

**Capabilities**:
- Role-based access to admin functions

**Source Requirements**: FR-022, FR-023

---

### 1.2 Product Entities

#### 1.2.1 Product
**Description**: Apparel item available for purchase

**Attributes**:
- Product ID (unique)
- SKU (Stock Keeping Unit)
- Product name/title
- Description
- Thumbnail image
- Product images (multiple)
- Category ID (foreign key)
- Sub-category ID (foreign key)
- Price (USD)
- Available sizes (array)
- Available colors (array)
- Keywords (for search)
- Status (active/inactive)
- Creation date
- Last modified date
- Average rating
- Review count

**Relationships**:
- Belongs to one Category
- Belongs to one Sub-category (optional)
- Has many Reviews
- Has many Ratings
- Can be in many Carts
- Can be in many Wishlists
- Can be in many Orders

**Source Requirements**: FR-004, FR-005, FR-019

---

#### 1.2.2 Category
**Description**: Product classification/grouping

**Attributes**:
- Category ID (unique)
- Category name
- Description
- Parent category ID (for sub-categories)
- Status (active/inactive)
- Display order

**Relationships**:
- Has many Products
- Has many Sub-categories (self-referential)

**Source Requirements**: FR-018

---

### 1.3 Shopping Entities

#### 1.3.1 Shopping Cart
**Description**: Temporary collection of products selected for purchase

**Attributes**:
- Cart ID (unique)
- User ID (foreign key)
- Created date
- Last modified date

**Relationships**:
- Belongs to one Buyer
- Has many Cart Items

**Source Requirements**: FR-007

---

#### 1.3.2 Cart Item
**Description**: Individual product in shopping cart

**Attributes**:
- Cart Item ID (unique)
- Cart ID (foreign key)
- Product ID (foreign key)
- Selected size
- Selected color
- Quantity
- Unit price
- Subtotal
- Added date

**Source Requirements**: FR-007

---

#### 1.3.3 Wishlist
**Description**: Saved products for future purchase consideration

**Attributes**:
- Wishlist ID (unique)
- User ID (foreign key)
- Created date

**Relationships**:
- Belongs to one Buyer
- Has many Wishlist Items

**Source Requirements**: FR-006

---

#### 1.3.4 Wishlist Item
**Description**: Individual product in wishlist

**Attributes**:
- Wishlist Item ID (unique)
- Wishlist ID (foreign key)
- Product ID (foreign key)
- Added date

**Source Requirements**: FR-006

---

### 1.4 Order Entities

#### 1.4.1 Order
**Description**: Confirmed purchase transaction

**Attributes**:
- Order ID (unique)
- User ID (foreign key)
- Order number (display)
- Order date
- Order status (Open, Confirmed, In Process, Shipped, Delivered)
- Billing address ID (foreign key)
- Shipping address ID (foreign key)
- Item total
- Subtotal
- Shipping cost
- Tax amount
- Order total
- Payment ID (foreign key)
- Payment status
- Created date
- Last modified date

**Relationships**:
- Belongs to one Buyer
- Has many Order Items
- Has one Payment
- Has one Shipment
- Has one Billing Address
- Has one Shipping Address

**Source Requirements**: FR-008, FR-012, FR-017

---

#### 1.4.2 Order Item
**Description**: Individual product within an order

**Attributes**:
- Order Item ID (unique)
- Order ID (foreign key)
- Product ID (foreign key)
- Product name (snapshot)
- Selected size
- Selected color
- Quantity
- Unit price
- Subtotal

**Source Requirements**: FR-008, FR-012

---

### 1.5 Address Entity

#### 1.5.1 Address
**Description**: Billing or shipping address

**Attributes**:
- Address ID (unique)
- User ID (foreign key)
- Address type (billing/shipping)
- Address line 1
- Address line 2
- City
- State
- ZIP/PIN code
- Country (default: USA)
- Is default (boolean)
- Created date

**Relationships**:
- Belongs to one Buyer

**Source Requirements**: FR-008, FR-010

---

### 1.6 Payment Entities

#### 1.6.1 Payment
**Description**: Payment transaction details

**Attributes**:
- Payment ID (unique)
- Order ID (foreign key)
- Payment method (Credit Card, Debit Card, Net Banking)
- Payment gateway (Stripe)
- Transaction ID
- Amount
- Currency (USD)
- Payment status (Pending, Completed, Failed)
- Payment date
- Gateway response

**Relationships**:
- Belongs to one Order

**Source Requirements**: FR-008, FR-020

---

### 1.7 Shipping Entity

#### 1.7.1 Shipment
**Description**: Order shipment tracking information

**Attributes**:
- Shipment ID (unique)
- Order ID (foreign key)
- Shipping carrier
- Tracking ID
- Shipment status
- Shipping address ID (foreign key)
- Shipping cost
- Shipped date
- Estimated delivery date
- Actual delivery date
- Last updated date

**Relationships**:
- Belongs to one Order
- Has one Shipping Address

**Source Requirements**: FR-017

---

### 1.8 Review and Rating Entities

#### 1.8.1 Review
**Description**: Customer product review

**Attributes**:
- Review ID (unique)
- Product ID (foreign key)
- User ID (foreign key)
- Order ID (foreign key) - to verify purchase
- Review text
- Review date
- Status (Pending, Approved, Rejected)
- Approved by (Admin ID)
- Approved date

**Relationships**:
- Belongs to one Product
- Belongs to one Buyer
- Associated with one Order

**Source Requirements**: FR-011, FR-020

---

#### 1.8.2 Rating
**Description**: Numeric product rating

**Attributes**:
- Rating ID (unique)
- Product ID (foreign key)
- User ID (foreign key)
- Order ID (foreign key) - to verify purchase
- Rating value (1-5)
- Rating date
- Status (Pending, Approved, Rejected)

**Relationships**:
- Belongs to one Product
- Belongs to one Buyer
- Associated with one Order

**Source Requirements**: FR-011, FR-020

---

### 1.9 CMS Entity

#### 1.9.1 CMS Page
**Description**: Content management system pages

**Attributes**:
- Page ID (unique)
- Page name/title
- Page slug/URL
- Content (HTML)
- Meta title
- Meta description
- Status (active/inactive)
- Last modified date
- Modified by (Admin ID)

**Types**:
- About Us
- Contact Us
- Privacy Policy
- Terms and Conditions

**Source Requirements**: FR-024

---

### 1.10 Support Entity

#### 1.10.1 Support Request
**Description**: Customer inquiry or complaint

**Attributes**:
- Request ID (unique)
- User ID (foreign key, optional)
- Name
- Email
- Contact number
- Message
- Request date
- Status (Open, In Progress, Resolved)

**Source Requirements**: FR-013, FR-026

---

### 1.11 System Entities

#### 1.11.1 Role
**Description**: User permission role

**Attributes**:
- Role ID (unique)
- Role name
- Description
- Permissions (JSON or array)
- Status (active/inactive)

**Source Requirements**: FR-023

---

#### 1.11.2 Email Template
**Description**: Email content templates

**Attributes**:
- Template ID (unique)
- Template name
- Subject
- Body content
- Variables/placeholders
- Status (active/inactive)

**Types**:
- Email verification
- Password reset
- Order confirmation
- Order status update
- Promotional emails

**Source Requirements**: FR-025

---

## 2. PRIMARY FLOWS

### 2.1 Visitor Flows

#### 2.1.1 Product Discovery Flow
**Flow Name**: Browse and Search Products

**Actors**: Visitor, System

**Entry Point**: Homepage or direct landing

**Flow Steps**:
1. Visitor accesses website
2. System displays homepage with featured products/categories
3. Visitor chooses search method:
   - **Option A: Keyword Search**
     - Visitor enters search keywords
     - System displays search results with filters/sorting
   - **Option B: Category Browse**
     - Visitor selects category/sub-category
     - System displays category products with filters/sorting
4. Visitor applies filters (price, size, color, ratings)
5. System updates product listing
6. Visitor views product listing page
7. Flow ends or continues to Product Detail Flow

**Source Requirements**: FR-003, FR-004, Section 4

---

#### 2.1.2 Product Detail View Flow
**Flow Name**: View Product Details

**Actors**: Visitor, System

**Preconditions**: Product exists and is active

**Flow Steps**:
1. Visitor clicks on product (from listing or search results)
2. System retrieves product details
3. System displays:
   - Product images
   - Product title and description
   - Price
   - Available sizes and colors
   - Ratings and reviews
4. Visitor interacts with product:
   - View different images
   - Select size/color variations
   - Check shipping availability (enter PIN code)
   - Read reviews and ratings
   - Share on social media
5. Flow ends or continues to:
   - Add to Cart Flow (requires login)
   - Add to Wishlist Flow (requires login)

**Source Requirements**: FR-005

---

### 2.2 Buyer Flows

#### 2.2.1 Registration Flow
**Flow Name**: Buyer Registration

**Actors**: Visitor, System, Email Service

**Entry Point**: Registration page or registration prompt

**Flow Steps**:
1. Visitor clicks "Register" or "Sign Up"
2. System displays registration form
3. Visitor enters:
   - First name
   - Last name
   - Email address
   - Contact number
   - Password
   - Confirm password
4. Visitor accepts terms and conditions
5. Visitor submits form
6. System validates input:
   - Check email uniqueness
   - Verify password match
   - Validate field formats
7. **If validation fails**:
   - System displays error messages
   - Return to step 3
8. **If validation succeeds**:
   - System creates user account (status: unverified)
   - System generates verification token
   - System sends verification email to user
   - System displays "Check your email" message
9. Buyer receives email with verification link
10. Buyer clicks verification link
11. System validates token
12. System updates account status to verified
13. System displays success message
14. Buyer can now login

**Exit Points**:
- Successful registration and verification
- User abandons registration
- Email verification timeout

**Source Requirements**: FR-002

---

#### 2.2.2 Login Flow
**Flow Name**: Buyer Login

**Actors**: Buyer, System

**Entry Point**: Login page or login prompt

**Flow Steps**:
1. Buyer clicks "Login"
2. System displays login options:
   - **Option A: Email/Password Login**
     - Buyer enters email and password
     - System validates credentials
     - System checks email verification status
     - If unverified, redirect to verification reminder
     - If verified, create session and redirect to account
   - **Option B: Social Login (Facebook)**
     - Buyer clicks "Login with Facebook"
     - System redirects to Facebook OAuth
     - Buyer authorizes application
     - Facebook returns user data
     - System creates/updates account and session
   - **Option C: Social Login (Google)**
     - Buyer clicks "Login with Google"
     - System redirects to Google OAuth
     - Buyer authorizes application
     - Google returns user data
     - System creates/updates account and session
3. **If login fails**:
   - System displays error message
   - Offer "Forgot Password" option
   - Return to step 2
4. **If login succeeds**:
   - System creates session
   - System redirects to intended page or account dashboard
5. Flow ends

**Alternate Flow - Password Reset**:
1. Buyer clicks "Forgot Password"
2. Buyer enters email address
3. System sends password reset link
4. Buyer clicks link and sets new password
5. System updates password
6. Buyer redirected to login

**Source Requirements**: FR-001

---

#### 2.2.3 Add to Cart Flow
**Flow Name**: Add Product to Shopping Cart

**Actors**: Buyer, System

**Preconditions**:
- Buyer is logged in
- Product is active and available

**Flow Steps**:
1. Buyer views product detail page
2. Buyer selects product variations (size, color)
3. Buyer selects quantity
4. Buyer clicks "Add to Cart"
5. System validates:
   - User is authenticated
   - Product is available
   - Selected variations exist
6. **If validation fails**:
   - System displays error message
   - Flow ends
7. **If validation succeeds**:
   - System adds product to buyer's cart
   - System displays confirmation (popup/message)
   - System updates cart icon/counter
8. Buyer can:
   - Continue shopping (return to browse)
   - View cart
   - Proceed to checkout

**Source Requirements**: FR-007

---

#### 2.2.4 Add to Wishlist Flow
**Flow Name**: Add Product to Wishlist

**Actors**: Buyer, System

**Preconditions**:
- Buyer is logged in
- Product is active

**Flow Steps**:
1. Buyer views product (listing or detail page)
2. Buyer clicks "Add to Wishlist" icon/button
3. System validates user authentication
4. **If not authenticated**:
   - System prompts login
   - After login, return to this flow
5. **If authenticated**:
   - System adds product to wishlist
   - System displays confirmation
   - System updates wishlist icon/counter
6. Flow ends

**Source Requirements**: FR-006

---

#### 2.2.5 Checkout and Payment Flow
**Flow Name**: Complete Purchase

**Actors**: Buyer, System, Payment Gateway

**Preconditions**:
- Buyer is logged in
- Cart has at least one item

**Flow Steps**:
1. Buyer views shopping cart
2. Buyer reviews cart items (can update quantities or remove items)
3. Buyer clicks "Proceed to Checkout"
4. System validates cart has items
5. **Checkout Step 1: Addresses**
   - System displays saved addresses or address form
   - Buyer selects/enters billing address
   - Buyer selects/enters shipping address (can be same as billing)
   - Buyer clicks "Continue"
6. **Checkout Step 2: Shipping**
   - System calculates shipping cost based on address
   - System displays shipping options (if applicable)
   - Buyer selects shipping method
   - Buyer clicks "Continue"
7. **Checkout Step 3: Review Order**
   - System displays order summary:
     - Items with quantities and prices
     - Subtotal
     - Shipping cost
     - Tax
     - Order total
   - Buyer reviews order
   - Buyer clicks "Proceed to Payment"
8. **Payment Step**:
   - System displays payment options:
     - Credit/Debit Card
     - Net Banking
   - Buyer selects payment method
   - Buyer enters payment details
   - System integrates with Stripe payment gateway
   - Buyer confirms payment
9. **Payment Processing**:
   - System sends payment request to Stripe
   - Stripe processes payment
   - **If payment fails**:
     - System displays error message
     - Buyer can retry or choose different method
     - Return to step 8
   - **If payment succeeds**:
     - Stripe returns success response
     - System creates order record
     - System updates order status to "Confirmed"
     - System clears shopping cart
     - System generates order number
     - System sends order confirmation email to buyer
     - System displays order confirmation page with order number
10. Flow ends

**Exit Points**:
- Successful order placement
- Payment failure (can retry)
- Buyer abandons checkout

**Source Requirements**: FR-008, Section 4

---

#### 2.2.6 Order Tracking Flow
**Flow Name**: Track Order Status

**Actors**: Buyer, System

**Preconditions**:
- Buyer is logged in
- Order exists

**Flow Steps**:
1. Buyer navigates to "My Orders" section
2. System displays list of orders with:
   - Order number
   - Order date
   - Status
   - Total amount
3. Buyer clicks on specific order
4. System displays order details:
   - Items ordered
   - Quantities and prices
   - Shipping address
   - Current order status
   - Shipment tracking information (if shipped)
     - Carrier name
     - Tracking ID
     - Current status
5. Buyer views tracking information
6. Flow ends

**Alternate Flow - Track from Email**:
1. Buyer receives order status email notification
2. Buyer clicks tracking link in email
3. System authenticates buyer
4. Continue from step 4 above

**Source Requirements**: FR-012, Section 4

---

#### 2.2.7 Post Review and Rating Flow
**Flow Name**: Submit Product Review and Rating

**Actors**: Buyer, System

**Preconditions**:
- Buyer is logged in
- Buyer has purchased the product (order exists)

**Flow Steps**:
1. Buyer navigates to purchased product or order history
2. Buyer clicks "Write a Review" or "Rate Product"
3. System validates buyer has purchased product
4. **If not purchased**:
   - System displays message "You must purchase this product to review"
   - Flow ends
5. **If purchased**:
   - System displays review form:
     - Rating (1-5 stars)
     - Review title
     - Review text
6. Buyer enters rating and review
7. Buyer submits review
8. System validates input
9. System saves review with status "Pending"
10. System displays "Thank you, your review is pending approval" message
11. Admin receives notification of new review
12. Flow ends (continues with Admin Review Approval Flow)

**Source Requirements**: FR-011

---

#### 2.2.8 Manage Account Flow
**Flow Name**: Update Account Settings

**Actors**: Buyer, System

**Preconditions**: Buyer is logged in

**Flow Steps**:
1. Buyer clicks "My Account"
2. System displays account dashboard with sections:
   - Profile Details
   - Change Password
   - Address Book
   - My Orders
   - My Wishlist
   - Shopping Cart
   - Ratings and Reviews
3. **Update Profile**:
   - Buyer clicks "Edit Profile"
   - Buyer updates email, phone number
   - Buyer saves changes
   - System validates and updates
4. **Change Password**:
   - Buyer clicks "Change Password"
   - Buyer enters current password
   - Buyer enters new password and confirmation
   - Buyer submits
   - System validates and updates password
5. **Manage Addresses**:
   - Buyer views saved addresses
   - Buyer can add/edit/delete addresses
   - Buyer can set default billing/shipping address
6. Flow ends

**Source Requirements**: FR-010

---

### 2.3 Admin Flows

#### 2.3.1 Admin Login Flow
**Flow Name**: Admin Authentication

**Actors**: Admin User, System

**Entry Point**: Admin panel login page

**Flow Steps**:
1. Admin accesses admin panel URL
2. System displays admin login form
3. Admin enters username and password
4. System validates credentials
5. **If validation fails**:
   - System displays error
   - Offer password reset option
   - Return to step 3
6. **If validation succeeds**:
   - System creates admin session
   - System redirects to admin dashboard
7. Flow ends

**Source Requirements**: FR-014

---

#### 2.3.2 Product Management Flow
**Flow Name**: Create/Edit Product

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Products" section
2. System displays product list with search/filter options
3. **Create New Product**:
   - Admin clicks "Add New Product"
   - System displays product form
   - Admin enters:
     - Product name
     - SKU
     - Description
     - Keywords
     - Category and sub-category
     - Price
     - Sizes (multiple selection)
     - Colors (multiple selection)
   - Admin uploads product images (thumbnail + additional)
   - Admin sets status (Active/Inactive)
   - Admin saves product
   - System validates input
   - System creates product record
   - System displays success message
4. **Edit Existing Product**:
   - Admin searches/filters for product
   - Admin clicks "Edit" on product
   - System displays product form with existing data
   - Admin updates fields
   - Admin saves changes
   - System validates and updates
   - System displays success message
5. **Activate/Deactivate Product**:
   - Admin toggles product status
   - System updates status
6. **Delete Product**:
   - Admin clicks "Delete" on product
   - System prompts confirmation
   - Admin confirms
   - System soft-deletes or archives product
7. Flow ends

**Source Requirements**: FR-019

---

#### 2.3.3 Category Management Flow
**Flow Name**: Manage Product Categories

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Categories" section
2. System displays category tree/list
3. **Add Category**:
   - Admin clicks "Add Category"
   - Admin enters category name, description
   - Admin selects parent category (for sub-category) or none for top-level
   - Admin sets display order
   - Admin sets status
   - Admin saves
   - System creates category
4. **Edit Category**:
   - Admin clicks "Edit" on category
   - Admin updates fields
   - Admin saves
   - System updates category
5. **Activate/Deactivate Category**:
   - Admin toggles status
   - System updates (may affect products in category)
6. Flow ends

**Source Requirements**: FR-018

---

#### 2.3.4 Order Management Flow
**Flow Name**: Process and Fulfill Orders

**Actors**: Admin User, System, Shipping Carrier

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Orders" section
2. System displays order list with filters:
   - Status (Open, Confirmed, In Process, Shipped, Delivered)
   - Date range
   - Customer name
3. Admin selects order to process
4. System displays order details:
   - Order number, date
   - Customer information
   - Items ordered with quantities
   - Billing and shipping address
   - Payment status
   - Current order status
5. **Update Order Status**:
   - Admin views current status
   - Admin updates status to next stage:
     - Open → Confirmed (verify payment)
     - Confirmed → In Process (preparing shipment)
     - In Process → Shipped (package dispatched)
     - Shipped → Delivered (customer received)
6. **Process Shipment** (when status changes to Shipped):
   - Admin enters shipment details:
     - Shipping carrier
     - Tracking ID
     - Estimated delivery date
     - Shipping cost
   - Admin saves shipment information
   - System updates order and shipment records
   - System sends "Order Shipped" email to buyer with tracking info
7. **Mark as Delivered**:
   - Admin updates status to Delivered
   - System records delivery date
   - System sends "Order Delivered" email to buyer
8. Admin can view order history and all status changes
9. Flow ends

**Source Requirements**: FR-017, Section 4

---

#### 2.3.5 Customer Management Flow
**Flow Name**: Manage Customer Accounts

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Customers" section
2. System displays customer list with filters
3. Admin searches/filters for specific customer
4. Admin clicks on customer record
5. System displays customer details:
   - Profile information
   - Registration date
   - Order history
   - Wishlist items
   - Cart items (current)
   - Saved addresses
   - Reviews and ratings posted
6. Admin can:
   - View all customer data (read-only some fields)
   - Edit customer profile (email, phone)
   - Activate/Deactivate account
   - View customer's order details
7. Admin saves changes if any
8. System updates customer record
9. Flow ends

**Source Requirements**: FR-016

---

#### 2.3.6 Review Moderation Flow
**Flow Name**: Approve/Reject Customer Reviews

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Reviews & Ratings" section
2. System displays list of reviews with filter:
   - Status (Pending, Approved, Rejected)
   - Product
   - Date
3. Admin filters for "Pending" reviews
4. System displays pending reviews for moderation
5. Admin reads review content and rating
6. Admin decides:
   - **Approve**:
     - Admin clicks "Approve"
     - System updates review status to "Approved"
     - System displays review on product page
     - System recalculates product average rating
     - System displays confirmation
   - **Reject**:
     - Admin clicks "Reject"
     - System prompts for rejection reason (optional)
     - System updates review status to "Rejected"
     - Review not displayed on site
     - System displays confirmation
7. Admin repeats for other pending reviews
8. Flow ends

**Source Requirements**: FR-020

---

#### 2.3.7 Reports and Statistics Flow
**Flow Name**: View Business Reports

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "Statistics & Reports" section
2. System displays dashboard with:
   - Total active/inactive customers
   - Total products
   - Revenue metrics (today, this week, this month)
   - Recent orders
3. Admin selects specific report type:
   - **Products Uploaded Report**:
     - Admin selects date range (from-to, month, year)
     - System generates report
     - System displays products uploaded count by period
   - **Revenue Report**:
     - Admin selects period (today, current week, date range, month, year)
     - System calculates total revenue for period
     - System displays revenue breakdown
     - System shows charts/graphs
4. Admin can export report:
   - Admin clicks "Export"
   - Admin selects format (PDF or Excel)
   - System generates file
   - System initiates download
5. Flow ends

**Source Requirements**: FR-015, FR-021

---

#### 2.3.8 CMS Management Flow
**Flow Name**: Update Website Content Pages

**Actors**: Admin User, System

**Preconditions**: Admin is logged in

**Flow Steps**:
1. Admin navigates to "CMS Pages" section
2. System displays list of CMS pages:
   - About Us
   - Contact Us
   - Privacy Policy
   - Terms and Conditions
3. Admin selects page to edit
4. System displays content editor (WYSIWYG or HTML)
5. Admin updates page content
6. Admin previews changes (optional)
7. Admin saves changes
8. System validates content
9. System updates page
10. System displays success message
11. Updated content visible on frontend
12. Flow ends

**Source Requirements**: FR-024

---

#### 2.3.9 User and Role Management Flow
**Flow Name**: Manage Admin Sub-Users and Roles

**Actors**: Admin User, System

**Preconditions**: Admin is logged in with appropriate permissions

**Flow Steps**:
1. **Manage Roles**:
   - Admin navigates to "Roles" section
   - System displays existing roles
   - Admin creates new role:
     - Enter role name
     - Select permissions (checkboxes for each module/function)
     - Set status
     - Save role
   - Admin can edit/activate/deactivate existing roles
2. **Manage Sub-Users**:
   - Admin navigates to "Users" section
   - System displays list of sub-users
   - Admin creates new sub-user:
     - Enter username, password
     - Assign role (from dropdown)
     - Set status
     - Save user
   - Admin can edit/activate/deactivate sub-users
3. System enforces role-based access for sub-users
4. Flow ends

**Source Requirements**: FR-022, FR-023

---

### 2.4 System Flows

#### 2.4.1 Email Notification Flow
**Flow Name**: Automated Email Sending

**Actors**: System, Email Service

**Triggers**: Various system events

**Flow Steps**:
1. System event occurs (e.g., order placed, order shipped)
2. System identifies appropriate email template
3. System populates template with dynamic data
4. System validates recipient email address
5. System sends email via email service provider
6. Email service delivers email
7. System logs email sent status
8. Flow ends

**Email Types**:
- Registration email verification
- Password reset
- Order confirmation
- Order status updates (shipped, delivered)
- Promotional emails (admin-initiated)
- Contact form submission confirmation
- Review approval notification

**Source Requirements**: FR-002, FR-008, FR-012, FR-017, FR-025

---

#### 2.4.2 Search and Filter Flow
**Flow Name**: Product Search Engine

**Actors**: Visitor/Buyer, System

**Entry Point**: Search bar or category page

**Flow Steps**:
1. User enters search query OR selects category
2. System processes search:
   - **Keyword Search**:
     - System searches product names, descriptions, keywords
     - System applies relevance ranking
   - **Category Browse**:
     - System filters products by selected category/sub-category
3. System retrieves matching products (active products only)
4. System displays results with:
   - Product thumbnail
   - Name
   - Price
   - Rating
5. User applies additional filters:
   - Price range
   - Size
   - Color
   - Rating
6. System refines results based on filters
7. User applies sorting:
   - Relevance (for search)
   - Price: Low to High
   - Price: High to Low
   - Newest First
   - Best Rating
8. System reorders results
9. System displays paginated results
10. Flow ends

**Source Requirements**: FR-003, FR-004

---

#### 2.4.3 Payment Processing Flow
**Flow Name**: Stripe Payment Integration

**Actors**: System, Stripe Payment Gateway, Buyer

**Preconditions**: Order created, payment details provided

**Flow Steps**:
1. System receives payment details from checkout
2. System validates payment information format
3. System creates payment request payload:
   - Amount (order total)
   - Currency (USD)
   - Payment method details
   - Order metadata
4. System calls Stripe API
5. Stripe validates payment method
6. Stripe processes payment with bank/card network
7. **If payment declined**:
   - Stripe returns failure response with reason
   - System logs failure
   - System displays error to buyer
   - Buyer can retry with different method
   - Flow ends (unsuccessful)
8. **If payment approved**:
   - Stripe returns success response with transaction ID
   - System saves transaction ID with order
   - System updates order status to "Confirmed"
   - System updates payment status to "Completed"
   - System triggers order confirmation email
   - Flow ends (successful)

**Source Requirements**: FR-008, FR-020

---

## 3. ENTITY RELATIONSHIP SUMMARY

### 3.1 Core Relationships

```
USER (Buyer)
├── Has many → ADDRESSES
├── Has one → SHOPPING CART
│   └── Has many → CART ITEMS
│       └── References → PRODUCT
├── Has one → WISHLIST
│   └── Has many → WISHLIST ITEMS
│       └── References → PRODUCT
├── Has many → ORDERS
│   ├── Has many → ORDER ITEMS
│   │   └── References → PRODUCT
│   ├── Has one → PAYMENT
│   ├── Has one → SHIPMENT
│   ├── References → BILLING ADDRESS
│   └── References → SHIPPING ADDRESS
├── Has many → REVIEWS
│   └── Belongs to → PRODUCT
└── Has many → RATINGS
    └── Belongs to → PRODUCT

PRODUCT
├── Belongs to → CATEGORY
├── Belongs to → SUB-CATEGORY (optional)
├── Has many → REVIEWS
├── Has many → RATINGS
├── Referenced by many → CART ITEMS
├── Referenced by many → WISHLIST ITEMS
└── Referenced by many → ORDER ITEMS

CATEGORY
├── Has many → PRODUCTS
└── Has many → SUB-CATEGORIES (self-referential)

ORDER
├── Belongs to → USER (Buyer)
├── Has many → ORDER ITEMS
├── Has one → PAYMENT
├── Has one → SHIPMENT
├── References → BILLING ADDRESS
└── References → SHIPPING ADDRESS

ADMIN USER
├── Has assigned → ROLE
└── Can have → PERMISSIONS (via role)
```

---

## 4. FLOW DEPENDENCIES

### 4.1 Sequential Dependencies
1. **Registration → Email Verification → Login** (FR-002, FR-001)
2. **Product Search → Product Detail → Add to Cart → Checkout → Payment → Order** (FR-003 → FR-004 → FR-005 → FR-007 → FR-008)
3. **Order Placed → Order Processing → Shipment → Delivery** (FR-008 → FR-017)
4. **Order Delivered → Post Review** (FR-011 requires order)

### 4.2 Parallel/Independent Flows
- Browse products (can run independently of login)
- Wishlist and Cart (can be built simultaneously)
- Admin product management and order management (independent)
- Review moderation and customer management (independent)

---

## 5. CRITICAL INTERACTION POINTS

### 5.1 Authentication Checkpoints
- Adding to cart (FR-007)
- Adding to wishlist (FR-006)
- Checkout process (FR-008)
- Posting reviews (FR-011)
- Accessing "My Account" (FR-010)
- All admin functions (FR-014+)

### 5.2 Data Validation Points
- User registration (email uniqueness, password strength)
- Product creation (SKU uniqueness, required fields)
- Checkout (address validation, inventory check)
- Payment processing (payment method validation)
- Review posting (purchase verification)

### 5.3 External Integration Points
- Stripe payment gateway (FR-008, FR-020)
- Email service (FR-002, FR-008, FR-012, FR-025)
- Facebook OAuth (FR-001)
- Google OAuth (FR-001)
- Social media sharing (FR-009)

---

## Document Complete
This document provides a comprehensive mapping of all entities and flows derived from the BRD requirements. These will form the basis for test scenario generation in the next step.
