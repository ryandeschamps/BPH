#!/usr/bin/env python3
"""
Generate exhaustive test variants using Cartesian product approach.

VERSION 2.0.0 - Scenario-Based Architecture

This script supports two modes:
1. Per-Scenario Mode (NEW): Generate variants for individual scenarios in isolated folders
2. Monolithic Mode (Legacy): Generate all variants in one CSV file

Usage:
    # Generate single scenario
    python3 generate_variants.py --scenario TS-001 --output-dir deliverables/scenarios

    # Generate specific scenarios
    python3 generate_variants.py --scenarios TS-001,TS-002,TS-010 --output-dir deliverables/scenarios

    # Generate all scenarios (new architecture)
    python3 generate_variants.py --all --output-dir deliverables/scenarios

    # Legacy monolithic mode
    python3 generate_variants.py --monolithic --output deliverables/04_variants.csv
"""

import csv
import itertools
import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

# Global parameters applicable across scenarios
GLOBAL_PARAMS = {
    'Browser': ['Chrome', 'Firefox', 'Safari', 'Edge'],
    'Device': ['Desktop', 'Mobile', 'Tablet'],
    'Network_Speed': ['High', 'Medium', 'Low']
}

# Scenario definitions - extracted for configurability
SCENARIO_DEFINITIONS = {
    'TS-001': {
        'title': 'New Buyer Registration with Email Verification',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Valid', 'Invalid'],
            'Field_Values': ['All_Valid', 'Missing_FirstName', 'Missing_LastName',
                            'Missing_Email', 'Invalid_Email', 'Missing_Contact',
                            'Invalid_Contact', 'Missing_Password', 'Weak_Password',
                            'Password_Mismatch', 'Terms_Not_Accepted', 'Duplicate_Email']
        }
    },
    'TS-002': {
        'title': 'Registration with Invalid Email Format',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Email_Format': ['Missing_At', 'Invalid_Domain', 'Special_Chars', 'No_Domain']
        }
    },
    'TS-003': {
        'title': 'Registration with Password Mismatch',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Password_State': ['Mismatch_One_Char', 'Mismatch_Multiple_Chars', 'Empty_Confirm']
        }
    },
    'TS-004': {
        'title': 'Registration with Existing Email',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Email_State': ['Active_Account', 'Inactive_Account', 'Unverified_Account']
        }
    },
    'TS-005': {
        'title': 'Registration Without Accepting Terms',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Terms_Accepted': ['No']
        }
    },
    'TS-006': {
        'title': 'Login with Valid Email and Password',
        'params': {
            'User_Type': ['Buyer'],
            'Input_Validity': ['Valid'],
            'Account_State': ['Active_Verified', 'Active_Multiple_Sessions']
        }
    },
    'TS-007': {
        'title': 'Login with Invalid Credentials',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Credential_Error': ['Wrong_Email', 'Wrong_Password', 'Both_Wrong', 'Empty_Email', 'Empty_Password']
        }
    },
    'TS-008': {
        'title': 'Login with Unverified Email',
        'params': {
            'User_Type': ['Buyer'],
            'Input_Validity': ['Valid'],
            'Account_State': ['Unverified'],
            'Email_Verification': ['Not_Clicked', 'Link_Expired']
        }
    },
    'TS-009': {
        'title': 'Social Login with Facebook',
        'params': {
            'User_Type': ['Visitor'],
            'Auth_Method': ['Facebook'],
            'Input_Validity': ['Valid', 'Invalid'],
            'OAuth_State': ['Authorized', 'Denied', 'Already_Linked', 'New_Account']
        }
    },
    'TS-010': {
        'title': 'Social Login with Google',
        'params': {
            'User_Type': ['Visitor'],
            'Auth_Method': ['Google'],
            'Input_Validity': ['Valid', 'Invalid'],
            'OAuth_State': ['Authorized', 'Denied', 'Already_Linked', 'New_Account']
        }
    },
    'TS-011': {
        'title': 'Password Reset Request',
        'params': {
            'User_Type': ['Buyer'],
            'Input_Validity': ['Valid'],
            'Email_State': ['Registered', 'Verified'],
            'Reset_Link_State': ['Valid', 'Expired', 'Already_Used']
        }
    },
    'TS-012': {
        'title': 'Password Reset with Invalid Email',
        'params': {
            'User_Type': ['Visitor'],
            'Input_Validity': ['Invalid'],
            'Email_State': ['Not_Registered', 'Invalid_Format']
        }
    },
    'TS-013': {
        'title': 'Search Products by Keyword as Visitor',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Input_Validity': ['Valid'],
            'Search_Query': ['Single_Keyword', 'Multiple_Keywords', 'Partial_Match', 'Exact_Match'],
            'Results_Count': ['Many_Results', 'Few_Results', 'One_Result']
        }
    },
    'TS-014': {
        'title': 'Search Products with No Results',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Input_Validity': ['Valid'],
            'Search_Query': ['No_Match', 'Typo', 'Special_Characters'],
            'Results_Count': ['Zero']
        }
    },
    'TS-015': {
        'title': 'Browse Products by Category',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Category_Type': ['Men', 'Women', 'Kids'],
            'Product_Count': ['Many', 'Few', 'One', 'None']
        }
    },
    'TS-016': {
        'title': 'Browse Products by Sub-Category',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Sub_Category_Type': ['Shirts', 'Jeans', 'TShirts', 'Dresses', 'Accessories'],
            'Product_Count': ['Many', 'Few', 'One', 'None']
        }
    },
    'TS-017': {
        'title': 'Filter Product Listing',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Filter_Type': ['Size', 'Color', 'Price_Range', 'Multiple_Filters'],
            'Filter_Value': ['Single_Value', 'Multiple_Values']
        }
    },
    'TS-018': {
        'title': 'Sort Product Listing',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Sort_By': ['Price_Low_High', 'Price_High_Low', 'Rating_High_Low', 'Newest_First', 'Oldest_First']
        }
    },
    'TS-019': {
        'title': 'View Product Details as Visitor',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Product_State': ['Active', 'Has_Variations', 'No_Variations', 'Has_Reviews', 'No_Reviews'],
            'Image_Count': ['Single_Image', 'Multiple_Images']
        }
    },
    'TS-020': {
        'title': 'Check Shipping Availability by PIN Code',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Input_Validity': ['Valid', 'Invalid'],
            'PIN_Code_State': ['Available', 'Not_Available', 'Invalid_Format']
        }
    },
    'TS-021': {
        'title': 'View Product Variations',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Variation_Type': ['Size_Only', 'Color_Only', 'Size_And_Color'],
            'Variation_Availability': ['All_Available', 'Some_Out_Of_Stock', 'All_Out_Of_Stock']
        }
    },
    'TS-022': {
        'title': 'View Product Ratings and Reviews',
        'params': {
            'User_Type': ['Visitor', 'Buyer'],
            'Review_Count': ['No_Reviews', 'Few_Reviews', 'Many_Reviews'],
            'Rating_Range': ['High_Rated', 'Medium_Rated', 'Low_Rated', 'Mixed_Ratings']
        }
    },
    'TS-023': {
        'title': 'Add Product to Cart as Logged-in Buyer',
        'params': {
            'User_Type': ['Buyer'],
            'Product_Variation': ['No_Variation', 'Size_Selected', 'Color_Selected', 'Size_And_Color'],
            'Quantity': ['Single', 'Multiple'],
            'Cart_State': ['Empty', 'Has_Items']
        }
    },
    'TS-024': {
        'title': 'Add Product to Cart Without Login',
        'params': {
            'User_Type': ['Visitor'],
            'Redirect_Action': ['Login', 'Register', 'Cancel']
        }
    },
    'TS-025': {
        'title': 'Add Multiple Quantities of Same Product',
        'params': {
            'User_Type': ['Buyer'],
            'Quantity': ['Two', 'Five', 'Ten', 'Hundred'],
            'Stock_Level': ['Sufficient', 'Insufficient', 'Exact_Match']
        }
    },
    'TS-026': {
        'title': 'View Shopping Cart',
        'params': {
            'User_Type': ['Buyer'],
            'Cart_State': ['Empty', 'Single_Item', 'Multiple_Items', 'Mixed_Variations'],
            'Item_Availability': ['All_Available', 'Some_Out_Of_Stock', 'Price_Changed']
        }
    },
    'TS-027': {
        'title': 'Update Item Quantity in Cart',
        'params': {
            'User_Type': ['Buyer'],
            'Quantity_Change': ['Increase', 'Decrease', 'Max_Limit', 'Zero'],
            'Stock_Level': ['Sufficient', 'Insufficient']
        }
    },
    'TS-028': {
        'title': 'Remove Item from Cart',
        'params': {
            'User_Type': ['Buyer'],
            'Cart_State': ['Single_Item', 'Multiple_Items'],
            'Removal_Action': ['Remove_One', 'Remove_All', 'Remove_Last_Item']
        }
    },
    'TS-029': {
        'title': 'View Empty Cart',
        'params': {
            'User_Type': ['Buyer'],
            'Cart_State': ['Never_Had_Items', 'Previously_Had_Items', 'Items_Removed']
        }
    },
    'TS-030': {
        'title': 'Add Product to Wishlist as Logged-in Buyer',
        'params': {
            'User_Type': ['Buyer'],
            'Wishlist_State': ['Empty', 'Has_Items', 'Product_Already_In_Wishlist'],
            'Product_State': ['In_Stock', 'Out_Of_Stock']
        }
    },
    'TS-031': {
        'title': 'Add Product to Wishlist Without Login',
        'params': {
            'User_Type': ['Visitor'],
            'Redirect_Action': ['Login', 'Register', 'Cancel']
        }
    },
    'TS-032': {
        'title': 'View Wishlist',
        'params': {
            'User_Type': ['Buyer'],
            'Wishlist_State': ['Empty', 'Single_Item', 'Multiple_Items'],
            'Item_Availability': ['All_Available', 'Some_Out_Of_Stock', 'Price_Changed']
        }
    },
    'TS-033': {
        'title': 'Remove Product from Wishlist',
        'params': {
            'User_Type': ['Buyer'],
            'Wishlist_State': ['Single_Item', 'Multiple_Items'],
            'Removal_Action': ['Remove_One', 'Remove_All']
        }
    },
    'TS-034': {
        'title': 'Move Product from Wishlist to Cart',
        'params': {
            'User_Type': ['Buyer'],
            'Product_State': ['In_Stock', 'Out_Of_Stock', 'Price_Changed'],
            'Cart_State': ['Empty', 'Has_Items']
        }
    },
    'TS-035': {
        'title': 'Checkout as Logged-in Buyer with Valid Data',
        'params': {
            'User_Type': ['Buyer'],
            'Input_Validity': ['Valid'],
            'Payment_Method': ['Credit_Card', 'Debit_Card', 'Net_Banking'],
            'Address_State': ['New_Address', 'Saved_Address'],
            'Cart_Items': ['Single', 'Multiple']
        }
    },
    'TS-036': {
        'title': 'Checkout Without Login',
        'params': {
            'User_Type': ['Visitor'],
            'Redirect_Action': ['Login', 'Register']
        }
    },
    'TS-037': {
        'title': 'Checkout with Same Billing and Shipping Address',
        'params': {
            'User_Type': ['Buyer'],
            'Address_Type': ['Same_Address'],
            'Address_State': ['New', 'Saved'],
            'Payment_Method': ['Credit_Card', 'Debit_Card', 'Net_Banking']
        }
    },
    'TS-038': {
        'title': 'Checkout with Different Billing and Shipping Addresses',
        'params': {
            'User_Type': ['Buyer'],
            'Address_Type': ['Different_Addresses'],
            'Address_State': ['Both_New', 'Both_Saved', 'Mixed'],
            'Payment_Method': ['Credit_Card', 'Debit_Card', 'Net_Banking']
        }
    },
    'TS-039': {
        'title': 'Select Credit/Debit Card Payment Method',
        'params': {
            'User_Type': ['Buyer'],
            'Payment_Method': ['Credit_Card', 'Debit_Card'],
            'Card_Type': ['Visa', 'Mastercard', 'Amex', 'Discover'],
            'Payment_Status': ['Success', 'Declined', 'Timeout']
        }
    },
    'TS-040': {
        'title': 'Select Net Banking Payment Method',
        'params': {
            'User_Type': ['Buyer'],
            'Payment_Method': ['Net_Banking'],
            'Bank': ['Chase', 'BofA', 'Wells_Fargo', 'Citi'],
            'Payment_Status': ['Success', 'Failed', 'Timeout']
        }
    },
    'TS-041': {
        'title': 'Successful Payment and Order Confirmation',
        'params': {
            'User_Type': ['Buyer'],
            'Payment_Method': ['Credit_Card', 'Debit_Card', 'Net_Banking'],
            'Order_Size': ['Single_Item', 'Multiple_Items'],
            'Email_Delivery': ['Delivered', 'Delayed']
        }
    },
    'TS-042': {
        'title': 'Failed Payment Handling',
        'params': {
            'User_Type': ['Buyer'],
            'Payment_Method': ['Credit_Card', 'Debit_Card', 'Net_Banking'],
            'Failure_Reason': ['Insufficient_Funds', 'Invalid_Card', 'Declined', 'Timeout', 'Network_Error'],
            'Retry_Action': ['Retry_Same_Method', 'Change_Method', 'Cancel']
        }
    },
    'TS-043': {
        'title': 'View Order Summary Before Payment',
        'params': {
            'User_Type': ['Buyer'],
            'Cart_Items': ['Single', 'Multiple', 'Mixed_Prices'],
            'Shipping_Cost': ['Standard', 'Express', 'Free'],
            'Tax_Applicable': ['Yes', 'No']
        }
    },
    'TS-044': {
        'title': 'Email Notification for Order Status Updates',
        'params': {
            'User_Type': ['Buyer'],
            'Order_Status': ['Confirmed', 'In_Process', 'Shipped', 'Delivered'],
            'Email_Delivery': ['Immediate', 'Delayed', 'Failed']
        }
    },
}

# Add remaining scenarios (TS-045 to TS-106) with simplified params
REMAINING_SCENARIOS = {
    'TS-045': {'title': 'Share Product on Social Media', 'params': {'User_Type': ['Visitor', 'Buyer'], 'Social_Platform': ['Facebook', 'Twitter', 'Pinterest', 'Instagram']}},
    'TS-046': {'title': 'Share Order on Social Media', 'params': {'User_Type': ['Buyer'], 'Social_Platform': ['Facebook', 'Twitter', 'Pinterest', 'Instagram']}},
    'TS-047': {'title': 'Submit Product Review', 'params': {'User_Type': ['Buyer'], 'Product_State': ['Purchased'], 'Rating': ['1_Star', '2_Star', '3_Star', '4_Star', '5_Star']}},
    'TS-048': {'title': 'Submit Review Without Purchase', 'params': {'User_Type': ['Buyer'], 'Product_State': ['Not_Purchased']}},
    'TS-049': {'title': 'View User Profile as Visitor', 'params': {'User_Type': ['Visitor']}},
    'TS-050': {'title': 'View User Profile as Logged-in Buyer', 'params': {'User_Type': ['Buyer']}},
    'TS-051': {'title': 'Update Profile Information', 'params': {'User_Type': ['Buyer'], 'Field_Updated': ['Email', 'Phone', 'Both']}},
    'TS-052': {'title': 'Change Password', 'params': {'User_Type': ['Buyer'], 'Password_Validity': ['Valid', 'Invalid', 'Weak']}},
    'TS-053': {'title': 'Manage Saved Addresses', 'params': {'User_Type': ['Buyer'], 'Address_Action': ['Add', 'Edit', 'Delete', 'Set_Default']}},
    'TS-054': {'title': 'View Order History', 'params': {'User_Type': ['Buyer'], 'Order_Count': ['None', 'Single', 'Multiple']}},
    'TS-055': {'title': 'View Order Details', 'params': {'User_Type': ['Buyer'], 'Order_Status': ['Open', 'Confirmed', 'Shipped', 'Delivered']}},
    'TS-056': {'title': 'Reorder Previous Order', 'params': {'User_Type': ['Buyer'], 'Reorder_Items': ['Single', 'Multiple', 'Out_Of_Stock']}},
    'TS-057': {'title': 'Track Order Shipment', 'params': {'User_Type': ['Buyer'], 'Order_Status': ['Shipped', 'Delivered']}},
    'TS-058': {'title': 'Cancel Order', 'params': {'User_Type': ['Buyer']}},
    'TS-059': {'title': 'Contact Customer Support as Buyer', 'params': {'User_Type': ['Buyer'], 'Message_Type': ['Question', 'Complaint', 'Feedback']}},
    'TS-060': {'title': 'Contact Customer Support as Visitor', 'params': {'User_Type': ['Visitor'], 'Message_Type': ['Question', 'Inquiry']}},
    'TS-061': {'title': 'Admin Login with Valid Credentials', 'params': {'User_Type': ['Admin'], 'Input_Validity': ['Valid']}},
    'TS-062': {'title': 'Admin Login with Invalid Credentials', 'params': {'User_Type': ['Admin'], 'Input_Validity': ['Invalid'], 'Credential_Error': ['Wrong_Username', 'Wrong_Password', 'Both']}},
    'TS-063': {'title': 'Admin Password Reset', 'params': {'User_Type': ['Admin'], 'Reset_State': ['Valid', 'Expired']}},
    'TS-064': {'title': 'View Admin Dashboard', 'params': {'User_Type': ['Admin']}},
    'TS-065': {'title': 'View All Buyers List', 'params': {'User_Type': ['Admin'], 'Buyer_Filter': ['All', 'Active', 'Inactive']}},
    'TS-066': {'title': 'View Buyer Details', 'params': {'User_Type': ['Admin'], 'Buyer_Status': ['Active', 'Inactive', 'Has_Orders', 'No_Orders']}},
    'TS-067': {'title': 'Edit Buyer Information', 'params': {'User_Type': ['Admin'], 'Edit_Field': ['Name', 'Email', 'Phone', 'Multiple']}},
    'TS-068': {'title': 'Activate Buyer Account', 'params': {'User_Type': ['Admin'], 'Buyer_Status': ['Active']}},
    'TS-069': {'title': 'Deactivate Buyer Account', 'params': {'User_Type': ['Admin'], 'Buyer_Status': ['Inactive']}},
    'TS-070': {'title': 'View All Orders List', 'params': {'User_Type': ['Admin'], 'Order_Filter': ['All', 'By_Status', 'By_Date']}},
    'TS-071': {'title': 'Filter Orders by Status', 'params': {'User_Type': ['Admin'], 'Order_Status': ['Open', 'Confirmed', 'In_Process', 'Shipped', 'Delivered']}},
    'TS-072': {'title': 'View Order Details as Admin', 'params': {'User_Type': ['Admin'], 'Order_Details': ['Basic', 'With_Items', 'With_Payment']}},
    'TS-073': {'title': 'Update Order Status to Confirmed', 'params': {'User_Type': ['Admin'], 'Status_Change': ['Open_To_Confirmed']}},
    'TS-074': {'title': 'Update Order Status to In Process', 'params': {'User_Type': ['Admin'], 'Status_Change': ['Confirmed_To_InProcess']}},
    'TS-075': {'title': 'Update Order Status to Shipped', 'params': {'User_Type': ['Admin'], 'Status_Change': ['InProcess_To_Shipped'], 'Tracking_Data': ['Complete', 'Partial']}},
    'TS-076': {'title': 'Update Order Status to Delivered', 'params': {'User_Type': ['Admin'], 'Status_Change': ['Shipped_To_Delivered']}},
    'TS-077': {'title': 'Edit Order Details', 'params': {'User_Type': ['Admin'], 'Edit_Type': ['Address', 'Items', 'Quantity']}},
    'TS-078': {'title': 'Add New Product', 'params': {'User_Type': ['Admin'], 'Product_Type': ['Simple', 'With_Variations'], 'Image_Count': ['Single', 'Multiple']}},
    'TS-079': {'title': 'Edit Product Details', 'params': {'User_Type': ['Admin'], 'Edit_Field': ['Name', 'Price', 'Description', 'Images', 'Variations']}},
    'TS-080': {'title': 'Activate Product', 'params': {'User_Type': ['Admin'], 'Product_Status': ['Active']}},
    'TS-081': {'title': 'Deactivate Product', 'params': {'User_Type': ['Admin'], 'Product_Status': ['Inactive']}},
    'TS-082': {'title': 'Delete Product', 'params': {'User_Type': ['Admin'], 'Product_Status': ['Any'], 'Has_Orders': ['Yes', 'No']}},
    'TS-083': {'title': 'Add Product Category', 'params': {'User_Type': ['Admin'], 'Category_Level': ['Top_Level']}},
    'TS-084': {'title': 'Add Product Sub-Category', 'params': {'User_Type': ['Admin'], 'Category_Level': ['Sub_Level']}},
    'TS-085': {'title': 'Edit Category', 'params': {'User_Type': ['Admin'], 'Edit_Field': ['Name', 'Description']}},
    'TS-086': {'title': 'Delete Category', 'params': {'User_Type': ['Admin'], 'Category_Status': ['Active']}},
    'TS-087': {'title': 'Approve Product Review', 'params': {'User_Type': ['Admin'], 'Review_Status': ['Pending'], 'Action': ['Approve']}},
    'TS-088': {'title': 'Reject Product Review', 'params': {'User_Type': ['Admin'], 'Review_Status': ['Pending'], 'Action': ['Reject']}},
    'TS-089': {'title': 'Manage CMS Pages', 'params': {'User_Type': ['Admin'], 'CMS_Page': ['About_Us', 'Contact_Us', 'Privacy_Policy', 'Terms']}},
    'TS-090': {'title': 'Create Email Template', 'params': {'User_Type': ['Admin'], 'Template_Type': ['Promotional', 'Transactional']}},
    'TS-091': {'title': 'Send Bulk Email', 'params': {'User_Type': ['Admin'], 'Target_Audience': ['All_Buyers', 'Filtered']}},
    'TS-092': {'title': 'Generate Sales Report', 'params': {'User_Type': ['Admin'], 'Report_Period': ['Date_Range', 'Month', 'Year']}},
    'TS-093': {'title': 'View Sales Analytics', 'params': {'User_Type': ['Admin'], 'Report_Period': ['Today', 'Week', 'Month', 'Year', 'Custom']}},
    'TS-094': {'title': 'Export Report as PDF', 'params': {'User_Type': ['Admin'], 'Export_Format': ['PDF']}},
    'TS-095': {'title': 'Export Report as Excel', 'params': {'User_Type': ['Admin'], 'Export_Format': ['Excel']}},
    'TS-096': {'title': 'Create Sub-Admin Account', 'params': {'User_Type': ['Admin'], 'Role_Type': ['Content_Manager', 'Order_Manager', 'Customer_Support']}},
    'TS-097': {'title': 'Edit Sub-Admin Account', 'params': {'User_Type': ['Admin'], 'Edit_Type': ['Username', 'Password', 'Role']}},
    'TS-098': {'title': 'Activate Sub-Admin Account', 'params': {'User_Type': ['Admin'], 'Sub_Admin_Status': ['Active']}},
    'TS-099': {'title': 'Deactivate Sub-Admin Account', 'params': {'User_Type': ['Admin'], 'Sub_Admin_Status': ['Inactive']}},
    'TS-100': {'title': 'View Customer Feedback', 'params': {'User_Type': ['Admin'], 'Feedback_Type': ['Complaint', 'Question', 'Feedback']}},
    'TS-101': {'title': 'Manage Payment Gateway Settings', 'params': {'User_Type': ['Admin'], 'Payment_Status': ['Pending', 'Completed', 'Failed']}},
    'TS-102': {'title': 'Configure Bank Account Details', 'params': {'User_Type': ['Admin'], 'Bank_Field': ['Account_Number', 'Routing', 'Bank_Name']}},
    'TS-103': {'title': 'Load Testing with Concurrent Users', 'params': {'Load_Type': ['Concurrent_Users'], 'User_Count': ['50', '100', '150']}},
    'TS-104': {'title': 'Page Load Performance Testing', 'params': {'Page_Type': ['Home', 'Product_Listing', 'Product_Detail', 'Cart', 'Checkout'], 'Load_Time': ['Fast', 'Medium', 'Slow']}},
    'TS-105': {'title': 'Error Handling and Recovery', 'params': {'Error_Type': ['404', '500', 'Timeout']}},
    'TS-106': {'title': 'Security Testing', 'params': {'Security_Type': ['SSL_Certificate', 'HTTPS', 'Encrypted_Data']}},
}

# Merge all scenario definitions
SCENARIO_DEFINITIONS.update(REMAINING_SCENARIOS)


@dataclass
class ScenarioMetrics:
    """Metrics for a generated scenario"""
    scenario_id: str
    scenario_title: str
    variant_count: int
    expected_variant_count: int
    parameters: Dict[str, int] = field(default_factory=dict)
    output_file: str = ""
    status: str = "success"
    error_message: str = ""


def generate_variants_for_scenario(
    scenario_id: str,
    scenario_params: Dict[str, List[str]],
    global_params: Optional[Dict[str, List[str]]] = None
) -> List[Dict[str, Any]]:
    """
    Generate all possible variants for a scenario using Cartesian product.

    Args:
        scenario_id: e.g., "TS-001"
        scenario_params: Scenario-specific parameters
        global_params: Cross-cutting parameters (Browser, Device, etc.)

    Returns:
        List of variant dictionaries
    """
    if global_params is None:
        global_params = GLOBAL_PARAMS

    # Combine scenario-specific params with global params
    all_params = {**scenario_params, **global_params}

    # Get parameter names and values
    param_names = list(all_params.keys())
    param_values = [all_params[name] for name in param_names]

    # Generate Cartesian product
    variants = []

    for combination in itertools.product(*param_values):
        variant = {
            'Scenario_ID': scenario_id,
            'Variant_ID': f'V{len(variants) + 1:05d}'  # V00001, V00002, etc.
        }

        # Add parameter values
        for i, param_name in enumerate(param_names):
            variant[param_name] = combination[i]

        variants.append(variant)

    return variants


def calculate_expected_variant_count(
    scenario_params: Dict[str, List[str]],
    global_params: Optional[Dict[str, List[str]]] = None
) -> int:
    """Calculate expected number of variants (Cartesian product size)"""
    if global_params is None:
        global_params = GLOBAL_PARAMS

    all_params = {**scenario_params, **global_params}

    count = 1
    for values in all_params.values():
        count *= len(values)

    return count


def write_variants_to_csv(
    variants: List[Dict[str, Any]],
    output_file: Path
) -> None:
    """Write variants to CSV file"""
    if not variants:
        raise ValueError("No variants to write")

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Get all unique column names
    all_columns = set()
    for variant in variants:
        all_columns.update(variant.keys())

    # Ensure Scenario_ID and Variant_ID are first columns
    column_order = ['Scenario_ID', 'Variant_ID']
    other_columns = sorted(all_columns - set(column_order))
    all_column_names = column_order + other_columns

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_column_names)
        writer.writeheader()

        for variant in variants:
            # Fill missing columns with 'N/A'
            row = {col: variant.get(col, 'N/A') for col in all_column_names}
            writer.writerow(row)


def save_scenario_metrics(
    metrics: ScenarioMetrics,
    output_dir: Path
) -> None:
    """Save scenario metrics to JSON file"""
    metrics_file = output_dir / 'metrics.json'

    metrics_dict = {
        'scenario_id': metrics.scenario_id,
        'scenario_title': metrics.scenario_title,
        'variant_count': metrics.variant_count,
        'expected_variant_count': metrics.expected_variant_count,
        'parameters': metrics.parameters,
        'output_file': metrics.output_file,
        'status': metrics.status,
        'error_message': metrics.error_message
    }

    with open(metrics_file, 'w') as f:
        json.dump(metrics_dict, f, indent=2)


def sanitize_folder_name(title: str) -> str:
    """Convert scenario title to safe folder name"""
    # Replace spaces and special characters
    safe_name = title.replace(' ', '_')
    safe_name = ''.join(c for c in safe_name if c.isalnum() or c in ['_', '-'])
    return safe_name[:50]  # Limit length


def generate_single_scenario(
    scenario_id: str,
    output_base_dir: Path,
    verbose: bool = False
) -> ScenarioMetrics:
    """
    Generate variants for a single scenario.

    Args:
        scenario_id: e.g., "TS-001"
        output_base_dir: Base directory for scenarios
        verbose: Enable verbose output

    Returns:
        ScenarioMetrics object
    """
    if scenario_id not in SCENARIO_DEFINITIONS:
        raise ValueError(f"Scenario {scenario_id} not found in definitions")

    scenario_def = SCENARIO_DEFINITIONS[scenario_id]
    scenario_title = scenario_def['title']
    scenario_params = scenario_def['params']

    # Create scenario directory
    folder_name = f"{scenario_id}_{sanitize_folder_name(scenario_title)}"
    scenario_dir = output_base_dir / folder_name
    scenario_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"\n[{scenario_id}] Generating variants for: {scenario_title}")

    # Calculate expected count
    expected_count = calculate_expected_variant_count(scenario_params, GLOBAL_PARAMS)

    if verbose:
        print(f"[{scenario_id}] Expected variants: {expected_count:,}")

    # Generate variants
    variants = generate_variants_for_scenario(scenario_id, scenario_params, GLOBAL_PARAMS)

    # Verify count
    actual_count = len(variants)
    if actual_count != expected_count:
        print(f"WARNING: Expected {expected_count} variants but generated {actual_count}")

    # Write to CSV
    output_file = scenario_dir / 'variants.csv'
    write_variants_to_csv(variants, output_file)

    if verbose:
        print(f"[{scenario_id}] ✓ Generated {actual_count:,} variants → {output_file}")

    # Collect parameter statistics
    param_stats = {}
    all_params = {**scenario_params, **GLOBAL_PARAMS}
    for param_name, param_values in all_params.items():
        param_stats[param_name] = len(param_values)

    # Create metrics
    metrics = ScenarioMetrics(
        scenario_id=scenario_id,
        scenario_title=scenario_title,
        variant_count=actual_count,
        expected_variant_count=expected_count,
        parameters=param_stats,
        output_file=str(output_file),
        status="success"
    )

    # Save metrics
    save_scenario_metrics(metrics, scenario_dir)

    return metrics


def generate_monolithic(output_file: Path, verbose: bool = False) -> int:
    """
    Generate all variants in one monolithic CSV (legacy mode).

    Args:
        output_file: Path to output CSV
        verbose: Enable verbose output

    Returns:
        Total variant count
    """
    print("Generating variants in MONOLITHIC mode (legacy)...")

    all_variants = []
    variant_id_counter = 1

    for scenario_id in sorted(SCENARIO_DEFINITIONS.keys()):
        scenario_def = SCENARIO_DEFINITIONS[scenario_id]

        if verbose:
            print(f"Processing {scenario_id}: {scenario_def['title']}")

        # Generate variants for this scenario
        variants = generate_variants_for_scenario(
            scenario_id,
            scenario_def['params'],
            GLOBAL_PARAMS
        )

        # Reassign global variant IDs
        for v in variants:
            v['Variant_ID'] = f'V{variant_id_counter:05d}'
            variant_id_counter += 1

        all_variants.extend(variants)

    # Write all variants to one file
    write_variants_to_csv(all_variants, output_file)

    print(f"\n✓ Generated {len(all_variants):,} variants in monolithic file")
    print(f"✓ Saved to {output_file}")
    print(f"✓ Variants per scenario: {len(all_variants) / len(SCENARIO_DEFINITIONS):.1f} average")

    return len(all_variants)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate exhaustive test variants (Scenario-Based Architecture v2.0)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate single scenario
  python3 generate_variants.py --scenario TS-001 --output-dir deliverables/scenarios

  # Generate specific scenarios
  python3 generate_variants.py --scenarios TS-001,TS-002,TS-010 --output-dir deliverables/scenarios

  # Generate all scenarios (new architecture)
  python3 generate_variants.py --all --output-dir deliverables/scenarios

  # Legacy monolithic mode
  python3 generate_variants.py --monolithic --output deliverables/04_variants.csv
        """
    )

    # Mode selection
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        '--scenario',
        help='Generate single scenario (e.g., TS-001)'
    )
    mode_group.add_argument(
        '--scenarios',
        help='Generate specific scenarios (comma-separated, e.g., TS-001,TS-002,TS-010)'
    )
    mode_group.add_argument(
        '--all',
        action='store_true',
        help='Generate all scenarios'
    )
    mode_group.add_argument(
        '--monolithic',
        action='store_true',
        help='Generate monolithic CSV (legacy mode)'
    )

    # Output options
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('deliverables/scenarios'),
        help='Base output directory for scenarios (default: deliverables/scenarios)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Output file for monolithic mode (default: deliverables/04_variants.csv)'
    )

    # Other options
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    try:
        if args.monolithic:
            # Legacy monolithic mode
            output_file = args.output or Path('deliverables/04_variants.csv')
            generate_monolithic(output_file, args.verbose)

        elif args.scenario:
            # Single scenario
            metrics = generate_single_scenario(args.scenario, args.output_dir, args.verbose)
            print(f"\n✓ Generated {metrics.variant_count:,} variants for {args.scenario}")
            print(f"  Output: {metrics.output_file}")

        elif args.scenarios:
            # Multiple specific scenarios
            scenario_list = [s.strip() for s in args.scenarios.split(',')]
            all_metrics = []

            for scenario_id in scenario_list:
                try:
                    metrics = generate_single_scenario(scenario_id, args.output_dir, args.verbose)
                    all_metrics.append(metrics)
                except Exception as e:
                    print(f"ERROR processing {scenario_id}: {e}")

            # Summary
            total_variants = sum(m.variant_count for m in all_metrics)
            print(f"\n{'='*60}")
            print(f"SUMMARY: Generated {total_variants:,} variants across {len(all_metrics)} scenarios")
            print(f"{'='*60}")

        elif args.all:
            # All scenarios
            all_metrics = []
            total_variants = 0

            print(f"Generating all {len(SCENARIO_DEFINITIONS)} scenarios...")
            print(f"Output directory: {args.output_dir}")
            print(f"{'='*60}\n")

            for idx, scenario_id in enumerate(sorted(SCENARIO_DEFINITIONS.keys()), 1):
                try:
                    metrics = generate_single_scenario(scenario_id, args.output_dir, args.verbose)
                    all_metrics.append(metrics)
                    total_variants += metrics.variant_count

                    # Progress update
                    if not args.verbose and idx % 10 == 0:
                        print(f"Progress: {idx}/{len(SCENARIO_DEFINITIONS)} scenarios ({idx/len(SCENARIO_DEFINITIONS)*100:.1f}%)")

                except Exception as e:
                    print(f"ERROR processing {scenario_id}: {e}")
                    # Continue with other scenarios

            # Final summary
            print(f"\n{'='*60}")
            print(f"VARIANT GENERATION COMPLETE")
            print(f"{'='*60}")
            print(f"  Total Scenarios: {len(all_metrics)}")
            print(f"  Total Variants: {total_variants:,}")
            print(f"  Avg Variants per Scenario: {total_variants / len(all_metrics):.1f}")

            # Find min/max
            if all_metrics:
                min_scenario = min(all_metrics, key=lambda m: m.variant_count)
                max_scenario = max(all_metrics, key=lambda m: m.variant_count)

                print(f"  Min: {min_scenario.variant_count:,} ({min_scenario.scenario_id})")
                print(f"  Max: {max_scenario.variant_count:,} ({max_scenario.scenario_id})")

            print(f"  Output Directory: {args.output_dir}")
            print(f"{'='*60}\n")

        return 0

    except Exception as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
