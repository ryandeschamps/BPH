#!/usr/bin/env python3
"""
Generate realistic test data for test variants.

VERSION 2.0.0 - Scenario-Based Architecture

This script supports two modes:
1. Per-Scenario Mode (NEW): Generate test data for individual scenario variants
2. Monolithic Mode (Legacy): Generate test data for all variants in one file

Usage:
    # Generate test data for single scenario
    python3 generate_test_data.py --scenario TS-001 \\
        --variants deliverables/scenarios/TS-001/variants.csv \\
        --output deliverables/scenarios/TS-001/test_data.csv

    # Legacy monolithic mode
    python3 generate_test_data.py --monolithic \\
        --variants deliverables/04_variants.csv \\
        --output deliverables/05_test_data.csv
"""

import csv
import random
import argparse
import sys
from pathlib import Path
from typing import Dict, Any

# Sample data pools
FIRST_NAMES = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Lisa', 'James', 'Mary']
LAST_NAMES = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
PRODUCT_NAMES = ['Cotton T-Shirt', 'Denim Jeans', 'Leather Jacket', 'Summer Dress', 'Wool Sweater',
                 'Casual Shirt', 'Sports Shorts', 'Winter Coat', 'Silk Scarf', 'Canvas Sneakers']
COLORS = ['Red', 'Blue', 'Green', 'Black', 'White', 'Navy', 'Gray', 'Brown', 'Beige', 'Burgundy']
SIZES = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
CATEGORIES = ['Men', 'Women', 'Kids']
SUB_CATEGORIES = ['Shirts', 'Jeans', 'T-Shirts', 'Dresses', 'Jackets', 'Accessories']
ADDRESSES = [
    '123 Main St, New York, NY 10001',
    '456 Oak Ave, Los Angeles, CA 90001',
    '789 Pine Rd, Chicago, IL 60601',
    '321 Elm St, Houston, TX 77001',
    '654 Maple Dr, Phoenix, AZ 85001'
]


def generate_email(first_name: str, last_name: str) -> str:
    """Generate email based on name."""
    return f"{first_name.lower()}.{last_name.lower()}@example.com"


def generate_test_data_row(variant: Dict[str, str]) -> Dict[str, Any]:
    """
    Generate test data for a single variant.

    Args:
        variant: Variant dictionary from CSV

    Returns:
        Test data dictionary
    """
    data = {'Variant_ID': variant['Variant_ID']}

    # User information
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    data['First_Name'] = first_name
    data['Last_Name'] = last_name
    data['Email'] = generate_email(first_name, last_name)
    data['Phone'] = f"+1-{random.randint(200, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    data['Password'] = 'Test@123' if variant.get('Input_Validity') == 'Valid' else 'weak'

    # Product information
    data['Product_Name'] = random.choice(PRODUCT_NAMES)
    data['Product_SKU'] = f"SKU-{random.randint(10000, 99999)}"
    data['Product_Price'] = round(random.uniform(19.99, 299.99), 2)
    data['Product_Category'] = random.choice(CATEGORIES)
    data['Product_Sub_Category'] = random.choice(SUB_CATEGORIES)
    data['Product_Color'] = random.choice(COLORS)
    data['Product_Size'] = random.choice(SIZES)

    # Order information
    data['Order_ID'] = f"ORD-{random.randint(100000, 999999)}"
    data['Order_Quantity'] = random.randint(1, 5)
    data['Order_Total'] = round(data['Product_Price'] * data['Order_Quantity'], 2)

    # Address information
    data['Billing_Address'] = random.choice(ADDRESSES)
    data['Shipping_Address'] = random.choice(ADDRESSES)
    data['ZIP_Code'] = random.randint(10001, 99999)

    # Payment information
    payment_method = variant.get('Payment_Method', 'N/A')
    if payment_method in ['Credit_Card', 'Debit_Card']:
        data['Card_Number'] = f"4532-****-****-{random.randint(1000, 9999)}"  # Masked
        data['Card_Expiry'] = f"{random.randint(1, 12):02d}/{random.randint(25, 30)}"
        data['CVV'] = '***'  # Masked for security
    else:
        data['Card_Number'] = 'N/A'
        data['Card_Expiry'] = 'N/A'
        data['CVV'] = 'N/A'

    # Tracking information
    data['Tracking_ID'] = f"TRK-{random.randint(100000000, 999999999)}"
    data['Shipping_Carrier'] = random.choice(['USPS', 'FedEx', 'UPS', 'DHL'])

    # Rating/Review information
    data['Rating'] = random.randint(1, 5)
    data['Review_Text'] = f"Great product! Would recommend to others. Quality is {random.choice(['excellent', 'good', 'fair'])}."

    # Test execution metadata
    data['Browser'] = variant.get('Browser', 'N/A')
    data['Device'] = variant.get('Device', 'N/A')
    data['Network_Speed'] = variant.get('Network_Speed', 'N/A')
    data['User_Type'] = variant.get('User_Type', 'N/A')

    return data


def generate_test_data_for_variants(
    variants_file: Path,
    output_file: Path,
    verbose: bool = False
) -> int:
    """
    Generate test data for all variants in a CSV file.

    Args:
        variants_file: Input variants CSV file
        output_file: Output test data CSV file
        verbose: Enable verbose output

    Returns:
        Number of test data rows generated
    """
    if not variants_file.exists():
        raise FileNotFoundError(f"Variants file not found: {variants_file}")

    if verbose:
        print(f"Reading variants from {variants_file}...")

    # Read variants
    variants = []
    with open(variants_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        variants = list(reader)

    if verbose:
        print(f"✓ Loaded {len(variants)} variants")
        print(f"Generating test data...")

    # Generate test data
    test_data = []
    for i, variant in enumerate(variants):
        if verbose and (i + 1) % 5000 == 0:
            print(f"  Progress: {i + 1}/{len(variants)} ({(i+1)/len(variants)*100:.1f}%)")
        test_data.append(generate_test_data_row(variant))

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write test data to CSV
    if verbose:
        print(f"Writing test data to {output_file}...")

    if test_data:
        fieldnames = test_data[0].keys()
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(test_data)

        if verbose:
            print(f"✓ Generated test data for {len(test_data)} variants")
            print(f"✓ Saved to {output_file}")

        # Verification
        if len(test_data) == len(variants):
            if verbose:
                print(f"✅ Verification PASSED: Row count matches ({len(test_data)} rows)")
        else:
            print(f"❌ Verification FAILED: Row count mismatch (expected {len(variants)}, got {len(test_data)})")

    return len(test_data)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate realistic test data for test variants (Scenario-Based Architecture v2.0)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate test data for single scenario
  python3 generate_test_data.py --scenario TS-001 \\
      --variants deliverables/scenarios/TS-001/variants.csv \\
      --output deliverables/scenarios/TS-001/test_data.csv

  # Legacy monolithic mode
  python3 generate_test_data.py --monolithic \\
      --variants deliverables/04_variants.csv \\
      --output deliverables/05_test_data.csv
        """
    )

    # Mode selection
    mode_group = parser.add_mutually_exclusive_group(required=False)
    mode_group.add_argument(
        '--scenario',
        help='Scenario ID (for logging purposes, e.g., TS-001)'
    )
    mode_group.add_argument(
        '--monolithic',
        action='store_true',
        help='Monolithic mode (legacy)'
    )

    # Required arguments
    parser.add_argument(
        '--variants',
        type=Path,
        required=True,
        help='Input variants CSV file'
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='Output test data CSV file'
    )

    # Options
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    try:
        if args.scenario and args.verbose:
            print(f"Generating test data for scenario: {args.scenario}")

        row_count = generate_test_data_for_variants(
            variants_file=args.variants,
            output_file=args.output,
            verbose=args.verbose
        )

        if not args.verbose:
            # Always print summary even in non-verbose mode
            print(f"✓ Generated {row_count:,} test data rows")
            print(f"  Output: {args.output}")

        return 0

    except Exception as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
