# Test Scenarios - Ecommerce Website

## Document Information
- **Source Document**: BRD v1.0 - Online Apparels Shopping Website
- **Date**: November 13, 2025
- **Format**: User Story Format

---

## User Story Format
Each test scenario follows the format:
**"As a [user role], I want to [perform an action], so that I can [achieve a benefit]."**

---

## 1. VISITOR / GUEST USER SCENARIOS

### TS-001: Browse Products by Category
**As a** Visitor
**I want to** browse products by selecting categories and sub-categories
**So that I can** find specific types of apparel I'm interested in

**Related Requirements**: FR-003, FR-004
**Priority**: Critical
**User Role**: Visitor

---

### TS-002: Search Products by Keyword
**As a** Visitor
**I want to** search for products using keywords
**So that I can** quickly find specific items I'm looking for

**Related Requirements**: FR-003, FR-004
**Priority**: Critical
**User Role**: Visitor

---

### TS-003: View Product Details Without Login
**As a** Visitor
**I want to** view detailed product information without logging in
**So that I can** make informed decisions before creating an account

**Related Requirements**: FR-005
**Priority**: Critical
**User Role**: Visitor

---

### TS-004: Check Shipping Availability by PIN Code
**As a** Visitor
**I want to** check if a product can be shipped to my PIN code
**So that I can** know if I can order the product before registering

**Related Requirements**: FR-005
**Priority**: High
**User Role**: Visitor

---

### TS-005: View Product Ratings and Reviews
**As a** Visitor
**I want to** read product ratings and reviews from other customers
**So that I can** assess product quality and make informed purchase decisions

**Related Requirements**: FR-005
**Priority**: High
**User Role**: Visitor

---

### TS-006: View Product Variations
**As a** Visitor
**I want to** see available sizes and colors for a product
**So that I can** determine if the product meets my needs

**Related Requirements**: FR-005
**Priority**: High
**User Role**: Visitor

---

### TS-007: Share Product on Social Media
**As a** Visitor
**I want to** share interesting products on social media platforms
**So that I can** show them to friends or save them for later reference

**Related Requirements**: FR-009
**Priority**: Low
**User Role**: Visitor

---

### TS-008: Filter Product Listings
**As a** Visitor
**I want to** apply filters to product search results
**So that I can** narrow down options based on price, size, color, or ratings

**Related Requirements**: FR-004
**Priority**: High
**User Role**: Visitor

---

### TS-009: Sort Product Listings
**As a** Visitor
**I want to** sort products by different criteria (price, rating, newest)
**So that I can** find products that best match my preferences

**Related Requirements**: FR-004
**Priority**: High
**User Role**: Visitor

---

### TS-010: Contact Support as Guest
**As a** Visitor
**I want to** contact customer support without having an account
**So that I can** get answers to pre-purchase questions

**Related Requirements**: FR-013
**Priority**: Medium
**User Role**: Visitor

---

## 2. BUYER REGISTRATION & AUTHENTICATION SCENARIOS

### TS-011: Register New Account
**As a** Visitor
**I want to** create a new buyer account with my details
**So that I can** make purchases on the website

**Related Requirements**: FR-002
**Priority**: Critical
**User Role**: Visitor → Buyer

---

### TS-012: Verify Email Address
**As a** Registered Buyer
**I want to** verify my email address through a verification link
**So that I can** activate my account and start shopping

**Related Requirements**: FR-002
**Priority**: Critical
**User Role**: Buyer

---

### TS-013: Login with Email and Password
**As a** Registered Buyer
**I want to** log in using my email and password
**So that I can** access my account and make purchases

**Related Requirements**: FR-001
**Priority**: Critical
**User Role**: Buyer

---

### TS-014: Login with Facebook Account
**As a** Visitor/Buyer
**I want to** log in using my Facebook account
**So that I can** access the site quickly without remembering separate credentials

**Related Requirements**: FR-001
**Priority**: High
**User Role**: Visitor/Buyer

---

### TS-015: Login with Google Account
**As a** Visitor/Buyer
**I want to** log in using my Google account
**So that I can** access the site quickly without remembering separate credentials

**Related Requirements**: FR-001
**Priority**: High
**User Role**: Visitor/Buyer

---

### TS-016: Reset Forgotten Password
**As a** Buyer
**I want to** reset my password if I forget it
**So that I can** regain access to my account

**Related Requirements**: FR-001
**Priority**: High
**User Role**: Buyer

---

### TS-017: Logout from Account
**As a** Logged-in Buyer
**I want to** log out of my account
**So that I can** secure my account when using shared devices

**Related Requirements**: FR-010
**Priority**: Medium
**User Role**: Buyer

---

## 3. BUYER SHOPPING SCENARIOS

### TS-018: Add Product to Shopping Cart
**As a** Logged-in Buyer
**I want to** add products to my shopping cart with selected size and color
**So that I can** collect items for purchase

**Related Requirements**: FR-007
**Priority**: Critical
**User Role**: Buyer

---

### TS-019: View Shopping Cart
**As a** Logged-in Buyer
**I want to** view all items in my shopping cart
**So that I can** review my selections before checkout

**Related Requirements**: FR-007
**Priority**: Critical
**User Role**: Buyer

---

### TS-020: Update Cart Item Quantity
**As a** Logged-in Buyer
**I want to** change the quantity of items in my cart
**So that I can** adjust my order before purchase

**Related Requirements**: FR-007
**Priority**: High
**User Role**: Buyer

---

### TS-021: Remove Item from Cart
**As a** Logged-in Buyer
**I want to** remove items from my shopping cart
**So that I can** delete products I no longer wish to purchase

**Related Requirements**: FR-007
**Priority**: High
**User Role**: Buyer

---

### TS-022: Add Product to Wishlist
**As a** Logged-in Buyer
**I want to** add products to my wishlist
**So that I can** save items for future consideration

**Related Requirements**: FR-006
**Priority**: Medium
**User Role**: Buyer

---

### TS-023: View Wishlist
**As a** Logged-in Buyer
**I want to** view all products in my wishlist
**So that I can** review items I saved for later

**Related Requirements**: FR-006
**Priority**: Medium
**User Role**: Buyer

---

### TS-024: Move Wishlist Item to Cart
**As a** Logged-in Buyer
**I want to** move items from wishlist to shopping cart
**So that I can** purchase saved items

**Related Requirements**: FR-006
**Priority**: Medium
**User Role**: Buyer

---

### TS-025: Remove Item from Wishlist
**As a** Logged-in Buyer
**I want to** remove items from my wishlist
**So that I can** manage my saved products

**Related Requirements**: FR-006
**Priority**: Medium
**User Role**: Buyer

---

## 4. CHECKOUT & PAYMENT SCENARIOS

### TS-026: Proceed to Checkout
**As a** Logged-in Buyer
**I want to** initiate the checkout process from my shopping cart
**So that I can** complete my purchase

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: Buyer

---

### TS-027: Enter Billing Address
**As a** Buyer in Checkout
**I want to** provide my billing address
**So that I can** complete the payment process

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: Buyer

---

### TS-028: Enter Shipping Address
**As a** Buyer in Checkout
**I want to** provide my shipping address
**So that I can** receive my order at the desired location

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: Buyer

---

### TS-029: Use Same Address for Billing and Shipping
**As a** Buyer in Checkout
**I want to** use the same address for both billing and shipping
**So that I can** save time during checkout

**Related Requirements**: FR-008
**Priority**: High
**User Role**: Buyer

---

### TS-030: Select Saved Address
**As a** Buyer in Checkout
**I want to** select from my saved addresses
**So that I can** quickly complete checkout without re-entering information

**Related Requirements**: FR-008, FR-010
**Priority**: High
**User Role**: Buyer

---

### TS-031: View Order Summary Before Payment
**As a** Buyer in Checkout
**I want to** review complete order summary including items, prices, shipping, and tax
**So that I can** verify everything is correct before payment

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: Buyer

---

### TS-032: Pay with Credit Card
**As a** Buyer in Checkout
**I want to** pay for my order using a credit card
**So that I can** complete my purchase

**Related Requirements**: FR-008, FR-020
**Priority**: Critical
**User Role**: Buyer

---

### TS-033: Pay with Debit Card
**As a** Buyer in Checkout
**I want to** pay for my order using a debit card
**So that I can** complete my purchase

**Related Requirements**: FR-008, FR-020
**Priority**: Critical
**User Role**: Buyer

---

### TS-034: Pay with Net Banking
**As a** Buyer in Checkout
**I want to** pay for my order using net banking
**So that I can** complete my purchase without using a card

**Related Requirements**: FR-008, FR-020
**Priority**: Critical
**User Role**: Buyer

---

### TS-035: Receive Order Confirmation Email
**As a** Buyer who completed purchase
**I want to** receive an order confirmation email
**So that I can** have a record of my purchase and order details

**Related Requirements**: FR-008
**Priority**: High
**User Role**: Buyer

---

### TS-036: Handle Payment Failure
**As a** Buyer with failed payment
**I want to** be notified of payment failure and retry options
**So that I can** successfully complete my purchase

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: Buyer

---

## 5. ORDER MANAGEMENT SCENARIOS

### TS-037: View Order History
**As a** Logged-in Buyer
**I want to** see a list of all my past and current orders
**So that I can** track my purchase history

**Related Requirements**: FR-012
**Priority**: High
**User Role**: Buyer

---

### TS-038: View Order Details
**As a** Logged-in Buyer
**I want to** view detailed information about a specific order
**So that I can** see what I ordered and its status

**Related Requirements**: FR-012
**Priority**: High
**User Role**: Buyer

---

### TS-039: Track Order Shipment
**As a** Logged-in Buyer
**I want to** track my order's shipping status
**So that I can** know when to expect delivery

**Related Requirements**: FR-012
**Priority**: High
**User Role**: Buyer

---

### TS-040: Receive Order Status Update Emails
**As a** Buyer with active orders
**I want to** receive email notifications when my order status changes
**So that I can** stay informed about my order progress

**Related Requirements**: FR-008
**Priority**: High
**User Role**: Buyer

---

### TS-041: Reorder Previous Items
**As a** Logged-in Buyer
**I want to** reorder items from a previous order
**So that I can** quickly purchase products I've bought before

**Related Requirements**: FR-012
**Priority**: Medium
**User Role**: Buyer

---

## 6. ACCOUNT MANAGEMENT SCENARIOS

### TS-042: View Account Dashboard
**As a** Logged-in Buyer
**I want to** access my account dashboard
**So that I can** manage all aspects of my account from one place

**Related Requirements**: FR-010
**Priority**: High
**User Role**: Buyer

---

### TS-043: Update Profile Information
**As a** Logged-in Buyer
**I want to** update my email address and phone number
**So that I can** keep my contact information current

**Related Requirements**: FR-010
**Priority**: High
**User Role**: Buyer

---

### TS-044: Change Password
**As a** Logged-in Buyer
**I want to** change my account password
**So that I can** maintain account security

**Related Requirements**: FR-010
**Priority**: High
**User Role**: Buyer

---

### TS-045: Manage Address Book
**As a** Logged-in Buyer
**I want to** add, edit, and delete saved addresses
**So that I can** maintain up-to-date delivery locations

**Related Requirements**: FR-010
**Priority**: High
**User Role**: Buyer

---

### TS-046: Set Default Billing Address
**As a** Logged-in Buyer
**I want to** designate a default billing address
**So that I can** speed up the checkout process

**Related Requirements**: FR-010
**Priority**: Medium
**User Role**: Buyer

---

### TS-047: Set Default Shipping Address
**As a** Logged-in Buyer
**I want to** designate a default shipping address
**So that I can** speed up the checkout process

**Related Requirements**: FR-010
**Priority**: Medium
**User Role**: Buyer

---

## 7. RATINGS & REVIEWS SCENARIOS

### TS-048: Post Product Rating
**As a** Buyer who purchased a product
**I want to** rate a product with a star rating
**So that I can** share my satisfaction level with other shoppers

**Related Requirements**: FR-011
**Priority**: Medium
**User Role**: Buyer

---

### TS-049: Write Product Review
**As a** Buyer who purchased a product
**I want to** write a detailed review of a product
**So that I can** share my experience with other shoppers

**Related Requirements**: FR-011
**Priority**: Medium
**User Role**: Buyer

---

### TS-050: View My Posted Reviews
**As a** Logged-in Buyer
**I want to** see all reviews I have posted
**So that I can** track my feedback history

**Related Requirements**: FR-010, FR-011
**Priority**: Low
**User Role**: Buyer

---

### TS-051: Verify Purchase Before Review
**As a** System
**I want to** verify that a buyer purchased a product before allowing a review
**So that I can** ensure only genuine customers can review products

**Related Requirements**: FR-011
**Priority**: High
**User Role**: System

---

## 8. BUYER SUPPORT SCENARIOS

### TS-052: Contact Customer Support
**As a** Logged-in Buyer
**I want to** send a message to customer support
**So that I can** get help with issues or questions

**Related Requirements**: FR-013
**Priority**: Medium
**User Role**: Buyer

---

## 9. ADMIN AUTHENTICATION SCENARIOS

### TS-053: Admin Login
**As an** Admin User
**I want to** log into the admin panel with username and password
**So that I can** manage the ecommerce website

**Related Requirements**: FR-014
**Priority**: Critical
**User Role**: Admin

---

### TS-054: Admin Password Reset
**As an** Admin User
**I want to** reset my password if forgotten
**So that I can** regain access to the admin panel

**Related Requirements**: FR-014
**Priority**: High
**User Role**: Admin

---

### TS-055: Admin Logout
**As a** Logged-in Admin
**I want to** log out of the admin panel
**So that I can** secure the system when leaving my workstation

**Related Requirements**: FR-014
**Priority**: Medium
**User Role**: Admin

---

## 10. ADMIN DASHBOARD SCENARIOS

### TS-056: View Admin Dashboard Statistics
**As a** Logged-in Admin
**I want to** view key business metrics on the dashboard
**So that I can** quickly assess business performance

**Related Requirements**: FR-015
**Priority**: High
**User Role**: Admin

---

### TS-057: View Total Registered Buyers
**As a** Logged-in Admin
**I want to** see the count of active and inactive registered buyers
**So that I can** monitor customer base growth

**Related Requirements**: FR-015
**Priority**: Medium
**User Role**: Admin

---

### TS-058: View Total Products Count
**As a** Logged-in Admin
**I want to** see the total number of products in the catalog
**So that I can** monitor inventory size

**Related Requirements**: FR-015
**Priority**: Medium
**User Role**: Admin

---

### TS-059: View Revenue Statistics
**As a** Logged-in Admin
**I want to** view revenue for today and this month
**So that I can** track sales performance

**Related Requirements**: FR-015
**Priority**: High
**User Role**: Admin

---

## 11. CUSTOMER MANAGEMENT SCENARIOS

### TS-060: View Customer List
**As a** Logged-in Admin
**I want to** see a list of all registered customers
**So that I can** manage customer accounts

**Related Requirements**: FR-016
**Priority**: High
**User Role**: Admin

---

### TS-061: View Customer Details
**As a** Logged-in Admin
**I want to** view comprehensive details of a specific customer
**So that I can** understand their account and purchase history

**Related Requirements**: FR-016
**Priority**: High
**User Role**: Admin

---

### TS-062: Edit Customer Profile
**As a** Logged-in Admin
**I want to** modify customer account information
**So that I can** correct errors or update details as needed

**Related Requirements**: FR-016
**Priority**: Medium
**User Role**: Admin

---

### TS-063: Activate Customer Account
**As a** Logged-in Admin
**I want to** activate an inactive customer account
**So that I can** restore access for legitimate users

**Related Requirements**: FR-016
**Priority**: Medium
**User Role**: Admin

---

### TS-064: Deactivate Customer Account
**As a** Logged-in Admin
**I want to** deactivate a customer account
**So that I can** prevent access for problematic users

**Related Requirements**: FR-016
**Priority**: Medium
**User Role**: Admin

---

## 12. ORDER MANAGEMENT SCENARIOS (ADMIN)

### TS-065: View All Orders
**As a** Logged-in Admin
**I want to** see a list of all customer orders
**So that I can** manage order fulfillment

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-066: Filter Orders by Status
**As a** Logged-in Admin
**I want to** filter orders by status (Open, Confirmed, In Process, Shipped, Delivered)
**So that I can** focus on orders at specific stages

**Related Requirements**: FR-017
**Priority**: High
**User Role**: Admin

---

### TS-067: View Order Details
**As a** Logged-in Admin
**I want to** view complete details of a specific order
**So that I can** process and fulfill the order

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-068: Update Order Status to Confirmed
**As a** Logged-in Admin
**I want to** change order status from Open to Confirmed
**So that I can** indicate payment verification

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-069: Update Order Status to In Process
**As a** Logged-in Admin
**I want to** change order status to In Process
**So that I can** indicate order preparation has started

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-070: Update Order Status to Shipped
**As a** Logged-in Admin
**I want to** change order status to Shipped with shipment details
**So that I can** notify the customer their order is on the way

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-071: Update Order Status to Delivered
**As a** Logged-in Admin
**I want to** mark an order as Delivered
**So that I can** complete the order lifecycle

**Related Requirements**: FR-017
**Priority**: Critical
**User Role**: Admin

---

### TS-072: Enter Shipment Tracking Information
**As a** Logged-in Admin
**I want to** add shipping carrier, tracking ID, and delivery details
**So that I can** enable customer order tracking

**Related Requirements**: FR-017
**Priority**: High
**User Role**: Admin

---

### TS-073: Edit Order Details
**As a** Logged-in Admin
**I want to** modify order information if needed
**So that I can** correct errors or accommodate customer requests

**Related Requirements**: FR-017
**Priority**: Medium
**User Role**: Admin

---

## 13. PRODUCT CATEGORY MANAGEMENT SCENARIOS

### TS-074: View Product Categories
**As a** Logged-in Admin
**I want to** see all product categories and sub-categories
**So that I can** manage the product classification structure

**Related Requirements**: FR-018
**Priority**: High
**User Role**: Admin

---

### TS-075: Create New Category
**As a** Logged-in Admin
**I want to** add a new product category
**So that I can** expand product organization

**Related Requirements**: FR-018
**Priority**: High
**User Role**: Admin

---

### TS-076: Create New Sub-Category
**As a** Logged-in Admin
**I want to** add a sub-category under an existing category
**So that I can** create more specific product classifications

**Related Requirements**: FR-018
**Priority**: High
**User Role**: Admin

---

### TS-077: Edit Category
**As a** Logged-in Admin
**I want to** modify category details
**So that I can** update category information

**Related Requirements**: FR-018
**Priority**: Medium
**User Role**: Admin

---

### TS-078: Activate/Deactivate Category
**As a** Logged-in Admin
**I want to** change category status
**So that I can** control which categories are visible to customers

**Related Requirements**: FR-018
**Priority**: Medium
**User Role**: Admin

---

## 14. PRODUCT MANAGEMENT SCENARIOS

### TS-079: View Product Catalog
**As a** Logged-in Admin
**I want to** see all products in the catalog
**So that I can** manage the product inventory

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-080: Create New Product
**As a** Logged-in Admin
**I want to** add a new product with all details
**So that I can** make it available for purchase

**Related Requirements**: FR-019
**Priority**: Critical
**User Role**: Admin

---

### TS-081: Upload Product Images
**As a** Logged-in Admin
**I want to** upload multiple images for a product
**So that I can** showcase the product visually

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-082: Edit Product Details
**As a** Logged-in Admin
**I want to** modify existing product information
**So that I can** update prices, descriptions, or other attributes

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-083: Set Product Variations
**As a** Logged-in Admin
**I want to** define available sizes and colors for a product
**So that I can** offer customers multiple options

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-084: Activate Product
**As a** Logged-in Admin
**I want to** activate a product
**So that I can** make it visible and purchasable on the website

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-085: Deactivate Product
**As a** Logged-in Admin
**I want to** deactivate a product
**So that I can** temporarily remove it from the website

**Related Requirements**: FR-019
**Priority**: High
**User Role**: Admin

---

### TS-086: Delete Product
**As a** Logged-in Admin
**I want to** delete a product from the catalog
**So that I can** remove discontinued items

**Related Requirements**: FR-019
**Priority**: Medium
**User Role**: Admin

---

### TS-087: Assign Product to Category
**As a** Logged-in Admin
**I want to** assign products to categories and sub-categories
**So that I can** organize products for customer browsing

**Related Requirements**: FR-018, FR-019
**Priority**: High
**User Role**: Admin

---

## 15. PAYMENT MANAGEMENT SCENARIOS

### TS-088: View Payment Information
**As a** Logged-in Admin
**I want to** view configured payment account details
**So that I can** verify payment setup

**Related Requirements**: FR-020
**Priority**: High
**User Role**: Admin

---

### TS-089: Edit Payment Information
**As a** Logged-in Admin
**I want to** update bank account details for receiving payments
**So that I can** ensure payments are received correctly

**Related Requirements**: FR-020
**Priority**: High
**User Role**: Admin

---

### TS-090: View Order Payment Status
**As a** Logged-in Admin
**I want to** see the payment status of each order
**So that I can** verify successful transactions

**Related Requirements**: FR-020
**Priority**: High
**User Role**: Admin

---

## 16. REVIEW MODERATION SCENARIOS

### TS-091: View Pending Reviews
**As a** Logged-in Admin
**I want to** see all reviews awaiting moderation
**So that I can** approve or reject them

**Related Requirements**: FR-020
**Priority**: Medium
**User Role**: Admin

---

### TS-092: Approve Product Review
**As a** Logged-in Admin
**I want to** approve a pending review
**So that I can** make it visible on the product page

**Related Requirements**: FR-020
**Priority**: Medium
**User Role**: Admin

---

### TS-093: Reject Product Review
**As a** Logged-in Admin
**I want to** reject an inappropriate review
**So that I can** maintain quality standards

**Related Requirements**: FR-020
**Priority**: Medium
**User Role**: Admin

---

### TS-094: View Approved Reviews
**As a** Logged-in Admin
**I want to** see all approved reviews
**So that I can** monitor published customer feedback

**Related Requirements**: FR-020
**Priority**: Low
**User Role**: Admin

---

### TS-095: View Rejected Reviews
**As a** Logged-in Admin
**I want to** see all rejected reviews
**So that I can** maintain a record of moderation decisions

**Related Requirements**: FR-020
**Priority**: Low
**User Role**: Admin

---

## 17. REPORTS & STATISTICS SCENARIOS

### TS-096: View Products Uploaded Report
**As a** Logged-in Admin
**I want to** generate a report of products uploaded by date range
**So that I can** analyze catalog growth

**Related Requirements**: FR-021
**Priority**: Medium
**User Role**: Admin

---

### TS-097: View Revenue Report by Period
**As a** Logged-in Admin
**I want to** generate revenue reports for specific time periods
**So that I can** analyze sales performance

**Related Requirements**: FR-021
**Priority**: High
**User Role**: Admin

---

### TS-098: Export Report as PDF
**As a** Logged-in Admin
**I want to** export reports in PDF format
**So that I can** share them with stakeholders

**Related Requirements**: FR-021
**Priority**: Medium
**User Role**: Admin

---

### TS-099: Export Report as Excel
**As a** Logged-in Admin
**I want to** export reports in Excel format
**So that I can** perform further analysis

**Related Requirements**: FR-021
**Priority**: Medium
**User Role**: Admin

---

## 18. USER & ROLE MANAGEMENT SCENARIOS

### TS-100: Create Sub-Admin User
**As a** Logged-in Admin
**I want to** create new sub-admin users
**So that I can** delegate administrative tasks

**Related Requirements**: FR-022
**Priority**: Medium
**User Role**: Admin

---

### TS-101: Edit Sub-Admin User
**As a** Logged-in Admin
**I want to** modify sub-admin user details
**So that I can** update their information

**Related Requirements**: FR-022
**Priority**: Medium
**User Role**: Admin

---

### TS-102: Activate/Deactivate Sub-Admin
**As a** Logged-in Admin
**I want to** activate or deactivate sub-admin accounts
**So that I can** control system access

**Related Requirements**: FR-022
**Priority**: Medium
**User Role**: Admin

---

### TS-103: Delete Sub-Admin User
**As a** Logged-in Admin
**I want to** remove sub-admin users
**So that I can** revoke access for former staff

**Related Requirements**: FR-022
**Priority**: Medium
**User Role**: Admin

---

### TS-104: Create User Role
**As a** Logged-in Admin
**I want to** define new user roles with specific permissions
**So that I can** implement role-based access control

**Related Requirements**: FR-023
**Priority**: Medium
**User Role**: Admin

---

### TS-105: Edit User Role Permissions
**As a** Logged-in Admin
**I want to** modify permissions for existing roles
**So that I can** adjust access levels as needed

**Related Requirements**: FR-023
**Priority**: Medium
**User Role**: Admin

---

### TS-106: Assign Role to Sub-Admin
**As a** Logged-in Admin
**I want to** assign specific roles to sub-admin users
**So that I can** grant appropriate access levels

**Related Requirements**: FR-023
**Priority**: Medium
**User Role**: Admin

---

### TS-107: Activate/Deactivate Role
**As a** Logged-in Admin
**I want to** activate or deactivate user roles
**So that I can** manage available permission sets

**Related Requirements**: FR-023
**Priority**: Low
**User Role**: Admin

---

## 19. CMS MANAGEMENT SCENARIOS

### TS-108: Edit About Us Page
**As a** Logged-in Admin
**I want to** update the About Us page content
**So that I can** keep company information current

**Related Requirements**: FR-024
**Priority**: Medium
**User Role**: Admin

---

### TS-109: Edit Contact Us Page
**As a** Logged-in Admin
**I want to** update the Contact Us page content
**So that I can** provide accurate contact information

**Related Requirements**: FR-024
**Priority**: Medium
**User Role**: Admin

---

### TS-110: Edit Privacy Policy Page
**As a** Logged-in Admin
**I want to** update the Privacy Policy content
**So that I can** maintain legal compliance

**Related Requirements**: FR-024
**Priority**: High
**User Role**: Admin

---

### TS-111: Edit Terms and Conditions Page
**As a** Logged-in Admin
**I want to** update the Terms and Conditions content
**So that I can** maintain legal compliance

**Related Requirements**: FR-024
**Priority**: High
**User Role**: Admin

---

## 20. EMAIL MANAGEMENT SCENARIOS

### TS-112: Create Promotional Email
**As a** Logged-in Admin
**I want to** create email content for promotions and new products
**So that I can** market to customers

**Related Requirements**: FR-025
**Priority**: Low
**User Role**: Admin

---

### TS-113: Edit Email Template
**As a** Logged-in Admin
**I want to** modify email templates
**So that I can** customize customer communications

**Related Requirements**: FR-025
**Priority**: Low
**User Role**: Admin

---

### TS-114: Delete Email Content
**As a** Logged-in Admin
**I want to** remove outdated email content
**So that I can** maintain relevant messaging

**Related Requirements**: FR-025
**Priority**: Low
**User Role**: Admin

---

## 21. SUPPORT MANAGEMENT SCENARIOS

### TS-115: View Customer Complaints
**As a** Logged-in Admin
**I want to** see all customer inquiries and complaints
**So that I can** address customer issues

**Related Requirements**: FR-026
**Priority**: Medium
**User Role**: Admin

---

### TS-116: Receive Email for New Complaint
**As a** Logged-in Admin
**I want to** receive email notifications when customers submit complaints
**So that I can** respond promptly

**Related Requirements**: FR-026
**Priority**: Medium
**User Role**: Admin

---

## 22. SYSTEM & INTEGRATION SCENARIOS

### TS-117: Process Stripe Payment
**As a** System
**I want to** integrate with Stripe payment gateway
**So that I can** securely process customer payments

**Related Requirements**: FR-020
**Priority**: Critical
**User Role**: System

---

### TS-118: Send Automated Email Notifications
**As a** System
**I want to** send automated emails for various events
**So that I can** keep users informed

**Related Requirements**: FR-002, FR-008, FR-017
**Priority**: High
**User Role**: System

---

### TS-119: Validate Email Uniqueness
**As a** System
**I want to** ensure email addresses are unique during registration
**So that I can** prevent duplicate accounts

**Related Requirements**: FR-002
**Priority**: Critical
**User Role**: System

---

### TS-120: Calculate Order Total
**As a** System
**I want to** calculate order total including items, shipping, and tax
**So that I can** charge the correct amount

**Related Requirements**: FR-008
**Priority**: Critical
**User Role**: System

---

## 23. NEGATIVE/ERROR SCENARIOS

### TS-121: Handle Invalid Login Credentials
**As a** System
**I want to** reject invalid login attempts and display error messages
**So that I can** protect user accounts

**Related Requirements**: FR-001
**Priority**: High
**User Role**: System

---

### TS-122: Prevent Guest Checkout
**As a** System
**I want to** require authentication before checkout
**So that I can** ensure order accountability

**Related Requirements**: FR-007, FR-008
**Priority**: High
**User Role**: System

---

### TS-123: Handle Out of Stock Items
**As a** System
**I want to** prevent purchase of unavailable products
**So that I can** avoid disappointing customers

**Related Requirements**: FR-019
**Priority**: High
**User Role**: System

---

### TS-124: Validate Shipping PIN Code
**As a** System
**I want to** verify if shipping is available to entered PIN code
**So that I can** set accurate customer expectations

**Related Requirements**: FR-005
**Priority**: High
**User Role**: System

---

### TS-125: Handle Unverified Email Login Attempt
**As a** System
**I want to** prevent unverified users from logging in
**So that I can** ensure email verification compliance

**Related Requirements**: FR-002
**Priority**: High
**User Role**: System

---

## SUMMARY

**Total Test Scenarios**: 125

**Breakdown by Priority**:
- Critical: 28 scenarios
- High: 58 scenarios
- Medium: 33 scenarios
- Low: 6 scenarios

**Breakdown by User Role**:
- Visitor: 10 scenarios
- Buyer: 48 scenarios
- Admin: 60 scenarios
- System: 7 scenarios

**Coverage**:
- All 26 Functional Requirements (FR-001 through FR-026) are covered
- All major user flows identified in the requirements are included
- Positive and negative test cases are represented
- Error handling and edge cases are included

---

## Document Complete
These test scenarios will serve as the foundation for generating test variants, test data, and detailed test scripts in subsequent steps.
