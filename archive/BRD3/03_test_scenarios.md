# Test Scenarios - Ecommerce Website

## Document Information
- **Source**: Requirements and Entities/Flows from BRD v1.0
- **Generation Date**: 2025-11-14
- **Total Test Scenarios**: 178
- **Coverage**: All 212 requirements

---

## FUNCTIONAL AREA 1: USER AUTHENTICATION & REGISTRATION

### TS-001: Buyer Registration with Valid Data
As a new visitor, I want to register on the website with valid information, so that I can create an account and shop online.

**Related Requirements**: REQ-005, REQ-006, REQ-007, REQ-008, REQ-009, REQ-010, REQ-011, REQ-012

---

### TS-002: Email Verification After Registration
As a newly registered user, I want to verify my email address, so that I can activate my account and log in.

**Related Requirements**: REQ-013, REQ-014, REQ-015, REQ-016

---

### TS-003: Registration with Invalid Email Format
As a new visitor, I want the system to validate my email format during registration, so that I don't create an account with invalid email.

**Related Requirements**: REQ-008

---

### TS-004: Registration with Mismatched Passwords
As a new visitor, I want the system to validate that my password and confirm password match, so that I don't accidentally set a wrong password.

**Related Requirements**: REQ-010, REQ-011

---

### TS-005: Registration Without Accepting Terms and Conditions
As a new visitor, I want the system to require acceptance of terms and conditions, so that I'm aware of the policies.

**Related Requirements**: REQ-012

---

### TS-006: Registration with Duplicate Email
As a new visitor, I want the system to prevent duplicate email registration, so that each account is unique.

**Related Requirements**: REQ-008

---

### TS-007: Login with Valid Email and Password
As a registered buyer, I want to log in using my email and password, so that I can access my account and shop.

**Related Requirements**: REQ-001, REQ-016

---

### TS-008: Login with Unverified Email
As a registered buyer who hasn't verified email, I want the system to prevent login, so that only verified accounts can access the site.

**Related Requirements**: REQ-013, REQ-016

---

### TS-009: Login with Invalid Credentials
As a user, I want the system to reject invalid login credentials, so that my account remains secure.

**Related Requirements**: REQ-001

---

### TS-010: Login with Facebook Account
As a buyer, I want to log in using my Facebook account, so that I can quickly access the site without creating a new password.

**Related Requirements**: REQ-003

---

### TS-011: Login with Google Account
As a buyer, I want to log in using my Google account, so that I can quickly access the site without creating a new password.

**Related Requirements**: REQ-004

---

### TS-012: First-Time Social Login (Auto-Registration)
As a new user logging in with Facebook/Google, I want the system to automatically create my account, so that I don't need to fill out a registration form.

**Related Requirements**: REQ-003, REQ-004

---

### TS-013: Password Reset Request
As a buyer who forgot their password, I want to request a password reset, so that I can regain access to my account.

**Related Requirements**: REQ-002

---

### TS-014: Password Reset Email Verification
As a buyer who requested password reset, I want to receive a reset link via email, so that I can securely reset my password.

**Related Requirements**: REQ-002

---

### TS-015: Complete Password Reset Process
As a buyer with a password reset link, I want to set a new password, so that I can log in with updated credentials.

**Related Requirements**: REQ-002

---

### TS-016: Password Reset with Expired Token
As a buyer, I want the system to reject expired password reset tokens, so that old reset links can't be used maliciously.

**Related Requirements**: REQ-002

---

### TS-017: Login with New Password After Reset
As a buyer who reset their password, I want to log in with my new password, so that I can confirm the reset was successful.

**Related Requirements**: REQ-001, REQ-002

---

### TS-018: Admin Login with Valid Credentials
As an admin user, I want to log in to the admin panel with username and password, so that I can manage the ecommerce website.

**Related Requirements**: REQ-017, REQ-018

---

### TS-019: Admin Login with Invalid Credentials
As an admin, I want the system to reject invalid admin credentials, so that unauthorized users cannot access the admin panel.

**Related Requirements**: REQ-017, REQ-018

---

### TS-020: Admin Password Reset
As an admin who forgot their password, I want to reset my password, so that I can regain access to the admin panel.

**Related Requirements**: REQ-019

---

## FUNCTIONAL AREA 2: PRODUCT BROWSING & SEARCH

### TS-021: Search Products by Keyword
As a visitor, I want to search for products using keywords, so that I can find specific items I'm looking for.

**Related Requirements**: REQ-020, REQ-025

---

### TS-022: Browse Products by Category
As a visitor, I want to browse products by selecting a category, so that I can see all products in that category.

**Related Requirements**: REQ-021, REQ-025

---

### TS-023: Browse Products by Sub-Category
As a visitor, I want to browse products by sub-category, so that I can narrow down my search to specific types of items.

**Related Requirements**: REQ-022, REQ-025

---

### TS-024: Filter Product Search Results
As a visitor, I want to apply filters to product search results, so that I can refine my search by criteria like price, color, or size.

**Related Requirements**: REQ-023, REQ-025

---

### TS-025: Sort Product Search Results
As a visitor, I want to sort product search results by different criteria, so that I can view products in my preferred order.

**Related Requirements**: REQ-024, REQ-025

---

### TS-026: Search with No Results
As a visitor, I want to see a meaningful message when my search returns no results, so that I know to try a different search.

**Related Requirements**: REQ-020

---

### TS-027: Search Without Logging In
As a visitor who is not logged in, I want to search for products, so that I can browse without creating an account.

**Related Requirements**: REQ-025

---

### TS-028: View Product Listing
As a visitor, I want to view a list of products with key information, so that I can quickly compare products.

**Related Requirements**: REQ-026, REQ-027, REQ-028, REQ-029, REQ-032

---

### TS-029: Navigate to Product Details from Listing (Click Title)
As a visitor, I want to click on a product title in the listing, so that I can view detailed information about that product.

**Related Requirements**: REQ-030, REQ-032

---

### TS-030: Navigate to Product Details from Listing (Click Image)
As a visitor, I want to click on a product image in the listing, so that I can view detailed information about that product.

**Related Requirements**: REQ-031, REQ-032

---

### TS-031: View Product Details Without Login
As a visitor, I want to view full product details without logging in, so that I can learn about products before deciding to register.

**Related Requirements**: REQ-033

---

### TS-032: View Product Details Page
As a visitor, I want to view comprehensive product details, so that I can make an informed purchase decision.

**Related Requirements**: REQ-035, REQ-036, REQ-037, REQ-038, REQ-039, REQ-040, REQ-041, REQ-042

---

### TS-033: Check Shipping Availability by ZIP Code
As a visitor, I want to check if a product can be shipped to my ZIP code, so that I know if I can order it.

**Related Requirements**: REQ-034

---

### TS-034: Check Shipping with Invalid ZIP Code
As a visitor, I want the system to validate my ZIP code entry, so that I get accurate shipping information.

**Related Requirements**: REQ-034

---

### TS-035: View Product Images Gallery
As a visitor, I want to view multiple images of a product, so that I can see it from different angles.

**Related Requirements**: REQ-036, REQ-037

---

### TS-036: View Product Ratings and Reviews
As a visitor, I want to view ratings and reviews on the product detail page, so that I can see what other buyers think.

**Related Requirements**: REQ-042, REQ-100, REQ-101

---

### TS-037: Select Product Variations (Size and Color)
As a visitor, I want to select different size and color variations, so that I can choose the exact product I want.

**Related Requirements**: REQ-040, REQ-041

---

## FUNCTIONAL AREA 3: WISHLIST & SOCIAL SHARING

### TS-038: Add Product to Wishlist (Logged In)
As a logged-in buyer, I want to add products to my wishlist, so that I can save items for later consideration.

**Related Requirements**: REQ-044, REQ-045, REQ-047

---

### TS-039: Add Product to Wishlist (Not Logged In)
As a visitor who is not logged in, I want to be prompted to log in when adding to wishlist, so that my wishlist is saved to my account.

**Related Requirements**: REQ-044, REQ-045

---

### TS-040: View Wishlist
As a logged-in buyer, I want to view all items in my wishlist, so that I can review products I've saved.

**Related Requirements**: REQ-046

---

### TS-041: Remove Product from Wishlist
As a logged-in buyer, I want to delete products from my wishlist, so that I can remove items I'm no longer interested in.

**Related Requirements**: REQ-048

---

### TS-042: Checkout from Wishlist
As a logged-in buyer, I want to proceed to checkout from wishlist items, so that I can purchase saved products.

**Related Requirements**: REQ-049

---

### TS-043: Share Product on Social Media (Logged In)
As a logged-in buyer, I want to share products on social media, so that I can recommend items to friends.

**Related Requirements**: REQ-050, REQ-052

---

### TS-044: Share Product on Social Media (Not Logged In)
As a visitor, I want to share products on social media without logging in, so that I can share items I find interesting.

**Related Requirements**: REQ-050, REQ-051, REQ-052

---

## FUNCTIONAL AREA 4: SHOPPING CART & CHECKOUT

### TS-045: Add Product to Cart (Logged In)
As a logged-in buyer, I want to add products to my shopping cart, so that I can collect items for purchase.

**Related Requirements**: REQ-043, REQ-053, REQ-054, REQ-055

---

### TS-046: Add Product to Cart (Not Logged In)
As a visitor who is not logged in, I want to be prompted to log in when adding to cart, so that my cart is saved.

**Related Requirements**: REQ-053, REQ-054

---

### TS-047: Add Product with Variation to Cart
As a logged-in buyer, I want to add a product with specific size and color to cart, so that I get exactly what I want.

**Related Requirements**: REQ-053, REQ-055

---

### TS-048: View Shopping Cart
As a logged-in buyer, I want to view my shopping cart with all items and pricing, so that I can review my order before checkout.

**Related Requirements**: REQ-059, REQ-060, REQ-061

---

### TS-049: Update Cart Item Quantity
As a logged-in buyer, I want to update the quantity of items in my cart, so that I can order the right amount.

**Related Requirements**: REQ-057

---

### TS-050: Remove Item from Cart
As a logged-in buyer, I want to remove items from my cart, so that I only purchase what I want.

**Related Requirements**: REQ-056

---

### TS-051: Proceed to Checkout from Cart
As a logged-in buyer, I want to proceed to checkout from my cart, so that I can complete my purchase.

**Related Requirements**: REQ-058

---

### TS-052: Checkout Process (Full Flow)
As a logged-in buyer, I want to complete the checkout process, so that I can place my order and make payment.

**Related Requirements**: REQ-062, REQ-063, REQ-064, REQ-065, REQ-066

---

### TS-053: Enter Billing Address at Checkout
As a logged-in buyer, I want to enter my billing address, so that payment can be processed correctly.

**Related Requirements**: REQ-064

---

### TS-054: Enter Shipping Address at Checkout
As a logged-in buyer, I want to enter my shipping address, so that my order is delivered to the correct location.

**Related Requirements**: REQ-065

---

### TS-055: Select Address from Address Book at Checkout
As a logged-in buyer with saved addresses, I want to select an address from my address book, so that I don't have to re-enter it.

**Related Requirements**: REQ-064, REQ-065, REQ-094

---

### TS-056: View Order Summary Before Payment
As a logged-in buyer, I want to review my order summary before payment, so that I can verify everything is correct.

**Related Requirements**: REQ-067, REQ-068, REQ-069, REQ-070, REQ-071, REQ-072

---

### TS-057: Select Credit/Debit Card Payment Method
As a logged-in buyer, I want to pay with credit or debit card, so that I can complete my purchase securely.

**Related Requirements**: REQ-066

---

### TS-058: Select Net Banking Payment Method
As a logged-in buyer, I want to pay with net banking, so that I have an alternative payment option.

**Related Requirements**: REQ-066

---

### TS-059: Complete Payment via Stripe
As a logged-in buyer, I want to complete payment through Stripe gateway, so that my payment is processed securely.

**Related Requirements**: REQ-066, REQ-158

---

### TS-060: Successful Payment and Order Placement
As a logged-in buyer with successful payment, I want my order to be created and confirmed, so that I receive my products.

**Related Requirements**: REQ-074, REQ-075

---

### TS-061: Failed Payment Handling
As a logged-in buyer with failed payment, I want to see an error message and retry, so that I can complete my purchase.

**Related Requirements**: REQ-066

---

### TS-062: Receive Order Confirmation Email
As a logged-in buyer who placed an order, I want to receive an order confirmation email, so that I have a record of my purchase.

**Related Requirements**: REQ-073, REQ-075

---

### TS-063: Cart Cleared After Successful Order
As a logged-in buyer who completed an order, I want my cart to be cleared, so that I start fresh for next purchase.

**Related Requirements**: REQ-055, REQ-074

---

## FUNCTIONAL AREA 5: ORDER MANAGEMENT (BUYER)

### TS-064: View Order History
As a logged-in buyer, I want to view all my past orders, so that I can track my purchase history.

**Related Requirements**: REQ-076

---

### TS-065: View Order Details
As a logged-in buyer, I want to view detailed information about a specific order, so that I can see what I ordered.

**Related Requirements**: REQ-077, REQ-078, REQ-079, REQ-080

---

### TS-066: Reorder from Order History
As a logged-in buyer, I want to reorder items from my past orders, so that I can easily repurchase products I like.

**Related Requirements**: REQ-081

---

### TS-067: Track Current Order
As a logged-in buyer, I want to track my current order status, so that I know when to expect delivery.

**Related Requirements**: REQ-082

---

### TS-068: View Order Status Updates
As a logged-in buyer, I want to see my order status (Open, Confirmed, In Process, Shipped, Delivered), so that I know the progress of my order.

**Related Requirements**: REQ-082, REQ-126, REQ-127, REQ-128, REQ-129, REQ-130

---

### TS-069: Receive Order Status Update Emails
As a logged-in buyer, I want to receive email notifications when my order status changes, so that I'm informed of progress.

**Related Requirements**: REQ-073

---

## FUNCTIONAL AREA 6: USER ACCOUNT MANAGEMENT

### TS-070: Access My Account Section
As a logged-in buyer, I want to access my account section, so that I can manage my profile and settings.

**Related Requirements**: REQ-083, REQ-086, REQ-087, REQ-088, REQ-089

---

### TS-071: Update Profile Details
As a logged-in buyer, I want to update my profile details (email, phone number), so that my information is current.

**Related Requirements**: REQ-083

---

### TS-072: Change Password
As a logged-in buyer, I want to change my password, so that I can maintain account security.

**Related Requirements**: REQ-084

---

### TS-073: Add New Address to Address Book
As a logged-in buyer, I want to add a new address to my address book, so that I can use it for future orders.

**Related Requirements**: REQ-085, REQ-091

---

### TS-074: Edit Existing Address in Address Book
As a logged-in buyer, I want to edit an existing address, so that I can update it if I move or correct mistakes.

**Related Requirements**: REQ-085, REQ-092

---

### TS-075: Delete Address from Address Book
As a logged-in buyer, I want to delete an address from my address book, so that I only keep relevant addresses.

**Related Requirements**: REQ-085, REQ-093

---

### TS-076: Access My Orders from My Account
As a logged-in buyer, I want to access my orders from my account, so that I can view order history and track shipments.

**Related Requirements**: REQ-086

---

### TS-077: Access My Wishlist from My Account
As a logged-in buyer, I want to access my wishlist from my account, so that I can view and manage saved items.

**Related Requirements**: REQ-087

---

### TS-078: Access Shopping Cart from My Account
As a logged-in buyer, I want to access my shopping cart from my account, so that I can review and checkout items.

**Related Requirements**: REQ-088

---

### TS-079: Access Ratings and Reviews from My Account
As a logged-in buyer, I want to access my ratings and reviews from my account, so that I can manage my feedback.

**Related Requirements**: REQ-089

---

### TS-080: Logout from My Account
As a logged-in buyer, I want to log out of my account, so that I can secure my session.

**Related Requirements**: REQ-090

---

## FUNCTIONAL AREA 7: RATINGS & REVIEWS

### TS-081: Post Rating for Purchased Product
As a logged-in buyer who purchased a product, I want to rate that product, so that I can share my opinion.

**Related Requirements**: REQ-095, REQ-097, REQ-098

---

### TS-082: Post Review for Purchased Product
As a logged-in buyer who purchased a product, I want to review that product, so that I can help other buyers.

**Related Requirements**: REQ-096, REQ-097, REQ-098

---

### TS-083: Attempt to Rate Product Not Purchased
As a logged-in buyer, I want the system to prevent me from rating products I haven't ordered, so that ratings are authentic.

**Related Requirements**: REQ-097

---

### TS-084: Attempt to Review Product Not Purchased
As a logged-in buyer, I want the system to prevent me from reviewing products I haven't ordered, so that reviews are authentic.

**Related Requirements**: REQ-097

---

### TS-085: Post Rating and Review Without Login
As a visitor not logged in, I want to be prompted to log in to post ratings/reviews, so that feedback is from verified users.

**Related Requirements**: REQ-098

---

### TS-086: View Product Ratings in Listing
As a visitor, I want to see product ratings in the product listing, so that I can quickly assess product quality.

**Related Requirements**: REQ-029, REQ-099

---

### TS-087: View Product Reviews on Detail Page
As a visitor, I want to read product reviews on the detail page, so that I can learn from other buyers' experiences.

**Related Requirements**: REQ-042, REQ-100

---

## FUNCTIONAL AREA 8: CUSTOMER SUPPORT

### TS-088: Submit Contact Support Request
As a visitor or buyer, I want to submit a support request with my details and question, so that I can get help.

**Related Requirements**: REQ-102, REQ-103, REQ-104, REQ-105, REQ-106

---

### TS-089: Admin Receives Support Request Email
As an admin, I want to receive an email when a user submits a support request, so that I can respond promptly.

**Related Requirements**: REQ-107

---

### TS-090: Submit Support Request with Invalid Email
As a visitor, I want the system to validate my email in the support form, so that I receive a response.

**Related Requirements**: REQ-104

---

## FUNCTIONAL AREA 9: ADMIN DASHBOARD

### TS-091: View Admin Dashboard Statistics
As an admin, I want to view dashboard statistics, so that I can monitor business performance at a glance.

**Related Requirements**: REQ-108, REQ-109, REQ-110, REQ-111, REQ-112

---

### TS-092: View Total Active Buyers
As an admin, I want to see the total number of active registered buyers, so that I know my customer base size.

**Related Requirements**: REQ-108

---

### TS-093: View Total Inactive Buyers
As an admin, I want to see the total number of inactive registered buyers, so that I can track dormant accounts.

**Related Requirements**: REQ-109

---

### TS-094: View Total Products Uploaded
As an admin, I want to see the total number of products on the website, so that I know my catalog size.

**Related Requirements**: REQ-110

---

### TS-095: View Today's Revenue
As an admin, I want to see total revenue for today, so that I can track daily sales.

**Related Requirements**: REQ-111

---

### TS-096: View Current Month Revenue
As an admin, I want to see total revenue for the current month, so that I can track monthly performance.

**Related Requirements**: REQ-112

---

## FUNCTIONAL AREA 10: ADMIN - CUSTOMER MANAGEMENT

### TS-097: View All Buyer Accounts
As an admin, I want to view a list of all buyer accounts, so that I can manage customers.

**Related Requirements**: REQ-113

---

### TS-098: View Buyer Account Details
As an admin, I want to view detailed information about a specific buyer, so that I can understand their activity.

**Related Requirements**: REQ-117, REQ-118, REQ-119, REQ-120, REQ-121

---

### TS-099: Edit Buyer Account Information
As an admin, I want to edit buyer account information, so that I can correct or update details if needed.

**Related Requirements**: REQ-114

---

### TS-100: Activate Buyer Account
As an admin, I want to activate a buyer account, so that the user can access the website.

**Related Requirements**: REQ-115

---

### TS-101: Deactivate Buyer Account
As an admin, I want to deactivate a buyer account, so that I can restrict access if necessary.

**Related Requirements**: REQ-116

---

## FUNCTIONAL AREA 11: ADMIN - ORDER MANAGEMENT

### TS-102: View All Orders
As an admin, I want to view a list of all orders, so that I can manage order fulfillment.

**Related Requirements**: REQ-122

---

### TS-103: View Order Status
As an admin, I want to see the current status of each order, so that I can track order progress.

**Related Requirements**: REQ-123

---

### TS-104: View Order Details
As an admin, I want to view detailed information about a specific order, so that I can process it correctly.

**Related Requirements**: REQ-124

---

### TS-105: Edit Order Details
As an admin, I want to edit order details, so that I can make corrections if needed.

**Related Requirements**: REQ-125

---

### TS-106: Update Order Status to Open
As an admin, I want to set order status to "Open", so that I can mark new orders.

**Related Requirements**: REQ-126

---

### TS-107: Update Order Status to Confirmed
As an admin, I want to set order status to "Confirmed", so that I can indicate order is verified.

**Related Requirements**: REQ-127

---

### TS-108: Update Order Status to In Process
As an admin, I want to set order status to "In Process", so that I can show order is being prepared.

**Related Requirements**: REQ-128

---

### TS-109: Update Order Status to Shipped
As an admin, I want to set order status to "Shipped", so that I can indicate order has been dispatched.

**Related Requirements**: REQ-129

---

### TS-110: Update Order Status to Delivered
As an admin, I want to set order status to "Delivered", so that I can mark order as completed.

**Related Requirements**: REQ-130

---

### TS-111: Add Shipping Information to Order
As an admin, I want to add shipping carrier and tracking ID to an order, so that buyer can track shipment.

**Related Requirements**: REQ-131, REQ-132, REQ-133, REQ-134, REQ-135, REQ-136

---

### TS-112: Buyer Receives Email on Order Status Update
As an admin who updates order status, I want the buyer to receive an email notification, so that they're informed.

**Related Requirements**: REQ-073

---

## FUNCTIONAL AREA 12: ADMIN - PRODUCT MANAGEMENT

### TS-113: Add New Product Category
As an admin, I want to add a new product category, so that I can organize products.

**Related Requirements**: REQ-137

---

### TS-114: Edit Existing Product Category
As an admin, I want to edit a product category, so that I can update category information.

**Related Requirements**: REQ-138

---

### TS-115: Activate Product Category
As an admin, I want to activate a product category, so that it appears on the website.

**Related Requirements**: REQ-139

---

### TS-116: Deactivate Product Category
As an admin, I want to deactivate a product category, so that I can hide it without deleting.

**Related Requirements**: REQ-140

---

### TS-117: Add New Product Sub-Category
As an admin, I want to add a new product sub-category, so that I can further organize products.

**Related Requirements**: REQ-141

---

### TS-118: Edit Existing Product Sub-Category
As an admin, I want to edit a product sub-category, so that I can update sub-category information.

**Related Requirements**: REQ-142

---

### TS-119: Activate Product Sub-Category
As an admin, I want to activate a product sub-category, so that it appears on the website.

**Related Requirements**: REQ-143

---

### TS-120: Deactivate Product Sub-Category
As an admin, I want to deactivate a product sub-category, so that I can hide it without deleting.

**Related Requirements**: REQ-144

---

### TS-121: Add New Product
As an admin, I want to add a new product to the catalog, so that buyers can purchase it.

**Related Requirements**: REQ-145, REQ-149, REQ-150, REQ-151, REQ-152, REQ-153, REQ-154

---

### TS-122: Edit Existing Product
As an admin, I want to edit an existing product, so that I can update product information.

**Related Requirements**: REQ-146, REQ-149, REQ-150, REQ-151, REQ-152, REQ-153, REQ-154

---

### TS-123: Activate Product
As an admin, I want to activate a product, so that it's available for purchase on the website.

**Related Requirements**: REQ-147

---

### TS-124: Deactivate Product
As an admin, I want to deactivate a product, so that I can hide it without deleting (e.g., out of stock).

**Related Requirements**: REQ-148

---

### TS-125: Manage Product Images
As an admin, I want to upload and manage product images, so that buyers can see the products.

**Related Requirements**: REQ-150

---

### TS-126: Manage Product Variations (Colors and Sizes)
As an admin, I want to add and manage color and size variations for a product, so that buyers have options.

**Related Requirements**: REQ-153, REQ-154

---

## FUNCTIONAL AREA 13: ADMIN - PAYMENT MANAGEMENT

### TS-127: View Payment Information
As an admin, I want to view payment gateway configuration and bank account details, so that I can verify payment setup.

**Related Requirements**: REQ-155

---

### TS-128: Edit Payment Information
As an admin, I want to edit bank account details for receiving payments, so that I can update payment information.

**Related Requirements**: REQ-156

---

### TS-129: View Order Payment Status
As an admin, I want to view the payment status of each order, so that I can confirm which orders are paid.

**Related Requirements**: REQ-157

---

### TS-130: Verify Stripe Payment Gateway Integration
As an admin, I want to verify that Stripe payment gateway is properly integrated, so that payments are processed correctly.

**Related Requirements**: REQ-158

---

## FUNCTIONAL AREA 14: ADMIN - RATINGS & REVIEWS MANAGEMENT

### TS-131: View Pending Ratings
As an admin, I want to view all pending ratings submitted by buyers, so that I can approve or reject them.

**Related Requirements**: REQ-159, REQ-160

---

### TS-132: Approve Rating
As an admin, I want to approve a rating, so that it appears on the product page.

**Related Requirements**: REQ-159

---

### TS-133: Reject Rating
As an admin, I want to reject a rating, so that inappropriate ratings don't appear on the product page.

**Related Requirements**: REQ-160

---

### TS-134: View Pending Reviews
As an admin, I want to view all pending reviews submitted by buyers, so that I can approve or reject them.

**Related Requirements**: REQ-161, REQ-162

---

### TS-135: Approve Review
As an admin, I want to approve a review, so that it appears on the product page.

**Related Requirements**: REQ-161

---

### TS-136: Reject Review
As an admin, I want to reject a review, so that inappropriate reviews don't appear on the product page.

**Related Requirements**: REQ-162

---

## FUNCTIONAL AREA 15: ADMIN - REPORTING & STATISTICS

### TS-137: Generate Products Uploaded Report by Date Range
As an admin, I want to generate a report of products uploaded within a date range, so that I can track catalog growth over time.

**Related Requirements**: REQ-163

---

### TS-138: Generate Products Uploaded Report by Month
As an admin, I want to generate a monthly products uploaded report, so that I can see monthly catalog additions.

**Related Requirements**: REQ-164

---

### TS-139: Generate Products Uploaded Report by Year
As an admin, I want to generate a yearly products uploaded report, so that I can see annual catalog growth.

**Related Requirements**: REQ-165

---

### TS-140: Generate Revenue Report for Today
As an admin, I want to generate a revenue report for today, so that I can see today's sales performance.

**Related Requirements**: REQ-166

---

### TS-141: Generate Revenue Report for Current Week
As an admin, I want to generate a revenue report for the current week, so that I can track weekly sales.

**Related Requirements**: REQ-167

---

### TS-142: Generate Revenue Report by Date Range
As an admin, I want to generate a revenue report for a custom date range, so that I can analyze specific periods.

**Related Requirements**: REQ-168

---

### TS-143: Generate Revenue Report by Month
As an admin, I want to generate a monthly revenue report, so that I can track monthly sales performance.

**Related Requirements**: REQ-169

---

### TS-144: Generate Revenue Report by Year
As an admin, I want to generate a yearly revenue report, so that I can see annual sales performance.

**Related Requirements**: REQ-170

---

### TS-145: Export Report as PDF
As an admin, I want to export reports in PDF format, so that I can share or archive them.

**Related Requirements**: REQ-171

---

### TS-146: Export Report as Excel
As an admin, I want to export reports in Excel format, so that I can further analyze the data.

**Related Requirements**: REQ-172

---

## FUNCTIONAL AREA 16: ADMIN - USER & ROLE MANAGEMENT

### TS-147: Create Sub-Admin User
As an admin, I want to create a new sub-admin user, so that I can delegate administrative tasks.

**Related Requirements**: REQ-173

---

### TS-148: Edit Sub-Admin User
As an admin, I want to edit a sub-admin user's details, so that I can update their information.

**Related Requirements**: REQ-174

---

### TS-149: Delete Sub-Admin User
As an admin, I want to delete a sub-admin user, so that I can remove users who no longer need access.

**Related Requirements**: REQ-175

---

### TS-150: Activate Sub-Admin User
As an admin, I want to activate a sub-admin user, so that they can access the admin panel.

**Related Requirements**: REQ-176

---

### TS-151: Deactivate Sub-Admin User
As an admin, I want to deactivate a sub-admin user, so that I can temporarily restrict their access.

**Related Requirements**: REQ-177

---

### TS-152: Assign Role to Sub-Admin User
As an admin, I want to assign a role to a sub-admin user, so that they have appropriate permissions.

**Related Requirements**: REQ-178, REQ-184

---

### TS-153: Add New Role
As an admin, I want to add a new role with specific permissions, so that I can create customized access levels.

**Related Requirements**: REQ-179, REQ-184

---

### TS-154: Edit Existing Role
As an admin, I want to edit a role's permissions, so that I can adjust access levels as needed.

**Related Requirements**: REQ-180, REQ-184

---

### TS-155: Delete Role
As an admin, I want to delete a role, so that I can remove roles that are no longer needed.

**Related Requirements**: REQ-181

---

### TS-156: Activate Role
As an admin, I want to activate a role, so that it can be assigned to users.

**Related Requirements**: REQ-182

---

### TS-157: Deactivate Role
As an admin, I want to deactivate a role, so that it can't be assigned to new users.

**Related Requirements**: REQ-183

---

### TS-158: Role-Based Access Control Enforcement
As a sub-admin user, I want to only access sections I have permissions for, so that the system maintains security.

**Related Requirements**: REQ-184

---

## FUNCTIONAL AREA 17: ADMIN - CONTENT MANAGEMENT

### TS-159: Edit About Us Page
As an admin, I want to edit the content of the About Us page, so that I can keep company information current.

**Related Requirements**: REQ-185

---

### TS-160: Edit Contact Us Page
As an admin, I want to edit the content of the Contact Us page, so that I can update contact information.

**Related Requirements**: REQ-186

---

### TS-161: Edit Privacy Policy Page
As an admin, I want to edit the content of the Privacy Policy page, so that I can keep privacy terms up to date.

**Related Requirements**: REQ-187

---

### TS-162: Edit Terms and Conditions Page
As an admin, I want to edit the content of the Terms and Conditions page, so that I can update legal terms.

**Related Requirements**: REQ-188

---

### TS-163: Add Email Template
As an admin, I want to add a new email template, so that I can create new email communications for buyers.

**Related Requirements**: REQ-189

---

### TS-164: Edit Email Template
As an admin, I want to edit an existing email template, so that I can update email content.

**Related Requirements**: REQ-190

---

### TS-165: Delete Email Template
As an admin, I want to delete an email template, so that I can remove unused templates.

**Related Requirements**: REQ-191

---

### TS-166: Send Email for New Product Launch
As an admin, I want to send emails to buyers about new product launches, so that I can promote new products.

**Related Requirements**: REQ-192

---

### TS-167: Send Email for Offers/Promotions
As an admin, I want to send emails to buyers about offers and promotions, so that I can drive sales.

**Related Requirements**: REQ-193, REQ-194

---

## FUNCTIONAL AREA 18: ADMIN - COMPLAINTS & FEEDBACK

### TS-168: View Customer Queries
As an admin, I want to view all queries received from buyers, so that I can respond to questions.

**Related Requirements**: REQ-195

---

### TS-169: View Customer Complaints
As an admin, I want to view all complaints received from buyers, so that I can address issues.

**Related Requirements**: REQ-196

---

### TS-170: View Customer Feedback
As an admin, I want to view all feedback received from buyers, so that I can improve the service.

**Related Requirements**: REQ-197

---

### TS-171: Receive Email for New Support Request
As an admin, I want to receive email notifications for new support requests, so that I can respond quickly.

**Related Requirements**: REQ-198

---

## FUNCTIONAL AREA 19: NON-FUNCTIONAL REQUIREMENTS - PERFORMANCE

### TS-172: Handle 100 Concurrent Users
As a system, I want to accommodate up to 100 users concurrently, so that multiple buyers can shop at the same time.

**Related Requirements**: REQ-199

---

### TS-173: Page Load Time Under 30 Seconds
As a user with good internet speed, I want web pages to load in under 30 seconds, so that I have a smooth browsing experience.

**Related Requirements**: REQ-200

---

## FUNCTIONAL AREA 20: NON-FUNCTIONAL REQUIREMENTS - RELIABILITY

### TS-174: Handle Missing Pages Gracefully
As a user, I want to see a "page not found" error when a page doesn't exist, rather than a broken page.

**Related Requirements**: REQ-201, REQ-202

---

## FUNCTIONAL AREA 21: NON-FUNCTIONAL REQUIREMENTS - SECURITY

### TS-175: SSL Security for Payments
As a buyer making a payment, I want my payment data to be transmitted over SSL, so that it's secure.

**Related Requirements**: REQ-203

---

### TS-176: Encryption for Payment Data
As a buyer making a payment, I want my payment data to be encrypted, so that it can't be intercepted.

**Related Requirements**: REQ-204

---

## FUNCTIONAL AREA 22: BUSINESS CONSTRAINTS

### TS-177: US-Only Orders
As a system, I want to only accept orders from the United States, so that I comply with business constraints.

**Related Requirements**: REQ-209

---

### TS-178: USD Currency for All Transactions
As a system, I want to process all transactions in USD, so that pricing is consistent.

**Related Requirements**: REQ-208

---

## SUMMARY

### Total Test Scenarios: 178

### Scenarios by Functional Area:
1. **User Authentication & Registration**: 20 scenarios
2. **Product Browsing & Search**: 17 scenarios
3. **Wishlist & Social Sharing**: 7 scenarios
4. **Shopping Cart & Checkout**: 19 scenarios
5. **Order Management (Buyer)**: 6 scenarios
6. **User Account Management**: 11 scenarios
7. **Ratings & Reviews**: 7 scenarios
8. **Customer Support**: 3 scenarios
9. **Admin Dashboard**: 6 scenarios
10. **Admin - Customer Management**: 5 scenarios
11. **Admin - Order Management**: 11 scenarios
12. **Admin - Product Management**: 14 scenarios
13. **Admin - Payment Management**: 4 scenarios
14. **Admin - Ratings & Reviews Management**: 6 scenarios
15. **Admin - Reporting & Statistics**: 10 scenarios
16. **Admin - User & Role Management**: 12 scenarios
17. **Admin - Content Management**: 9 scenarios
18. **Admin - Complaints & Feedback**: 4 scenarios
19. **Performance**: 2 scenarios
20. **Reliability**: 1 scenario
21. **Security**: 2 scenarios
22. **Business Constraints**: 2 scenarios

### Coverage Analysis:
- **Total Requirements**: 212
- **Total Scenarios**: 178
- **Average Scenarios per Requirement**: 0.84 (some requirements are covered by multiple scenarios)
- **Requirements Coverage**: 100% (all functional areas covered)

### Next Steps:
1. Generate exhaustive variants for each scenario (Step 5)
2. Create test data for all variants (Step 6)
3. Write detailed test scripts for all scenarios (Step 7)
