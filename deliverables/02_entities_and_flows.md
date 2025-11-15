# Entities and Flows Analysis
**Source**: BRD - Online Apparels Shopping Website
**Date**: 2025-11-15

---

## 1. User Roles (4 roles)

### 1.1 Visitor (Guest User)
- **Description**: Unauthenticated users visiting the website
- **Capabilities**:
  - Browse products
  - Search products by keyword/category
  - View product listing and details
  - Check shipping availability
  - Share products on social media
  - View ratings and reviews
  - Contact support
- **Limitations**:
  - Cannot add to wishlist
  - Cannot add to cart
  - Cannot checkout
  - Cannot post reviews

### 1.2 Buyer (Registered User)
- **Description**: Registered and authenticated customers
- **Capabilities**:
  - All Visitor capabilities, plus:
  - Register and login
  - Manage wishlist
  - Manage shopping cart
  - Checkout and make payments
  - Track orders
  - View order history
  - Reorder previous items
  - Post ratings and reviews
  - Manage profile and addresses
  - Change password
- **Authentication**: Email/password, Facebook, Google

### 1.3 Admin (Business Owner)
- **Description**: Primary system administrator and business owner
- **Capabilities**:
  - Full system access
  - Manage products catalog
  - Manage categories
  - Manage orders and shipments
  - Manage customers
  - Manage payments
  - Manage sub-users and roles
  - View dashboard analytics
  - Manage CMS content
  - Approve/reject reviews
  - Generate reports
  - Manage email campaigns

### 1.4 Sub-Admin (Sub-User)
- **Description**: Secondary admin users with role-based access
- **Capabilities**:
  - Limited access based on assigned roles
  - Operate specific system sections
  - Defined by Admin through roles management

---

## 2. Core Entities (15 entities)

### 2.1 User/Account
**Attributes**:
- User ID (primary key)
- First Name
- Last Name
- Email (unique, verified)
- Contact Number
- Password (encrypted)
- Role (Buyer/Admin/Sub-Admin)
- Account Status (Active/Inactive)
- Created Date
- Email Verified (boolean)
- Social Login Provider (Facebook/Google/None)

### 2.2 Product
**Attributes**:
- Product ID (primary key)
- SKU (Stock Keeping Unit)
- Product Name
- Description
- Keywords (for search)
- Category ID (foreign key)
- Sub-Category ID (foreign key)
- Base Price
- Status (Active/Inactive)
- Created Date
- Updated Date

### 2.3 Product Variant
**Attributes**:
- Variant ID (primary key)
- Product ID (foreign key)
- Size
- Color
- Additional Price (if variant affects price)
- Stock Quantity
- Status (Active/Inactive)

### 2.4 Product Image
**Attributes**:
- Image ID (primary key)
- Product ID (foreign key)
- Image URL
- Is Thumbnail (boolean)
- Display Order
- Alt Text

### 2.5 Category
**Attributes**:
- Category ID (primary key)
- Category Name
- Description
- Parent Category ID (null for top-level)
- Status (Active/Inactive)
- Display Order

### 2.6 Shopping Cart
**Attributes**:
- Cart ID (primary key)
- User ID (foreign key)
- Created Date
- Updated Date
- Status (Active/Converted/Abandoned)

### 2.7 Cart Item
**Attributes**:
- Cart Item ID (primary key)
- Cart ID (foreign key)
- Product ID (foreign key)
- Variant ID (foreign key)
- Quantity
- Unit Price
- Subtotal
- Added Date

### 2.8 Wishlist
**Attributes**:
- Wishlist ID (primary key)
- User ID (foreign key)
- Product ID (foreign key)
- Variant ID (foreign key)
- Added Date

### 2.9 Order
**Attributes**:
- Order ID (primary key)
- User ID (foreign key)
- Order Number (unique, user-facing)
- Order Date
- Order Status (Open/Confirmed/In Process/Shipped/Delivered)
- Item Total
- Subtotal
- Shipping Cost
- Tax
- Order Total
- Payment Status
- Billing Address ID (foreign key)
- Shipping Address ID (foreign key)
- Created Date
- Updated Date

### 2.10 Order Item
**Attributes**:
- Order Item ID (primary key)
- Order ID (foreign key)
- Product ID (foreign key)
- Variant ID (foreign key)
- Quantity
- Unit Price
- Subtotal
- Product Name (snapshot at order time)
- Variant Details (snapshot at order time)

### 2.11 Address
**Attributes**:
- Address ID (primary key)
- User ID (foreign key)
- Address Type (Billing/Shipping)
- Address Line 1
- Address Line 2
- City
- State
- ZIP Code
- Country (default: USA)
- Is Default (boolean)

### 2.12 Payment
**Attributes**:
- Payment ID (primary key)
- Order ID (foreign key)
- Payment Method (Credit Card/Debit Card/Net Banking)
- Payment Gateway (Stripe)
- Transaction ID
- Amount
- Payment Status (Pending/Completed/Failed)
- Payment Date
- Payment Details (encrypted)

### 2.13 Shipment
**Attributes**:
- Shipment ID (primary key)
- Order ID (foreign key)
- Shipping Carrier
- Tracking ID
- Shipment Status
- Shipped Date
- Estimated Delivery Date
- Actual Delivery Date
- Shipping Cost
- Delivery Address ID (foreign key)

### 2.14 Review/Rating
**Attributes**:
- Review ID (primary key)
- Product ID (foreign key)
- User ID (foreign key)
- Order ID (foreign key - proves purchase)
- Rating (1-5 stars)
- Review Title
- Review Text
- Review Date
- Approval Status (Pending/Approved/Rejected)
- Admin Notes

### 2.15 CMS Page
**Attributes**:
- Page ID (primary key)
- Page Name (About Us/Contact Us/Privacy Policy/Terms)
- Page Content (HTML)
- Last Updated Date
- Updated By (Admin User ID)

---

## 3. System Components (8 components)

### 3.1 Frontend Website
- **Technology**: Web-based (responsive)
- **Users**: Visitors, Buyers
- **Functions**: Product browsing, search, cart, checkout, account management

### 3.2 Admin Panel (Backend)
- **Technology**: Web-based admin interface
- **Users**: Admin, Sub-Admin
- **Functions**: Product management, order management, user management, reporting

### 3.3 Authentication Service
- **Functions**: Login, registration, password reset, social login (Facebook/Google)
- **Security**: Email verification, password encryption

### 3.4 Product Catalog Service
- **Functions**: Product search, filtering, sorting, category navigation

### 3.5 Order Management Service
- **Functions**: Cart management, order placement, order tracking, status updates

### 3.6 Payment Gateway Integration
- **Provider**: Stripe
- **Functions**: Payment processing, transaction management, refund handling

### 3.7 Shipping Service
- **Functions**: Shipping availability check (by ZIP code), shipping cost calculation, tracking integration

### 3.8 Email Notification Service
- **Functions**: Email verification, order confirmation, order status updates, promotional emails

---

## 4. Primary User Flows (10 flows)

### Flow 1: New Buyer Registration
**Actors**: Visitor → Buyer
**Steps**:
1. Visitor navigates to registration page
2. Fills registration form (first name, last name, email, contact number, password, confirm password)
3. Accepts terms and conditions
4. Submits registration
5. System creates account with email verification pending status
6. System sends verification email with link
7. User clicks verification link in email
8. Email verified, account activated
9. User can now login

**Requirements**: FR-002
**Success Criteria**: User account created, email verified, can login

### Flow 2: Buyer Login
**Actors**: Buyer
**Steps**:
1. Buyer navigates to login page
2. Option A: Email/Password login
   - Enters email and password
   - System authenticates
   - Redirects to homepage or cart
3. Option B: Social Login (Facebook/Google)
   - Clicks social login button
   - Redirects to social provider
   - Grants permissions
   - Returns to website, auto-logged in
4. Option C: Forgot Password
   - Clicks forgot password
   - Enters email
   - Receives password reset link
   - Creates new password
   - Logs in with new password

**Requirements**: FR-001
**Success Criteria**: User authenticated and logged in

### Flow 3: Product Search and Browse
**Actors**: Visitor/Buyer
**Steps**:
1. User lands on homepage
2. Option A: Keyword Search
   - Enters search keyword in search box
   - Clicks search
   - Views search results (product listing)
3. Option B: Category Navigation
   - Clicks on category
   - Views products in category
   - Optionally clicks sub-category
   - Views refined product listing
4. Applies filters (price, size, color, etc.)
5. Applies sorting (price, popularity, newest, etc.)
6. Views filtered and sorted product listing

**Requirements**: FR-003, FR-004
**Success Criteria**: User sees relevant product listing

### Flow 4: View Product Details
**Actors**: Visitor/Buyer
**Steps**:
1. User clicks on product from listing
2. Product detail page loads
3. User views:
   - Product images (thumbnail and gallery)
   - Product name and description
   - Price
   - Available variants (size, color)
   - Ratings and reviews
4. User enters ZIP code to check shipping availability
5. System displays shipping availability and cost
6. User can:
   - Add to cart (login required)
   - Add to wishlist (login required)
   - Share on social media (no login required)

**Requirements**: FR-005, FR-009
**Success Criteria**: User views complete product information

### Flow 5: Add to Cart and Checkout
**Actors**: Buyer (must be logged in)
**Steps**:
1. Buyer selects product variant (size, color)
2. Selects quantity
3. Clicks "Add to Cart"
4. System adds item to shopping cart
5. Buyer can:
   - Continue shopping (return to listing)
   - View cart
6. From cart page:
   - Update quantities
   - Remove items
   - View item prices, subtotal, total
7. Click "Proceed to Checkout"
8. Enter/select billing address
9. Enter/select shipping address
10. View order summary (items, subtotal, shipping, tax, total)
11. Select payment method (credit/debit card or net banking)
12. Enter payment details
13. Submit payment
14. Payment gateway processes payment
15. Order confirmed
16. Receive order confirmation email
17. View order in order history

**Requirements**: FR-007, FR-008, FR-012
**Success Criteria**: Order placed successfully, payment processed, confirmation received

### Flow 6: Manage Wishlist
**Actors**: Buyer (must be logged in)
**Steps**:
1. Buyer views product details
2. Clicks "Add to Wishlist"
3. Product added to wishlist
4. Buyer navigates to My Account → Wishlist
5. Views all wishlist items
6. Can:
   - Remove items from wishlist
   - Add items from wishlist to cart
   - Proceed to checkout from wishlist

**Requirements**: FR-006
**Success Criteria**: Buyer manages wishlist items

### Flow 7: Order Tracking
**Actors**: Buyer
**Steps**:
1. Buyer logs in
2. Navigates to My Account → My Orders
3. Views list of all past and current orders
4. Clicks on specific order
5. Views order details:
   - Items ordered
   - Quantities and prices
   - Total amount paid
   - Shipping address
   - Order status (Open/Confirmed/In Process/Shipped/Delivered)
   - Tracking information (if shipped)
6. Can reorder same items

**Requirements**: FR-012
**Success Criteria**: Buyer views order status and details

### Flow 8: Post Review and Rating
**Actors**: Buyer (must have purchased product)
**Steps**:
1. Buyer navigates to My Orders
2. Finds ordered product
3. Clicks "Write Review"
4. Selects rating (1-5 stars)
5. Writes review title and text
6. Submits review
7. Review sent to admin for approval
8. Admin approves review
9. Review appears on product page

**Requirements**: FR-011, FR-021
**Success Criteria**: Review posted and approved

### Flow 9: Admin Order Management
**Actors**: Admin/Sub-Admin
**Steps**:
1. Admin logs into admin panel
2. Navigates to Orders Management
3. Views list of all orders with current status
4. Filters/searches for specific order
5. Clicks on order to view details
6. Can edit order details
7. Updates order status:
   - Open → Confirmed → In Process → Shipped → Delivered
8. For shipped orders:
   - Enters shipping carrier
   - Enters tracking ID
   - Enters shipment status
   - System sends status update email to buyer
9. Buyer receives notification

**Requirements**: FR-017
**Success Criteria**: Order status updated, buyer notified

### Flow 10: Admin Product Management
**Actors**: Admin/Sub-Admin
**Steps**:
1. Admin logs into admin panel
2. Navigates to Product Categories Management
3. Creates/edits categories and sub-categories
4. Navigates to Products Management
5. Creates new product:
   - Enters product name, description, keywords
   - Selects category and sub-category
   - Sets base price
   - Uploads product images (thumbnail and gallery)
   - Adds variants (sizes, colors)
   - Sets product status (Active/Inactive)
6. Saves product
7. Product appears on frontend website
8. Can edit/deactivate product later

**Requirements**: FR-018, FR-019
**Success Criteria**: Product created and visible on website

---

## 5. Data Flow Summary

### 5.1 Buyer Journey Data Flow
```
Visitor → Registration → Email Verification → Login →
Browse Products → Search/Filter → View Details →
Add to Cart → Checkout → Payment → Order Confirmation →
Order Tracking → Delivery → Review
```

### 5.2 Admin Management Data Flow
```
Admin Login → Dashboard (View Analytics) →
Manage Products/Categories →
Manage Orders (Update Status, Ship) →
Manage Customers (View, Activate/Deactivate) →
Manage Payments →
Approve Reviews →
Generate Reports →
Manage CMS Content
```

### 5.3 Payment Data Flow
```
Cart → Checkout → Payment Method Selection →
Payment Details → Stripe Gateway →
Transaction Processing → Payment Confirmation →
Order Status Update → Email Notification
```

### 5.4 Shipping Data Flow
```
Order Placed → Order Confirmed → Order In Process →
Admin Updates Shipment Details → Order Shipped →
Tracking Info Added → Buyer Notified →
Delivery Status Updated → Order Delivered
```

---

## 6. Integration Points

### 6.1 External Services
1. **Stripe Payment Gateway**: Payment processing for credit/debit cards and net banking
2. **Facebook OAuth**: Social login authentication
3. **Google OAuth**: Social login authentication
4. **Email Service Provider**: Sending transactional and promotional emails
5. **Shipping Carrier API**: ZIP code validation, shipping cost calculation, tracking integration

### 6.2 Internal Integrations
1. **Frontend ↔ Backend API**: RESTful or GraphQL API for data exchange
2. **Admin Panel ↔ Database**: Direct database operations for management
3. **Authentication Service ↔ User Database**: User verification and session management
4. **Order Service ↔ Payment Service**: Order payment processing
5. **Order Service ↔ Inventory Service**: Stock management

---

## Summary

**Entities Identified**: 15 core entities
- 4 User/Role entities
- 11 Data entities (Product, Order, Cart, Wishlist, Payment, Shipment, Review, Category, Address, CMS, Images)

**Flows Identified**: 10 primary flows
- 8 Buyer-facing flows (Registration, Login, Search, Browse, Cart, Checkout, Order Tracking, Reviews)
- 2 Admin flows (Order Management, Product Management)

**System Components**: 8 components
- Frontend, Admin Panel, Authentication, Product Catalog, Order Management, Payment, Shipping, Email

**Integration Points**: 5 external + 5 internal

This entity and flow analysis provides the foundation for deriving comprehensive test scenarios in the next step.
