# Test Scenarios
## Ecommerce Website - Online Apparels Shopping Platform

**Source**: Requirements (00_requirements.md) and Entities/Flows (02_entities_and_flows.md)
**Generation Date**: November 15, 2025
**Total Scenarios**: 95
**Coverage**: All 31 requirements, all 30 user flows, positive/negative/edge cases

---

## Buyer Registration and Authentication Scenarios

### TS-001: New Buyer Registration with Email Verification
As a visitor, I want to register for a new account with email verification, so that I can access buyer features and make purchases.

**Priority**: Critical
**Related Requirements**: REQ-002

**Details**: User completes registration form with all required fields (first name, last name, email, contact number, password, confirm password) and accepts terms and conditions. System sends email verification link. User clicks link to activate account.

### TS-002: Registration with Invalid Email Format
As a visitor, I want to see validation errors when I enter an invalid email format, so that I can correct it before submitting.

**Priority**: High
**Related Requirements**: REQ-002

**Details**: User attempts registration with invalid email formats (missing @, invalid domain, special characters). System displays validation error and prevents submission.

### TS-003: Registration with Password Mismatch
As a visitor, I want to see an error when password and confirm password don't match, so that I can ensure my password is entered correctly.

**Priority**: High
**Related Requirements**: REQ-002

**Details**: User enters different passwords in password and confirm password fields. System displays mismatch error.

### TS-004: Registration with Existing Email Address
As a visitor, I want to be notified if my email is already registered, so that I can login instead or use a different email.

**Priority**: High
**Related Requirements**: REQ-002

**Details**: User attempts to register with email that already exists in system. System displays "Email already registered" error.

### TS-005: Registration Without Accepting Terms and Conditions
As a visitor, I want to be prevented from registering if I don't accept terms and conditions, so that the system ensures legal compliance.

**Priority**: Medium
**Related Requirements**: REQ-002

**Details**: User completes form but doesn't check "Accept terms and conditions" checkbox. System prevents submission and highlights missing requirement.

### TS-006: Login with Valid Email and Password
As a registered buyer, I want to login with my email and password, so that I can access my account and buyer features.

**Priority**: Critical
**Related Requirements**: REQ-001

**Details**: Buyer enters valid email and password. System authenticates and redirects to home page or previously requested page.

### TS-007: Login with Invalid Credentials
As a visitor, I want to see an error when I enter incorrect login credentials, so that I know my attempt failed.

**Priority**: High
**Related Requirements**: REQ-001

**Details**: User enters incorrect email or password. System displays "Invalid credentials" error without revealing which field is incorrect (security best practice).

### TS-008: Login with Unverified Email
As a registered buyer with unverified email, I want to be reminded to verify my email, so that I can complete the registration process.

**Priority**: High
**Related Requirements**: REQ-001, REQ-002

**Details**: User registered but hasn't clicked email verification link. Login attempt shows "Please verify your email address" message with option to resend verification email.

### TS-009: Social Login with Facebook
As a visitor, I want to login using my Facebook account, so that I can access the site without creating a separate password.

**Priority**: High
**Related Requirements**: REQ-001

**Details**: User clicks "Login with Facebook" button. System redirects to Facebook OAuth. User authorizes app. System creates/links account and logs user in.

### TS-010: Social Login with Google
As a visitor, I want to login using my Google account, so that I can access the site without creating a separate password.

**Priority**: High
**Related Requirements**: REQ-001

**Details**: User clicks "Login with Google" button. System redirects to Google OAuth. User authorizes app. System creates/links account and logs user in.

### TS-011: Password Reset Request
As a buyer, I want to request a password reset, so that I can regain access to my account if I forget my password.

**Priority**: High
**Related Requirements**: REQ-001

**Details**: User clicks "Forgot Password" link, enters registered email. System sends password reset link to email. User clicks link, enters new password, submits. System updates password and redirects to login.

### TS-012: Password Reset with Invalid Email
As a visitor, I want to see a message when I request password reset for non-existent email, so that I know the email isn't registered.

**Priority**: Medium
**Related Requirements**: REQ-001

**Details**: User enters email not in system for password reset. System displays generic message "If this email exists, you will receive a reset link" (security best practice - don't reveal if email exists).

---

## Product Discovery and Browsing Scenarios

### TS-013: Search Products by Keyword as Visitor
As a visitor, I want to search products by keyword without logging in, so that I can browse available items.

**Priority**: Critical
**Related Requirements**: REQ-003, REQ-004

**Details**: Visitor enters keyword in search box. System displays matching products with title, thumbnail, price, and ratings.

### TS-014: Search Products with No Results
As a visitor, I want to see a "No results found" message when my search doesn't match any products, so that I know to try a different search.

**Priority**: Medium
**Related Requirements**: REQ-003, REQ-004

**Details**: Visitor searches for keyword that doesn't match any products. System displays "No results found" with suggestions to try different keywords.

### TS-015: Browse Products by Category
As a visitor, I want to browse products by selecting a category, so that I can see all items in that category.

**Priority**: Critical
**Related Requirements**: REQ-003, REQ-004, REQ-018

**Details**: Visitor clicks category from navigation menu. System displays all active products in that category.

### TS-016: Browse Products by Sub-Category
As a visitor, I want to browse products by sub-category, so that I can narrow down my search.

**Priority**: High
**Related Requirements**: REQ-003, REQ-004, REQ-018

**Details**: Visitor clicks sub-category from category dropdown. System displays all products in that sub-category.

### TS-017: Filter Product Listing
As a visitor, I want to filter product listings by attributes (size, color, price range), so that I can find products matching my preferences.

**Priority**: High
**Related Requirements**: REQ-003, REQ-004

**Details**: Visitor applies filters on product listing page. System dynamically updates results to show only matching products.

### TS-018: Sort Product Listing
As a visitor, I want to sort products by different criteria (price, rating, newest), so that I can view products in my preferred order.

**Priority**: High
**Related Requirements**: REQ-003, REQ-004

**Details**: Visitor selects sort option from dropdown. System reorders products according to selected criteria.

### TS-019: View Product Details as Visitor
As a visitor, I want to view detailed product information without logging in, so that I can make an informed decision before purchasing.

**Priority**: Critical
**Related Requirements**: REQ-005

**Details**: Visitor clicks product from listing. System displays product detail page with title, images, description, price, available sizes/colors, and ratings/reviews.

### TS-020: Check Shipping Availability by PIN Code
As a visitor, I want to check if product can be shipped to my PIN code, so that I know if I can order it.

**Priority**: High
**Related Requirements**: REQ-005

**Details**: Visitor enters PIN code on product detail page. System checks shipping availability and displays "Available" or "Not available for delivery" message.

### TS-021: View Product Variations (Size and Color)
As a visitor, I want to see available size and color variations for a product, so that I can choose my preferred option.

**Priority**: Critical
**Related Requirements**: REQ-005, REQ-019

**Details**: Product detail page displays available sizes and colors. Visitor selects variation, and price/availability updates accordingly.

### TS-022: View Product Ratings and Reviews
As a visitor, I want to view ratings and reviews for a product, so that I can learn from other customers' experiences.

**Priority**: High
**Related Requirements**: REQ-005, REQ-011

**Details**: Product detail page displays aggregate rating and individual customer reviews. Reviews show rating, text, reviewer name, and date.

---

## Shopping Cart and Wishlist Scenarios

### TS-023: Add Product to Cart as Logged-in Buyer
As a logged-in buyer, I want to add a product to my cart, so that I can purchase it later.

**Priority**: Critical
**Related Requirements**: REQ-007

**Details**: Buyer on product detail page selects size/color and clicks "Add to Cart". System adds product to buyer's cart and displays success message.

### TS-024: Add Product to Cart Without Login
As a visitor, I want to be prompted to login when I try to add a product to cart, so that I can create an account to proceed.

**Priority**: High
**Related Requirements**: REQ-007

**Details**: Visitor clicks "Add to Cart". System displays login/registration prompt.

### TS-025: Add Multiple Quantities of Same Product
As a buyer, I want to add multiple quantities of the same product to my cart, so that I can purchase in bulk.

**Priority**: High
**Related Requirements**: REQ-007

**Details**: Buyer on product page sets quantity to multiple units before adding to cart. System adds specified quantity.

### TS-026: View Shopping Cart
As a buyer, I want to view my shopping cart, so that I can see all items I've added.

**Priority**: Critical
**Related Requirements**: REQ-007

**Details**: Buyer clicks cart icon. System displays cart page with all items, showing image, name, variation, unit price, quantity, and subtotal.

### TS-027: Update Item Quantity in Cart
As a buyer, I want to update the quantity of items in my cart, so that I can change my order.

**Priority**: High
**Related Requirements**: REQ-007

**Details**: Buyer on cart page changes quantity field and updates. System recalculates subtotal and total.

### TS-028: Remove Item from Cart
As a buyer, I want to remove an item from my cart, so that I don't purchase it.

**Priority**: High
**Related Requirements**: REQ-007

**Details**: Buyer clicks "Remove" button next to cart item. System removes item and updates cart total.

### TS-029: View Empty Cart
As a buyer, I want to see a message when my cart is empty, so that I know there are no items to checkout.

**Priority**: Medium
**Related Requirements**: REQ-007

**Details**: Buyer with empty cart views cart page. System displays "Your cart is empty" message with link to continue shopping.

### TS-030: Add Product to Wishlist as Logged-in Buyer
As a logged-in buyer, I want to add a product to my wishlist, so that I can save it for later consideration.

**Priority**: High
**Related Requirements**: REQ-006

**Details**: Buyer on product detail page clicks "Add to Wishlist". System adds product to buyer's wishlist and displays success message.

### TS-031: Add Product to Wishlist Without Login
As a visitor, I want to be prompted to login when I try to add a product to wishlist, so that the system can save my preferences.

**Priority**: Medium
**Related Requirements**: REQ-006

**Details**: Visitor clicks "Add to Wishlist". System displays login/registration prompt.

### TS-032: View Wishlist
As a buyer, I want to view my wishlist, so that I can see all products I've saved.

**Priority**: High
**Related Requirements**: REQ-006

**Details**: Buyer navigates to My Account > Wishlist. System displays all wishlist items with product images, names, and prices.

### TS-033: Remove Product from Wishlist
As a buyer, I want to remove a product from my wishlist, so that I can keep my wishlist current.

**Priority**: Medium
**Related Requirements**: REQ-006

**Details**: Buyer clicks "Remove" button on wishlist item. System removes product from wishlist.

### TS-034: Move Product from Wishlist to Cart
As a buyer, I want to move a product from wishlist to cart, so that I can proceed to purchase it.

**Priority**: Medium
**Related Requirements**: REQ-006, REQ-007

**Details**: Buyer on wishlist page clicks "Add to Cart" for wishlist item. System adds product to cart.

---

## Checkout and Payment Scenarios

### TS-035: Checkout as Logged-in Buyer with Valid Data
As a buyer, I want to checkout with my cart items, so that I can complete my purchase.

**Priority**: Critical
**Related Requirements**: REQ-008

**Details**: Buyer clicks "Proceed to Checkout" from cart. Checkout page displays order summary. Buyer enters billing and shipping addresses, selects payment method (credit card or net banking), and submits order. System processes payment via Stripe and creates order.

### TS-036: Checkout Without Login
As a visitor, I want to be prompted to login when I try to checkout, so that I can complete the purchase securely.

**Priority**: Critical
**Related Requirements**: REQ-008

**Details**: Visitor clicks "Checkout" button. System redirects to login page with message indicating login required for checkout.

### TS-037: Checkout with Same Billing and Shipping Address
As a buyer, I want to use the same address for billing and shipping, so that I can save time during checkout.

**Priority**: High
**Related Requirements**: REQ-008

**Details**: Buyer on checkout page checks "Same as billing address" checkbox. System auto-populates shipping address fields.

### TS-038: Checkout with Different Billing and Shipping Addresses
As a buyer, I want to specify different billing and shipping addresses, so that I can send items to a different location.

**Priority**: High
**Related Requirements**: REQ-008

**Details**: Buyer enters different addresses for billing and shipping. System saves both addresses and uses shipping address for delivery.

### TS-039: Select Credit/Debit Card Payment Method
As a buyer, I want to pay with credit or debit card, so that I can complete my purchase online.

**Priority**: Critical
**Related Requirements**: REQ-008, REQ-020

**Details**: Buyer selects "Credit/Debit Card" payment option. System redirects to Stripe payment gateway. Buyer enters card details and completes payment.

### TS-040: Select Net Banking Payment Method
As a buyer, I want to pay via net banking, so that I can use my bank account for payment.

**Priority**: Critical
**Related Requirements**: REQ-008, REQ-020

**Details**: Buyer selects "Net Banking" payment option. System redirects to Stripe payment gateway with net banking option. Buyer completes bank authentication and payment.

### TS-041: Successful Payment and Order Confirmation
As a buyer, I want to receive order confirmation after successful payment, so that I know my order was placed.

**Priority**: Critical
**Related Requirements**: REQ-008

**Details**: Buyer completes payment on Stripe. Stripe returns success status. System creates order with status "Open", sends confirmation email to buyer, and displays order confirmation page with order number.

### TS-042: Failed Payment Handling
As a buyer, I want to be notified if my payment fails, so that I can retry with different payment method.

**Priority**: High
**Related Requirements**: REQ-008

**Details**: Buyer completes payment but Stripe returns failure status. System displays error message and allows buyer to retry payment.

### TS-043: View Order Summary Before Payment
As a buyer, I want to review my order summary before making payment, so that I can verify items, prices, and total cost.

**Priority**: Critical
**Related Requirements**: REQ-008

**Details**: Checkout page displays order summary with: item total, subtotal, shipping cost, tax, and order total. Buyer reviews before proceeding to payment.

### TS-044: Email Notification for Order Status Updates
As a buyer, I want to receive email notifications when my order status changes, so that I can track my order progress.

**Priority**: High
**Related Requirements**: REQ-008, REQ-017

**Details**: System sends automated emails when order status changes (Confirmed, In Process, Shipped, Delivered). Emails include order details and tracking information.

---

## Social Sharing Scenarios

### TS-045: Share Product on Social Media as Visitor
As a visitor, I want to share a product on social media, so that I can show it to my friends.

**Priority**: Low
**Related Requirements**: REQ-009

**Details**: Visitor on product detail page clicks social share button (Facebook, Twitter, Pinterest). System opens share dialog for selected platform.

### TS-046: Share Product on Social Media as Buyer
As a buyer, I want to share a product on social media, so that I can recommend it to my network.

**Priority**: Low
**Related Requirements**: REQ-009

**Details**: Buyer on product detail page clicks social share button. System opens share dialog with product details pre-populated.

---

## Ratings and Reviews Scenarios

### TS-047: Post Rating and Review for Purchased Product
As a buyer, I want to post a rating and review for a product I purchased, so that I can share my experience with other customers.

**Priority**: High
**Related Requirements**: REQ-011

**Details**: Buyer navigates to My Account > Ratings and Reviews. System displays list of purchased products eligible for review. Buyer selects product, enters rating (1-5 stars) and review text, and submits. System saves review with status "Pending" for admin approval.

### TS-048: Attempt to Review Product Without Purchase
As a buyer, I want to be prevented from reviewing a product I haven't purchased, so that reviews remain trustworthy.

**Priority**: High
**Related Requirements**: REQ-011

**Details**: Buyer attempts to access review form for product they haven't ordered. System displays message "You can only review products you have purchased."

### TS-049: Attempt to Review Without Login
As a visitor, I want to be prompted to login when I try to post a review, so that I can register and share my feedback.

**Priority**: Medium
**Related Requirements**: REQ-011

**Details**: Visitor clicks "Write a Review" button. System displays login/registration prompt.

---

## Buyer Account Management Scenarios

### TS-050: View My Account Dashboard
As a buyer, I want to view my account dashboard, so that I can access all my account features.

**Priority**: Critical
**Related Requirements**: REQ-010

**Details**: Buyer navigates to My Account. System displays dashboard with links to: My Orders, My Wishlist, Shopping Cart, Ratings and Reviews, Profile Settings, and Logout.

### TS-051: Update Profile Information
As a buyer, I want to update my profile details (email, phone number), so that my account information stays current.

**Priority**: High
**Related Requirements**: REQ-010

**Details**: Buyer navigates to My Account > Profile. Buyer edits email or phone number and saves. System validates and updates profile information.

### TS-052: Change Password
As a buyer, I want to change my password, so that I can maintain account security.

**Priority**: High
**Related Requirements**: REQ-010

**Details**: Buyer navigates to My Account > Change Password. Buyer enters current password, new password, and confirms new password. System validates current password and updates to new password.

### TS-053: Manage Address Book
As a buyer, I want to add, edit, and delete addresses in my address book, so that I can use them for checkout.

**Priority**: High
**Related Requirements**: REQ-010

**Details**: Buyer navigates to My Account > Addresses. Buyer can add new address, edit existing address, delete address, or set default address. System saves changes.

### TS-054: View Order History
As a buyer, I want to view my past orders, so that I can see my purchase history.

**Priority**: Critical
**Related Requirements**: REQ-012

**Details**: Buyer navigates to My Account > My Orders. System displays list of all orders with: order ID, date, total amount, and status.

### TS-055: View Order Details
As a buyer, I want to view detailed information about a specific order, so that I can review what I purchased.

**Priority**: High
**Related Requirements**: REQ-012

**Details**: Buyer clicks order from order history. System displays full order details: items ordered (name, quantity, price), shipping address, payment status, order total, and tracking information (if shipped).

### TS-056: Reorder Items from Order History
As a buyer, I want to reorder items from a previous order, so that I can quickly repurchase favorite products.

**Priority**: Medium
**Related Requirements**: REQ-012

**Details**: Buyer on order details page clicks "Reorder" button. System adds all items from that order to current shopping cart.

### TS-057: Track Current Order
As a buyer, I want to track my current order, so that I know when it will arrive.

**Priority**: High
**Related Requirements**: REQ-012, REQ-017

**Details**: Buyer navigates to My Orders and clicks order with "Shipped" status. System displays tracking information: shipping carrier, tracking ID, current status, and estimated delivery date.

### TS-058: Logout from Account
As a buyer, I want to logout from my account, so that I can secure my session.

**Priority**: Medium
**Related Requirements**: REQ-010

**Details**: Buyer clicks "Logout" from My Account menu. System ends session and redirects to home page.

---

## Contact Support Scenarios

### TS-059: Submit Contact Support Request as Buyer
As a buyer, I want to contact support with a question or complaint, so that I can get assistance.

**Priority**: High
**Related Requirements**: REQ-013

**Details**: Buyer navigates to Contact Us page, fills form (name, email, contact number, message), and submits. System sends email to admin and displays confirmation message to buyer.

### TS-060: Submit Contact Support Request as Visitor
As a visitor, I want to contact support, so that I can ask questions before purchasing.

**Priority**: Medium
**Related Requirements**: REQ-013

**Details**: Visitor navigates to Contact Us page, fills form, and submits. System sends email to admin with inquiry details.

---

## Admin Authentication and Dashboard Scenarios

### TS-061: Admin Login with Valid Credentials
As an admin, I want to login to the admin panel, so that I can manage the ecommerce platform.

**Priority**: Critical
**Related Requirements**: REQ-014

**Details**: Admin enters username and password on admin login page. System authenticates and redirects to admin dashboard.

### TS-062: Admin Login with Invalid Credentials
As an admin, I want to see an error when I enter incorrect credentials, so that I know my login attempt failed.

**Priority**: High
**Related Requirements**: REQ-014

**Details**: Admin enters incorrect username or password. System displays "Invalid credentials" error.

### TS-063: Admin Password Reset
As an admin, I want to reset my password if I forget it, so that I can regain access to the admin panel.

**Priority**: High
**Related Requirements**: REQ-014

**Details**: Admin clicks "Forgot Password" on login page, enters username/email, receives reset link, and sets new password.

### TS-064: View Admin Dashboard Metrics
As an admin, I want to view key business metrics on the dashboard, so that I can monitor platform performance.

**Priority**: Critical
**Related Requirements**: REQ-015

**Details**: Admin logs in and lands on dashboard. System displays: total active buyers, total inactive buyers, total products uploaded, total revenue (today), and total revenue (this month).

---

## Admin Buyer Management Scenarios

### TS-065: View All Buyers
As an admin, I want to view a list of all registered buyers, so that I can manage customer accounts.

**Priority**: Critical
**Related Requirements**: REQ-016

**Details**: Admin navigates to Buyers Management. System displays list of all buyers with: name, email, registration date, and account status.

### TS-066: View Buyer Details
As an admin, I want to view detailed information about a specific buyer, so that I can understand their account activity.

**Priority**: High
**Related Requirements**: REQ-016

**Details**: Admin clicks buyer from list. System displays buyer profile details, addresses, order history, wishlist items, and cart items.

### TS-067: Edit Buyer Information
As an admin, I want to edit a buyer's profile information, so that I can correct errors or update data.

**Priority**: Medium
**Related Requirements**: REQ-016

**Details**: Admin on buyer details page edits profile fields (name, email, phone) and saves. System updates buyer information.

### TS-068: Deactivate Buyer Account
As an admin, I want to deactivate a buyer account, so that I can prevent access for problematic users.

**Priority**: High
**Related Requirements**: REQ-016

**Details**: Admin clicks "Deactivate" button on buyer account. System sets account status to "Inactive" and prevents buyer from logging in.

### TS-069: Reactivate Buyer Account
As an admin, I want to reactivate a previously deactivated buyer account, so that the user can access the platform again.

**Priority**: Medium
**Related Requirements**: REQ-016

**Details**: Admin clicks "Activate" button on inactive buyer account. System sets account status to "Active" and buyer can login again.

---

## Admin Order Management Scenarios

### TS-070: View All Orders
As an admin, I want to view a list of all orders, so that I can manage order fulfillment.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin navigates to Orders Management. System displays list of all orders with: order ID, buyer name, order date, order status, and order total.

### TS-071: Filter Orders by Status
As an admin, I want to filter orders by status (Open, Confirmed, In Process, Shipped, Delivered), so that I can focus on specific order stages.

**Priority**: High
**Related Requirements**: REQ-017

**Details**: Admin selects status filter on orders page. System displays only orders with selected status.

### TS-072: View Order Details
As an admin, I want to view detailed information about a specific order, so that I can process it.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin clicks order from list. System displays full order details: buyer information, items ordered, quantities, prices, shipping address, payment status, and current order status.

### TS-073: Update Order Status from Open to Confirmed
As an admin, I want to update order status from Open to Confirmed, so that I can indicate the order has been verified.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin on order details page changes status from "Open" to "Confirmed" and saves. System updates order status and sends email notification to buyer.

### TS-074: Update Order Status from Confirmed to In Process
As an admin, I want to update order status to In Process, so that I can indicate shipment preparation has started.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin changes status from "Confirmed" to "In Process" and saves. System updates status and notifies buyer.

### TS-075: Update Order Status to Shipped with Tracking Information
As an admin, I want to update order status to Shipped and add tracking details, so that the buyer can track their shipment.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin changes status from "In Process" to "Shipped", enters shipping carrier, tracking ID, and estimated delivery date. System updates order and sends tracking email to buyer.

### TS-076: Update Order Status to Delivered
As an admin, I want to mark an order as Delivered, so that I can close the order lifecycle.

**Priority**: Critical
**Related Requirements**: REQ-017

**Details**: Admin changes status from "Shipped" to "Delivered" and saves. System updates order and sends delivery confirmation email to buyer.

### TS-077: Edit Order Details
As an admin, I want to edit order details (shipping address, items), so that I can accommodate buyer requests for changes.

**Priority**: Medium
**Related Requirements**: REQ-017

**Details**: Admin on order details page edits modifiable fields (shipping address, quantities) before order is shipped. System saves changes.

---

## Admin Product Management Scenarios

### TS-078: Create New Product
As an admin, I want to add a new product to the catalog, so that buyers can purchase it.

**Priority**: Critical
**Related Requirements**: REQ-019

**Details**: Admin navigates to Products Management, clicks "Add New Product", fills form (product name, description, SKU, price, category, sub-category, keywords), uploads images, adds variations (sizes, colors), and saves. System creates product with status "Active".

### TS-079: Edit Product Information
As an admin, I want to edit an existing product's details, so that I can keep product information accurate.

**Priority**: High
**Related Requirements**: REQ-019

**Details**: Admin searches for product, clicks to edit, updates fields (name, description, price, images, variations), and saves. System updates product information.

### TS-080: Deactivate Product
As an admin, I want to deactivate a product, so that it's no longer visible to buyers on the website.

**Priority**: High
**Related Requirements**: REQ-019

**Details**: Admin clicks "Deactivate" button on product. System sets product status to "Inactive" and removes it from frontend listings.

### TS-081: Reactivate Product
As an admin, I want to reactivate a previously deactivated product, so that buyers can see and purchase it again.

**Priority**: Medium
**Related Requirements**: REQ-019

**Details**: Admin clicks "Activate" button on inactive product. System sets product status to "Active" and displays it on frontend.

### TS-082: Delete Product
As an admin, I want to delete a product from the catalog, so that I can remove discontinued items.

**Priority**: Low
**Related Requirements**: REQ-019

**Details**: Admin clicks "Delete" button on product. System prompts for confirmation. If confirmed, system removes product from database (or marks as deleted).

### TS-083: Create Product Category
As an admin, I want to create a new product category, so that I can organize products.

**Priority**: High
**Related Requirements**: REQ-018

**Details**: Admin navigates to Product Categories Management, clicks "Add Category", enters category name and description, and saves. System creates category.

### TS-084: Create Product Sub-Category
As an admin, I want to create a sub-category under an existing category, so that I can further organize products.

**Priority**: High
**Related Requirements**: REQ-018

**Details**: Admin clicks "Add Sub-Category" under parent category, enters name and description, and saves. System creates sub-category linked to parent.

### TS-085: Edit Product Category
As an admin, I want to edit a category's name or description, so that I can keep it accurate.

**Priority**: Medium
**Related Requirements**: REQ-018

**Details**: Admin clicks category to edit, updates name or description, and saves. System updates category.

### TS-086: Deactivate Product Category
As an admin, I want to deactivate a category, so that it's hidden from frontend navigation.

**Priority**: Medium
**Related Requirements**: REQ-018

**Details**: Admin clicks "Deactivate" on category. System sets status to "Inactive" and removes from frontend menu. Products in category remain but aren't browsable by category.

---

## Admin Content and Moderation Scenarios

### TS-087: Approve Product Review
As an admin, I want to approve a pending product review, so that it's displayed on the product page.

**Priority**: Medium
**Related Requirements**: REQ-021

**Details**: Admin navigates to Ratings & Reviews Management, views pending review, reads content, and clicks "Approve". System sets review status to "Approved" and displays on product detail page.

### TS-088: Reject Product Review
As an admin, I want to reject inappropriate product reviews, so that I can maintain quality standards.

**Priority**: Medium
**Related Requirements**: REQ-021

**Details**: Admin views pending review with inappropriate content and clicks "Reject". System sets review status to "Rejected" and does not display on product page.

### TS-089: Edit CMS Page Content
As an admin, I want to edit CMS pages (About Us, Contact Us, Privacy Policy, Terms and Conditions), so that I can keep website content current.

**Priority**: Critical
**Related Requirements**: REQ-024

**Details**: Admin navigates to CMS Management, selects page to edit, updates content using editor, and saves. System updates CMS page content on frontend.

### TS-090: Create Email Template
As an admin, I want to create an email template for promotional campaigns, so that I can send marketing emails to buyers.

**Priority**: Medium
**Related Requirements**: REQ-025

**Details**: Admin navigates to Email Management, clicks "Add Template", enters subject and body content, and saves. System stores email template for future use.

### TS-091: Send Promotional Email to Buyers
As an admin, I want to send promotional emails to all buyers, so that I can announce new products or offers.

**Priority**: Low
**Related Requirements**: REQ-025

**Details**: Admin selects email template, chooses target audience (all buyers or filtered segment), and sends. System sends emails to selected buyers.

---

## Admin Reporting and System Management Scenarios

### TS-092: View Products Uploaded Report
As an admin, I want to view a report of products uploaded by date range, so that I can track catalog growth.

**Priority**: High
**Related Requirements**: REQ-022

**Details**: Admin navigates to Statistics & Reports, selects "Products Uploaded" report type, specifies date range, and generates report. System displays product count by date.

### TS-093: View Revenue Report
As an admin, I want to view revenue reports (today, current week, month, year), so that I can monitor sales performance.

**Priority**: High
**Related Requirements**: REQ-022

**Details**: Admin selects "Revenue/Sales" report type, chooses time period (today, current week, date range, month, year), and generates report. System displays total revenue with breakdown.

### TS-094: Export Report to PDF
As an admin, I want to export reports to PDF format, so that I can share them with stakeholders.

**Priority**: Medium
**Related Requirements**: REQ-022

**Details**: Admin generates report and clicks "Export to PDF" button. System creates PDF file and initiates download.

### TS-095: Export Report to Excel
As an admin, I want to export reports to Excel format, so that I can perform additional analysis.

**Priority**: Medium
**Related Requirements**: REQ-022

**Details**: Admin generates report and clicks "Export to Excel" button. System creates Excel file and initiates download.

### TS-096: Create Sub-Admin User
As an admin, I want to create sub-admin users with role-based access, so that I can delegate responsibilities.

**Priority**: High
**Related Requirements**: REQ-023, REQ-027

**Details**: Admin navigates to System Users Management, clicks "Add User", enters username and password, assigns role, and saves. System creates sub-admin user with specified permissions.

### TS-097: Edit Sub-Admin User
As an admin, I want to edit sub-admin user details or change their role, so that I can update access as needed.

**Priority**: Medium
**Related Requirements**: REQ-023, REQ-027

**Details**: Admin clicks sub-admin user to edit, updates username, password, or assigned role, and saves. System updates user information.

### TS-098: Deactivate Sub-Admin User
As an admin, I want to deactivate a sub-admin user, so that I can revoke their access without deleting the account.

**Priority**: Medium
**Related Requirements**: REQ-023

**Details**: Admin clicks "Deactivate" on sub-admin user. System sets user status to "Inactive" and prevents login.

### TS-099: Delete Sub-Admin User
As an admin, I want to delete a sub-admin user permanently, so that I can remove unnecessary accounts.

**Priority**: Low
**Related Requirements**: REQ-023

**Details**: Admin clicks "Delete" on sub-admin user and confirms. System removes user from database.

### TS-100: View Customer Complaints and Feedback
As an admin, I want to view customer complaints and feedback submitted via Contact Us form, so that I can respond to customer inquiries.

**Priority**: High
**Related Requirements**: REQ-026

**Details**: Admin navigates to Complaints/Feedbacks section. System displays list of all contact form submissions with: customer name, email, contact number, message, and submission date. Admin receives email notification for each new submission.

---

## Admin Payment Management Scenarios

### TS-101: View Payment Status for Orders
As an admin, I want to view payment status for each order (Pending, Completed, Failed), so that I can track financial transactions.

**Priority**: Critical
**Related Requirements**: REQ-020

**Details**: Admin navigates to Payment Management or Orders. System displays payment status for each order with transaction details from Stripe.

### TS-102: Update Bank Account Information
As an admin, I want to update the bank account details for receiving payments, so that funds are deposited correctly.

**Priority**: Medium
**Related Requirements**: REQ-020

**Details**: Admin navigates to Payment Management, edits bank account information, and saves. System updates payment receiving account details for Stripe integration.

---

## Non-Functional Requirements Scenarios

### TS-103: Concurrent User Load Test
As a system, I want to support 100 concurrent users, so that multiple buyers can use the platform simultaneously.

**Priority**: Critical
**Related Requirements**: REQ-028

**Details**: Performance test with 100 simultaneous users browsing, searching, and purchasing. System maintains responsiveness and stability.

### TS-104: Page Load Performance Test
As a system, I want web pages to load within 30 seconds, so that users have acceptable experience.

**Priority**: Critical
**Related Requirements**: REQ-029

**Details**: Test page load times for all major pages (home, product listing, product details, cart, checkout) with good internet speed. All pages should load within 30 seconds (note: industry standard is 2-3 seconds, this requirement may need revision).

### TS-105: Error Handling for Page Not Found
As a system, I want to display a proper error page when a requested page doesn't exist, so that users aren't confused by broken pages.

**Priority**: High
**Related Requirements**: REQ-030

**Details**: User navigates to non-existent URL. System displays custom 404 error page with navigation options instead of broken page.

### TS-106: SSL Security for Payment Transactions
As a system, I want to use SSL encryption for all payment transactions, so that customer payment data is secure.

**Priority**: Critical
**Related Requirements**: REQ-031

**Details**: All payment pages and Stripe integration use HTTPS with valid SSL certificate. Payment data transmitted securely.

---

## Summary

**Total Test Scenarios**: 106
**Coverage Breakdown**:
- Buyer Registration and Authentication: 12 scenarios (TS-001 to TS-012)
- Product Discovery and Browsing: 10 scenarios (TS-013 to TS-022)
- Shopping Cart and Wishlist: 12 scenarios (TS-023 to TS-034)
- Checkout and Payment: 10 scenarios (TS-035 to TS-044)
- Social Sharing: 2 scenarios (TS-045 to TS-046)
- Ratings and Reviews: 3 scenarios (TS-047 to TS-049)
- Buyer Account Management: 9 scenarios (TS-050 to TS-058)
- Contact Support: 2 scenarios (TS-059 to TS-060)
- Admin Authentication and Dashboard: 4 scenarios (TS-061 to TS-064)
- Admin Buyer Management: 5 scenarios (TS-065 to TS-069)
- Admin Order Management: 8 scenarios (TS-070 to TS-077)
- Admin Product Management: 9 scenarios (TS-078 to TS-086)
- Admin Content and Moderation: 5 scenarios (TS-087 to TS-091)
- Admin Reporting and System Management: 9 scenarios (TS-092 to TS-100)
- Admin Payment Management: 2 scenarios (TS-101 to TS-102)
- Non-Functional Requirements: 4 scenarios (TS-103 to TS-106)

**Requirements Coverage**: All 31 requirements covered with at least one scenario

**Scenario Types**:
- Positive/Happy Path: ~65 scenarios
- Negative/Error Handling: ~30 scenarios
- Edge Cases: ~11 scenarios

**Next Step**: Generate exhaustive variants for all 106 scenarios in Step 5
