# Entities and Flows - Ecommerce Website

## Document Information
- **Source**: Business Requirement Document: Ecommerce Website v1.0
- **Extraction Date**: 2025-11-14
- **Total Entities**: 38
- **Total Flows**: 24

---

## PART 1: KEY ENTITIES

### 1. User Roles (4 entities)

#### 1.1 Visitor (Guest User)
- **Description**: Unregistered user browsing the website
- **Capabilities**:
  - Search products
  - View product listings
  - View product details
  - View ratings and reviews
  - Share products on social media
  - Check shipping availability by PIN code
  - Contact support
- **Limitations**:
  - Cannot add to cart
  - Cannot add to wishlist
  - Cannot place orders
  - Cannot post ratings/reviews

#### 1.2 Buyer (Registered User)
- **Description**: Registered and logged-in customer
- **Capabilities**:
  - All Visitor capabilities PLUS:
  - Register and login
  - Manage profile
  - Add to cart
  - Add to wishlist
  - Checkout and pay
  - Place orders
  - View order history
  - Track orders
  - Post ratings and reviews
  - Manage address book
- **Authentication**: Email/password, Facebook, or Google login

#### 1.3 Admin (Business Owner)
- **Description**: Primary system administrator with full access
- **Capabilities**:
  - Manage all products
  - Manage all categories
  - Manage all orders
  - Manage all customers
  - Manage all payments
  - Manage shipping
  - Manage CMS pages
  - Manage ratings/reviews
  - View statistics and reports
  - Manage roles and permissions
  - Manage sub-users
  - Receive complaint notifications

#### 1.4 Sub-Admin (Sub-User)
- **Description**: Limited administrator with role-based access
- **Capabilities**:
  - Role-based sectional operations
  - Permissions assigned by Admin
  - May have limited access to specific admin functions

---

### 2. Product Entities (5 entities)

#### 2.1 Product
- **Attributes**:
  - Product ID (SKU)
  - Product Name/Title
  - Description
  - Price (USD)
  - Keywords (for search)
  - Status (Active/Inactive)
  - Category ID (link to Category)
  - Sub-category ID (link to Sub-category)
  - Created date
  - Modified date
- **Relationships**:
  - Belongs to one Category
  - Belongs to one Sub-category
  - Has many Product Images
  - Has many Product Variations
  - Has many Ratings
  - Has many Reviews

#### 2.2 Product Image
- **Attributes**:
  - Image ID
  - Product ID (foreign key)
  - Image URL/Path
  - Is Thumbnail (boolean)
  - Sort Order
- **Relationships**:
  - Belongs to one Product

#### 2.3 Product Variation
- **Attributes**:
  - Variation ID
  - Product ID (foreign key)
  - Color
  - Size
  - Stock Quantity (implicit)
  - Status (Active/Inactive)
- **Relationships**:
  - Belongs to one Product

#### 2.4 Category
- **Attributes**:
  - Category ID
  - Category Name
  - Description
  - Status (Active/Inactive)
  - Sort Order
- **Relationships**:
  - Has many Sub-categories
  - Has many Products

#### 2.5 Sub-category
- **Attributes**:
  - Sub-category ID
  - Category ID (foreign key)
  - Sub-category Name
  - Description
  - Status (Active/Inactive)
  - Sort Order
- **Relationships**:
  - Belongs to one Category
  - Has many Products

---

### 3. Shopping Entities (4 entities)

#### 3.1 Shopping Cart
- **Attributes**:
  - Cart ID
  - User ID (foreign key)
  - Created Date
  - Modified Date
  - Status (Active/Abandoned)
- **Relationships**:
  - Belongs to one Buyer
  - Has many Cart Items

#### 3.2 Cart Item
- **Attributes**:
  - Cart Item ID
  - Cart ID (foreign key)
  - Product ID (foreign key)
  - Variation ID (foreign key)
  - Quantity
  - Unit Price
  - Subtotal
  - Added Date
- **Relationships**:
  - Belongs to one Cart
  - References one Product
  - References one Product Variation

#### 3.3 Wishlist
- **Attributes**:
  - Wishlist ID
  - User ID (foreign key)
  - Created Date
- **Relationships**:
  - Belongs to one Buyer
  - Has many Wishlist Items

#### 3.4 Wishlist Item
- **Attributes**:
  - Wishlist Item ID
  - Wishlist ID (foreign key)
  - Product ID (foreign key)
  - Added Date
- **Relationships**:
  - Belongs to one Wishlist
  - References one Product

---

### 4. Order Entities (3 entities)

#### 4.1 Order
- **Attributes**:
  - Order ID
  - User ID (foreign key)
  - Order Number (display)
  - Order Date
  - Order Status (Open, Confirmed, In Process, Shipped, Delivered)
  - Item Total
  - Sub-total
  - Shipping Cost
  - Tax
  - Order Total
  - Billing Address ID (foreign key)
  - Shipping Address ID (foreign key)
  - Payment Method ID (foreign key)
  - Payment Status (Pending, Paid, Failed)
  - Shipment ID (foreign key)
- **Relationships**:
  - Belongs to one Buyer
  - Has many Order Items
  - Has one Billing Address
  - Has one Shipping Address
  - Has one Payment
  - Has one Shipment

#### 4.2 Order Item
- **Attributes**:
  - Order Item ID
  - Order ID (foreign key)
  - Product ID (foreign key)
  - Variation ID (foreign key)
  - Quantity
  - Unit Price
  - Subtotal
- **Relationships**:
  - Belongs to one Order
  - References one Product
  - References one Product Variation

#### 4.3 Shipment
- **Attributes**:
  - Shipment ID
  - Order ID (foreign key)
  - Shipping Carrier
  - Tracking ID
  - Current Status
  - Delivery Address ID (foreign key)
  - Shipping Cost
  - Shipped Date
  - Estimated Delivery Date
  - Actual Delivery Date
- **Relationships**:
  - Belongs to one Order
  - Has one Delivery Address

---

### 5. Payment Entities (2 entities)

#### 5.1 Payment
- **Attributes**:
  - Payment ID
  - Order ID (foreign key)
  - Payment Method (Credit Card, Debit Card, Net Banking)
  - Payment Gateway (Stripe)
  - Transaction ID (from Stripe)
  - Amount
  - Currency (USD)
  - Payment Status (Pending, Completed, Failed)
  - Payment Date
  - Card Last 4 Digits (if applicable)
- **Relationships**:
  - Belongs to one Order

#### 5.2 Payment Gateway Configuration
- **Attributes**:
  - Config ID
  - Gateway Name (Stripe)
  - API Keys (encrypted)
  - Bank Account Details (for receiving payments)
  - Status (Active/Inactive)
- **Relationships**:
  - System-level configuration

---

### 6. User Profile Entities (3 entities)

#### 6.1 User Profile
- **Attributes**:
  - User ID
  - First Name
  - Last Name
  - Email (unique)
  - Contact Number
  - Password (hashed)
  - Email Verified (boolean)
  - Registration Date
  - Last Login Date
  - Account Status (Active/Inactive)
  - Login Method (Email, Facebook, Google)
- **Relationships**:
  - Has many Addresses
  - Has one Shopping Cart
  - Has one Wishlist
  - Has many Orders
  - Has many Ratings
  - Has many Reviews

#### 6.2 Address
- **Attributes**:
  - Address ID
  - User ID (foreign key)
  - Address Type (Billing, Shipping, Both)
  - Full Name
  - Address Line 1
  - Address Line 2
  - City
  - State
  - ZIP Code (PIN code in BRD, but US only)
  - Country (USA)
  - Phone Number
  - Is Default (boolean)
- **Relationships**:
  - Belongs to one User

#### 6.3 Email Verification
- **Attributes**:
  - Verification ID
  - User ID (foreign key)
  - Verification Token
  - Created Date
  - Expiry Date
  - Verified Date
  - Status (Pending, Verified, Expired)
- **Relationships**:
  - Belongs to one User

---

### 7. Rating & Review Entities (2 entities)

#### 7.1 Rating
- **Attributes**:
  - Rating ID
  - User ID (foreign key)
  - Product ID (foreign key)
  - Order ID (foreign key) - to verify purchase
  - Rating Value (scale TBD, assume 1-5)
  - Created Date
  - Status (Pending, Approved, Rejected)
- **Relationships**:
  - Belongs to one Buyer
  - Belongs to one Product
  - References one Order (purchased product)

#### 7.2 Review
- **Attributes**:
  - Review ID
  - User ID (foreign key)
  - Product ID (foreign key)
  - Order ID (foreign key) - to verify purchase
  - Review Text
  - Created Date
  - Status (Pending, Approved, Rejected)
- **Relationships**:
  - Belongs to one Buyer
  - Belongs to one Product
  - References one Order (purchased product)
  - May have one Rating (same user/product)

---

### 8. CMS & Communication Entities (4 entities)

#### 8.1 CMS Page
- **Attributes**:
  - Page ID
  - Page Title
  - Page Slug/URL
  - Page Content (HTML)
  - Meta Title
  - Meta Description
  - Last Modified Date
  - Modified By (Admin ID)
  - Status (Active/Inactive)
- **Pages**:
  - About Us
  - Contact Us
  - Privacy Policy
  - Terms and Conditions
- **Relationships**:
  - Modified by Admin

#### 8.2 Email Template
- **Attributes**:
  - Template ID
  - Template Name
  - Subject Line
  - Email Body (HTML)
  - Template Type (Transactional, Marketing)
  - Created Date
  - Modified Date
  - Status (Active/Inactive)
- **Types**:
  - Email verification
  - Password reset
  - Order confirmation
  - Shipping notification
  - Delivery confirmation
  - New product launch
  - Offers/Promotions
- **Relationships**:
  - Managed by Admin

#### 8.3 Support Request (Contact Form)
- **Attributes**:
  - Request ID
  - Name
  - Email
  - Contact Number
  - Message
  - Request Date
  - Status (New, In Progress, Resolved)
  - Assigned To (Admin ID)
- **Relationships**:
  - May be linked to User (if logged in)
  - Assigned to Admin

#### 8.4 Email Notification Log
- **Attributes**:
  - Log ID
  - User ID (recipient)
  - Email Template ID
  - Sent Date
  - Status (Sent, Failed, Bounced)
  - Order ID (if order-related)
- **Relationships**:
  - Sent to User
  - Uses Email Template
  - May reference Order

---

### 9. Admin Entities (3 entities)

#### 9.1 Admin User
- **Attributes**:
  - Admin ID
  - Username
  - Email
  - Password (hashed)
  - Role ID (foreign key)
  - Status (Active/Inactive)
  - Created Date
  - Last Login Date
  - Is Primary Admin (boolean)
- **Relationships**:
  - Has one Role
  - May manage multiple sections

#### 9.2 Role
- **Attributes**:
  - Role ID
  - Role Name
  - Description
  - Status (Active/Inactive)
- **Relationships**:
  - Has many Permissions
  - Assigned to many Admin Users

#### 9.3 Permission
- **Attributes**:
  - Permission ID
  - Role ID (foreign key)
  - Module Name
  - Can Create (boolean)
  - Can Read (boolean)
  - Can Update (boolean)
  - Can Delete (boolean)
- **Modules**:
  - Products
  - Categories
  - Orders
  - Customers
  - Payments
  - Shipping
  - CMS
  - Reports
  - Ratings/Reviews
  - Users/Roles
- **Relationships**:
  - Belongs to one Role

---

### 10. Reporting Entities (2 entities)

#### 10.1 Product Upload Report
- **Attributes**:
  - Report ID
  - Date Range (From-To)
  - Month
  - Year
  - Total Products Uploaded
  - Generated Date
  - Generated By (Admin ID)
- **Relationships**:
  - Generated by Admin

#### 10.2 Revenue Report
- **Attributes**:
  - Report ID
  - Report Period (Today, Current Week, Date Range, Month, Year)
  - Start Date
  - End Date
  - Total Revenue
  - Total Orders
  - Generated Date
  - Generated By (Admin ID)
  - Export Format (PDF, Excel)
- **Relationships**:
  - Generated by Admin

---

## PART 2: PRIMARY FLOWS

### BUYER FLOWS (12 flows)

#### Flow 1: User Registration & Email Verification
**Flow Steps**:
1. Visitor navigates to Registration page
2. Visitor enters registration form:
   - First Name
   - Last Name
   - Email
   - Contact Number
   - Password
   - Confirm Password
   - Accepts Terms and Conditions
3. System validates input
4. System creates user account (inactive status)
5. System generates email verification token
6. System sends verification email with link
7. User clicks verification link in email
8. System validates token
9. System activates user account
10. System redirects to login page
11. User logs in with email and password
12. User is redirected to homepage (logged in)

**Related Requirements**: REQ-005 through REQ-016

---

#### Flow 2: User Login (Email/Password)
**Flow Steps**:
1. User navigates to Login page
2. User enters email and password
3. System validates credentials
4. System checks email verification status
5. System creates user session
6. System redirects to homepage or previous page
7. User can access authenticated features

**Related Requirements**: REQ-001

---

#### Flow 3: User Login (Social - Facebook/Google)
**Flow Steps**:
1. User clicks "Login with Facebook" or "Login with Google"
2. System redirects to OAuth provider
3. User authorizes application
4. OAuth provider returns user data
5. System checks if user exists (by email)
6. If new user: System creates account (auto-verified)
7. If existing user: System logs in
8. System creates user session
9. System redirects to homepage

**Related Requirements**: REQ-003, REQ-004

---

#### Flow 4: Password Reset
**Flow Steps**:
1. User clicks "Forgot Password" on Login page
2. User enters email address
3. System validates email exists
4. System generates password reset token
5. System sends password reset email with link
6. User clicks link in email
7. System validates token (not expired)
8. User enters new password and confirms
9. System validates password
10. System updates password (hashed)
11. System invalidates reset token
12. System confirms password reset
13. User logs in with new password

**Related Requirements**: REQ-002, REQ-019

---

#### Flow 5: Product Search & Browse
**Flow Steps**:
1. User enters keyword in search bar OR selects category
2. System searches products by:
   - Keyword match (name, description, keywords)
   - OR Category/Sub-category filter
3. System displays product listing with:
   - Product title
   - Thumbnail image
   - Price
   - Ratings & reviews
4. User applies filters (color, size, price range, etc.)
5. User applies sorting (price, popularity, rating, newest)
6. System refines results
7. User clicks on product title or image
8. System displays product detail page

**Related Requirements**: REQ-020 through REQ-032

---

#### Flow 6: View Product Details & Check Shipping
**Flow Steps**:
1. User lands on product detail page
2. System displays:
   - Product title
   - Images (thumbnail + gallery)
   - Description
   - Price
   - Available sizes
   - Available colors
   - Ratings & reviews
3. User enters PIN code (ZIP code) to check shipping availability
4. System validates ZIP code
5. System displays shipping availability (Yes/No, estimated delivery)
6. User selects size and color variation
7. User can:
   - Add to Cart
   - Add to Wishlist (requires login)
   - Share on social media

**Related Requirements**: REQ-033 through REQ-044, REQ-050 through REQ-052

---

#### Flow 7: Add to Wishlist
**Flow Steps**:
1. User clicks "Add to Wishlist" on product detail page
2. System checks if user is logged in
3. If not logged in: System redirects to login page
4. If logged in: System adds product to user's wishlist
5. System confirms item added
6. User can view wishlist from My Account
7. User can checkout items from wishlist

**Related Requirements**: REQ-044 through REQ-049

---

#### Flow 8: Add to Cart & Manage Cart
**Flow Steps**:
1. User selects product variation (size, color)
2. User clicks "Add to Cart"
3. System checks if user is logged in
4. If not logged in: System redirects to login page
5. If logged in: System adds item to cart
6. System displays cart summary
7. User can:
   - Update quantity
   - Remove items
   - View item price, subtotal, total
8. User proceeds to checkout

**Related Requirements**: REQ-053 through REQ-061

---

#### Flow 9: Checkout & Payment
**Flow Steps**:
1. User clicks "Proceed to Checkout" from cart
2. System checks user is logged in
3. System displays checkout page
4. User selects or adds billing address
5. User selects or adds shipping address
6. System calculates:
   - Item total
   - Sub-total
   - Shipping cost
   - Tax
   - Order total
7. System displays order summary
8. User selects payment method:
   - Credit/Debit Card
   - Net Banking
9. User proceeds to payment
10. System redirects to Stripe payment gateway
11. User completes payment on Stripe
12. Stripe processes payment
13. Stripe returns payment status
14. If payment successful:
    - System creates order
    - System updates order status to "Open"
    - System clears cart items
    - System sends order confirmation email
    - System displays order confirmation page
15. If payment fails:
    - System displays error message
    - System allows user to retry

**Related Requirements**: REQ-062 through REQ-075

---

#### Flow 10: View Order History & Track Order
**Flow Steps**:
1. User navigates to "My Account" > "My Orders"
2. System displays list of all past orders with:
   - Order number
   - Order date
   - Order total
   - Order status
3. User clicks on order to view details
4. System displays:
   - All order items (product, quantity, price per unit)
   - Shipping address
   - Total amount paid
   - Order status
   - Tracking information (if available)
5. User can:
   - Track current order
   - Reorder items

**Related Requirements**: REQ-076 through REQ-082

---

#### Flow 11: Post Rating & Review
**Flow Steps**:
1. User navigates to "My Account" > "Ratings and Reviews"
2. System displays products user has ordered
3. User selects product to review
4. User enters rating (1-5 stars, assumed)
5. User enters review text
6. User submits rating and review
7. System saves rating and review (Pending status)
8. System notifies admin for approval
9. Admin approves or rejects
10. If approved: Rating/review appears on product page
11. If rejected: Rating/review not displayed

**Related Requirements**: REQ-095 through REQ-098, REQ-159 through REQ-162

---

#### Flow 12: Contact Support
**Flow Steps**:
1. User navigates to "Contact Us" page
2. User enters:
   - Name
   - Email
   - Contact number
   - Message/Query
3. User submits form
4. System saves support request
5. System sends email notification to admin
6. System confirms submission to user
7. Admin reviews and responds via email

**Related Requirements**: REQ-102 through REQ-107

---

### ADMIN FLOWS (12 flows)

#### Flow 13: Admin Login
**Flow Steps**:
1. Admin navigates to admin panel login
2. Admin enters username and password
3. System validates credentials
4. System creates admin session
5. System redirects to admin dashboard
6. Admin can access admin features based on role

**Related Requirements**: REQ-017, REQ-018

---

#### Flow 14: View Dashboard Statistics
**Flow Steps**:
1. Admin logs in to admin panel
2. System displays dashboard with:
   - Total active registered buyers
   - Total inactive registered buyers
   - Total products uploaded
   - Total revenue (today)
   - Total revenue (current month)
3. Admin reviews statistics

**Related Requirements**: REQ-108 through REQ-112

---

#### Flow 15: Manage Product Categories
**Flow Steps**:
1. Admin navigates to "Product Categories" section
2. System displays list of categories and sub-categories
3. Admin can:
   - **Add Category**:
     - Enter category name, description
     - Save category
   - **Edit Category**:
     - Select category
     - Update name, description
     - Save changes
   - **Activate/Deactivate Category**:
     - Select category
     - Change status
   - **Add Sub-category**:
     - Select parent category
     - Enter sub-category name, description
     - Save sub-category
   - **Edit Sub-category**:
     - Select sub-category
     - Update name, description
     - Save changes
   - **Activate/Deactivate Sub-category**:
     - Select sub-category
     - Change status

**Related Requirements**: REQ-137 through REQ-144

---

#### Flow 16: Manage Products
**Flow Steps**:
1. Admin navigates to "Products" section
2. System displays list of all products
3. Admin can:
   - **Add Product**:
     - Enter product name
     - Enter description
     - Enter keywords
     - Upload images
     - Set price
     - Select category and sub-category
     - Add variations (colors, sizes)
     - Save product
   - **Edit Product**:
     - Select product
     - Update any fields
     - Manage variations
     - Save changes
   - **Activate/Deactivate Product**:
     - Select product
     - Change status
   - **Delete Product** (implicit):
     - Select product
     - Delete (or deactivate)

**Related Requirements**: REQ-145 through REQ-154

---

#### Flow 17: Manage Orders & Shipping
**Flow Steps**:
1. Admin navigates to "Orders" section
2. System displays list of all orders with current status
3. Admin selects order to view details
4. System displays:
   - Order items
   - Customer information
   - Billing and shipping addresses
   - Payment status
   - Current order status
5. Admin can:
   - **Update Order Status**:
     - Change status (Open → Confirmed → In Process → Shipped → Delivered)
   - **Edit Order Details**:
     - Update items, quantities (if not shipped)
   - **Add Shipping Information**:
     - Enter shipping carrier
     - Enter tracking ID
     - Enter current shipment status
     - Enter delivery address
     - Enter shipping cost
     - Update order status to "Shipped"
6. System sends email notification to buyer on status update

**Related Requirements**: REQ-122 through REQ-136

---

#### Flow 18: Manage Customers (Buyers)
**Flow Steps**:
1. Admin navigates to "Customers" section
2. System displays list of all registered buyers
3. Admin selects buyer to view details
4. System displays:
   - Profile details (name, email, phone)
   - Addresses
   - Order history
   - Wishlist items
   - Cart items
5. Admin can:
   - Edit buyer profile
   - Activate/Deactivate buyer account
   - View all buyer activity

**Related Requirements**: REQ-113 through REQ-121

---

#### Flow 19: Manage Payments
**Flow Steps**:
1. Admin navigates to "Payments" section
2. Admin can:
   - View payment gateway configuration
   - Edit bank account details
   - View payment status of all orders
   - Filter by status (Pending, Paid, Failed)

**Related Requirements**: REQ-155 through REQ-158

---

#### Flow 20: Approve/Reject Ratings & Reviews
**Flow Steps**:
1. Admin navigates to "Ratings & Reviews" section
2. System displays list of pending ratings and reviews
3. Admin selects rating/review to review
4. System displays:
   - User who posted
   - Product reviewed
   - Rating value
   - Review text
   - Date posted
5. Admin can:
   - Approve: Rating/review appears on product page
   - Reject: Rating/review does not appear

**Related Requirements**: REQ-159 through REQ-162

---

#### Flow 21: Generate Reports
**Flow Steps**:
1. Admin navigates to "Reports" section
2. Admin selects report type:
   - **Products Uploaded Report**:
     - Select date range (From-To) OR Month OR Year
     - Generate report
   - **Revenue/Sales Report**:
     - Select period (Today, Current Week, Date Range, Month, Year)
     - Generate report
3. System generates report with statistics
4. System displays report on screen
5. Admin can export report as:
   - PDF
   - Excel
6. System downloads exported report

**Related Requirements**: REQ-163 through REQ-172

---

#### Flow 22: Manage Sub-Admin Users & Roles
**Flow Steps**:
1. Admin navigates to "Users & Roles" section
2. Admin can:
   - **Manage Roles**:
     - Add new role
     - Edit role name and description
     - Delete role
     - Activate/Deactivate role
     - Assign permissions to role (Create, Read, Update, Delete per module)
   - **Manage Sub-Users**:
     - Create new sub-admin user
     - Assign role to user
     - Edit user details
     - Delete user
     - Activate/Deactivate user

**Related Requirements**: REQ-173 through REQ-184

---

#### Flow 23: Manage CMS Pages
**Flow Steps**:
1. Admin navigates to "CMS" section
2. System displays list of CMS pages:
   - About Us
   - Contact Us
   - Privacy Policy
   - Terms and Conditions
3. Admin selects page to edit
4. Admin updates page content (using WYSIWYG editor)
5. Admin saves changes
6. System updates page content on website

**Related Requirements**: REQ-185 through REQ-188

---

#### Flow 24: Manage Email Templates & Send Marketing Emails
**Flow Steps**:
1. Admin navigates to "Email Management" section
2. Admin can:
   - **Manage Templates**:
     - Add new email template
     - Edit existing template (subject, body)
     - Delete template
   - **Send Marketing Emails**:
     - Select email type (New Product Launch, Offers, Promotions)
     - Select or create email content
     - Select recipient list (all buyers, specific segment)
     - Send email
3. System sends emails to selected recipients

**Related Requirements**: REQ-189 through REQ-194

---

## Summary

### Entity Counts by Category:
- **User Roles**: 4 entities
- **Product Entities**: 5 entities
- **Shopping Entities**: 4 entities
- **Order Entities**: 3 entities
- **Payment Entities**: 2 entities
- **User Profile Entities**: 3 entities
- **Rating & Review Entities**: 2 entities
- **CMS & Communication Entities**: 4 entities
- **Admin Entities**: 3 entities
- **Reporting Entities**: 2 entities

**Total Entities**: 32 (not counting sub-components)

### Flow Counts by User Type:
- **Buyer Flows**: 12 flows
- **Admin Flows**: 12 flows

**Total Flows**: 24 flows

### Key Integrations:
1. **Stripe Payment Gateway** - For online payments
2. **Email Service** - For transactional and marketing emails
3. **Facebook OAuth** - For social login
4. **Google OAuth** - For social login
5. **Shipping Carrier APIs** - For tracking (implicit)

### Data Relationships:
- **One-to-Many**: User-to-Orders, User-to-Addresses, Product-to-Images, Category-to-Products
- **Many-to-Many**: Products-to-Categories (through sub-categories)
- **One-to-One**: Order-to-Payment, Order-to-Shipment

---

## Notes for Test Scenario Generation:
1. Each entity should have CRUD test scenarios (where applicable)
2. Each flow should have positive, negative, and edge case scenarios
3. Integration points (payment gateway, email, OAuth) require specific testing
4. State transitions (Order Status, Payment Status) need exhaustive testing
5. Role-based access control needs permission matrix testing
6. All user inputs need validation testing
7. All relationships need referential integrity testing
