#!/usr/bin/env python3
"""
Test Script Generator from Variants

This script automatically generates test scripts for every variant by combining:
- Test scenario descriptions from 03_test_scenarios.md
- Variant parameters from 04_variants.csv
- Concrete test data from 05_test_data.csv

Generates: TS-XXX_VXXX.txt for each variant with specific GIVEN/WHEN/THEN steps.

Benefits:
- 100% automated - no LLM needed for script generation
- Perfect consistency - no quality degradation
- Instant generation - thousands of scripts in seconds
- Maintainable - update templates, regenerate all

Author: QA Automation Skill
Version: 1.0.0
"""

import csv
import re
import sys
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
from datetime import datetime
import time


@dataclass
class TestScenario:
    """Represents a test scenario"""
    scenario_id: str
    title: str
    description: str
    related_requirements: List[str] = field(default_factory=list)
    priority: str = "Medium"


@dataclass
class Variant:
    """Represents a test variant"""
    variant_id: str
    scenario_id: str
    parameters: Dict[str, str] = field(default_factory=dict)


@dataclass
class TestData:
    """Represents test data for a variant"""
    variant_id: str
    data_fields: Dict[str, str] = field(default_factory=dict)


class TestScriptGenerator:
    """
    Generates test scripts from variants and test data.
    """

    def __init__(self, verbose: bool = False):
        """Initialize the generator"""
        self.verbose = verbose
        self._setup_logging()

        self.scenarios: Dict[str, TestScenario] = {}
        self.variants: Dict[str, Variant] = {}
        self.test_data: Dict[str, TestData] = {}

        self.scripts_generated = 0
        self.start_time = None

    def _setup_logging(self):
        """Configure logging"""
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def load_scenarios(self, scenarios_file: str):
        """Load test scenarios from markdown file"""
        self.logger.info(f"Loading scenarios from {scenarios_file}")

        with open(scenarios_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern: ### TS-XXX: Title
        scenario_pattern = re.compile(
            r'### (TS-\d+):\s*(.+?)$',
            re.MULTILINE
        )

        # Split content by scenarios
        scenarios = scenario_pattern.split(content)[1:]  # Skip header

        for i in range(0, len(scenarios), 3):
            if i + 2 >= len(scenarios):
                break

            scenario_id = scenarios[i].strip()
            title = scenarios[i + 1].strip()
            body = scenarios[i + 2].strip() if i + 2 < len(scenarios) else ""

            # Extract description (first paragraph, usually user story)
            description_match = re.search(r'^(.+?)(?:\n\n|\*\*)', body, re.DOTALL)
            description = description_match.group(1).strip() if description_match else ""

            # Extract related requirements
            req_match = re.search(r'\*\*Related Requirements\*\*:\s*(.+)', body)
            related_reqs = []
            if req_match:
                req_text = req_match.group(1).strip()
                related_reqs = [r.strip() for r in req_text.split(',')]

            # Extract priority
            priority_match = re.search(r'\*\*Priority\*\*:\s*(\w+)', body)
            priority = priority_match.group(1) if priority_match else "Medium"

            self.scenarios[scenario_id] = TestScenario(
                scenario_id=scenario_id,
                title=title,
                description=description,
                related_requirements=related_reqs,
                priority=priority
            )

        self.logger.info(f"✓ Loaded {len(self.scenarios)} scenarios")

    def load_variants(self, variants_file: str):
        """Load variants from CSV"""
        self.logger.info(f"Loading variants from {variants_file}")

        with open(variants_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                variant_id = row.get('Variant_ID', '').strip()
                scenario_id = row.get('Scenario_ID', '').strip()

                if not variant_id or not scenario_id:
                    continue

                # Get all parameters (exclude ID columns)
                parameters = {
                    k: v for k, v in row.items()
                    if k not in ['Variant_ID', 'Scenario_ID']
                }

                self.variants[variant_id] = Variant(
                    variant_id=variant_id,
                    scenario_id=scenario_id,
                    parameters=parameters
                )

        self.logger.info(f"✓ Loaded {len(self.variants)} variants")

    def load_test_data(self, test_data_file: str):
        """Load test data from CSV"""
        self.logger.info(f"Loading test data from {test_data_file}")

        with open(test_data_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                variant_id = row.get('Variant_ID', '').strip()

                if not variant_id:
                    continue

                # Get all data fields (exclude Variant_ID)
                data_fields = {
                    k: v for k, v in row.items()
                    if k != 'Variant_ID'
                }

                self.test_data[variant_id] = TestData(
                    variant_id=variant_id,
                    data_fields=data_fields
                )

        self.logger.info(f"✓ Loaded test data for {len(self.test_data)} variants")

    def generate_script_content(self, variant: Variant) -> str:
        """Generate test script content for a variant"""
        scenario = self.scenarios.get(variant.scenario_id)
        data = self.test_data.get(variant.variant_id)

        if not scenario:
            return f"ERROR: Scenario {variant.scenario_id} not found"

        # Build script sections
        header = self._build_header(scenario, variant)
        given_section = self._build_given_section(scenario, variant, data)
        when_section = self._build_when_section(scenario, variant, data)
        then_section = self._build_then_section(scenario, variant, data)
        expected_result = self._build_expected_result(scenario, variant, data)

        # Combine sections
        script = f"""{header}

{given_section}

{when_section}

{then_section}

{expected_result}

VARIANT PARAMETERS:
{self._format_parameters(variant.parameters)}

TEST DATA:
{self._format_test_data(data) if data else 'N/A'}

RELATED REQUIREMENTS:
{', '.join(scenario.related_requirements) if scenario.related_requirements else 'N/A'}
"""

        return script

    def _build_header(self, scenario: TestScenario, variant: Variant) -> str:
        """Build script header"""
        return f"""TEST SCRIPT: {variant.scenario_id}_{variant.variant_id}

SCENARIO: {scenario.title}
VARIANT: {variant.variant_id}
PRIORITY: {scenario.priority}
GENERATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

DESCRIPTION:
{scenario.description}"""

    def _build_given_section(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> str:
        """Build GIVEN section based on variant parameters"""
        given_steps = ["GIVEN:"]

        params = variant.parameters

        # User type / authentication state
        user_type = params.get('User_Type', 'User')
        if user_type in ['Buyer', 'Admin', 'Sub_Admin', 'Seller']:
            email = data.data_fields.get('Email', 'user@example.com') if data else 'user@example.com'
            given_steps.append(f"- {user_type} is logged in with account {email}")
        elif user_type == 'Visitor':
            given_steps.append(f"- User is a visitor (not logged in)")
        else:
            given_steps.append(f"- User has role: {user_type}")

        # Device and browser
        device = params.get('Device', 'Desktop')
        browser = params.get('Browser', 'Chrome')
        given_steps.append(f"- Using {browser} browser on {device} device")

        # Network conditions
        network = params.get('Network_Speed', 'High')
        given_steps.append(f"- Network speed: {network}")

        # Data state (if applicable)
        data_state = params.get('Data_State', 'N/A')
        if data_state != 'N/A':
            given_steps.append(f"- Data state: {data_state}")

        # Scenario-specific preconditions
        given_steps.extend(self._get_scenario_specific_givens(scenario, variant, data))

        return '\n'.join(given_steps)

    def _build_when_section(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> str:
        """Build WHEN section based on variant and test data"""
        when_steps = ["WHEN:"]

        # Get scenario-specific actions
        when_steps.extend(self._get_scenario_specific_whens(scenario, variant, data))

        return '\n'.join(when_steps)

    def _build_then_section(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> str:
        """Build THEN section based on expected outcomes"""
        then_steps = ["THEN:"]

        # Get scenario-specific assertions
        then_steps.extend(self._get_scenario_specific_thens(scenario, variant, data))

        return '\n'.join(then_steps)

    def _build_expected_result(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> str:
        """Build expected result section"""
        results = ["EXPECTED RESULT:"]

        # Get scenario-specific expected results
        results.extend(self._get_scenario_specific_results(scenario, variant, data))

        return '\n'.join(results)

    def _get_scenario_specific_givens(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> List[str]:
        """Get scenario-specific GIVEN conditions"""
        givens = []
        title_lower = scenario.title.lower()

        if 'registration' in title_lower or 'register' in title_lower:
            givens.append("- User is on the registration page")
            givens.append("- Registration system is active and accepting new users")

        elif 'login' in title_lower:
            givens.append("- User is on the login page")
            if data and 'Email' in data.data_fields:
                email = data.data_fields['Email']
                givens.append(f"- User account exists for {email}")

        elif 'checkout' in title_lower or 'payment' in title_lower:
            givens.append("- User is on the checkout page")
            cart_state = variant.parameters.get('Cart_State', 'Items in cart')
            givens.append(f"- Shopping cart state: {cart_state}")

        elif 'search' in title_lower:
            givens.append("- User is on the product search page")

        elif 'cart' in title_lower:
            givens.append("- User has access to shopping cart")

        elif 'product' in title_lower and 'view' in title_lower:
            givens.append("- User is viewing a product page")

        elif 'admin' in title_lower:
            givens.append("- User is on the admin dashboard")

        return givens

    def _get_scenario_specific_whens(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> List[str]:
        """Get scenario-specific WHEN actions"""
        whens = []
        title_lower = scenario.title.lower()
        params = variant.parameters

        if 'registration' in title_lower or 'register' in title_lower:
            if data:
                whens.append(f"- User enters first name: {data.data_fields.get('FirstName', 'John')}")
                whens.append(f"- User enters last name: {data.data_fields.get('LastName', 'Doe')}")
                whens.append(f"- User enters email: {data.data_fields.get('Email', 'john.doe@example.com')}")
                whens.append(f"- User enters phone: {data.data_fields.get('Phone', '555-0123')}")
                whens.append(f"- User enters password: {data.data_fields.get('Password', 'SecurePass123!')}")
                whens.append(f"- User confirms password: {data.data_fields.get('ConfirmPassword', 'SecurePass123!')}")

            field_validity = params.get('Field_Values', 'Valid')
            if 'Invalid' in field_validity or 'Missing' in field_validity:
                whens.append(f"- Data validation issue: {field_validity}")

            whens.append("- User clicks 'Register' button")

        elif 'login' in title_lower:
            if data:
                whens.append(f"- User enters email: {data.data_fields.get('Email', 'user@example.com')}")
                whens.append(f"- User enters password: {data.data_fields.get('Password', 'password123')}")
            whens.append("- User clicks 'Login' button")

        elif 'checkout' in title_lower or 'payment' in title_lower:
            payment_method = params.get('Payment_Method', 'Credit_Card')
            whens.append(f"- User selects payment method: {payment_method}")

            if data and payment_method == 'Credit_Card':
                whens.append(f"- User enters card number: {data.data_fields.get('CardNumber', '4111-1111-1111-1111')}")
                whens.append(f"- User enters cardholder name: {data.data_fields.get('CardholderName', 'John Doe')}")
                whens.append(f"- User enters expiry: {data.data_fields.get('CardExpiry', '12/25')}")
                whens.append(f"- User enters CVV: {data.data_fields.get('CardCVV', '123')}")

            whens.append("- User confirms shipping address")
            whens.append("- User clicks 'Place Order' button")

        elif 'search' in title_lower:
            if data:
                search_term = data.data_fields.get('SearchTerm', 'product')
                whens.append(f"- User enters search term: '{search_term}'")
            whens.append("- User clicks 'Search' button")

        elif 'add to cart' in title_lower or 'cart' in title_lower:
            if data:
                quantity = data.data_fields.get('Quantity', '1')
                whens.append(f"- User selects quantity: {quantity}")
            whens.append("- User clicks 'Add to Cart' button")

        else:
            # Generic action
            whens.append(f"- User performs the action described in scenario: {scenario.title}")

        return whens

    def _get_scenario_specific_thens(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> List[str]:
        """Get scenario-specific THEN assertions"""
        thens = []
        title_lower = scenario.title.lower()
        params = variant.parameters
        input_validity = params.get('Input_Validity', 'Valid')

        if 'registration' in title_lower or 'register' in title_lower:
            if input_validity == 'Valid':
                thens.append("- System creates new user account")
                thens.append("- Verification email is sent to user's email address")
                thens.append("- Success message is displayed: 'Registration successful. Please check your email to verify your account.'")
                thens.append("- User is redirected to login page or verification page")
            else:
                field_values = params.get('Field_Values', '')
                thens.append(f"- System displays validation error for: {field_values}")
                thens.append("- User account is NOT created")
                thens.append("- User remains on registration page")

        elif 'login' in title_lower:
            if input_validity == 'Valid':
                user_type = params.get('User_Type', 'Buyer')
                thens.append("- User is successfully authenticated")
                thens.append(f"- User is redirected to {user_type} dashboard/home page")
                thens.append("- User session is established")
                thens.append("- User name is displayed in header")
            else:
                thens.append("- System displays error: 'Invalid email or password'")
                thens.append("- User is NOT authenticated")
                thens.append("- User remains on login page")

        elif 'checkout' in title_lower or 'payment' in title_lower:
            if input_validity == 'Valid':
                thens.append("- Payment is processed successfully")
                thens.append("- Order is created in the system")
                thens.append("- Order confirmation page is displayed")
                thens.append("- Confirmation email is sent to user")
                thens.append("- Shopping cart is cleared")
            else:
                thens.append("- System displays payment error message")
                thens.append("- Order is NOT created")
                thens.append("- User remains on checkout page")

        elif 'search' in title_lower:
            thens.append("- Search results are displayed")
            thens.append("- Results are relevant to search term")
            thens.append("- Product count is shown")

        elif 'add to cart' in title_lower or 'cart' in title_lower:
            thens.append("- Item is added to shopping cart")
            thens.append("- Cart quantity badge is updated")
            thens.append("- Success message is displayed: 'Item added to cart'")

        else:
            # Generic assertion
            if input_validity == 'Valid':
                thens.append("- Action is completed successfully")
                thens.append("- System displays success confirmation")
            else:
                thens.append("- System displays appropriate error message")
                thens.append("- Action is NOT completed")

        return thens

    def _get_scenario_specific_results(self, scenario: TestScenario, variant: Variant, data: Optional[TestData]) -> List[str]:
        """Get scenario-specific expected results"""
        results = []
        title_lower = scenario.title.lower()
        params = variant.parameters
        input_validity = params.get('Input_Validity', 'Valid')

        if 'registration' in title_lower or 'register' in title_lower:
            if input_validity == 'Valid':
                if data:
                    email = data.data_fields.get('Email', 'user@example.com')
                    results.append(f"- Database contains new user record for {email}")
                    results.append(f"- Verification email sent to {email}")
                results.append("- User account status = 'Unverified' or 'Pending Verification'")
            else:
                results.append("- No database changes")
                results.append("- No email sent")

        elif 'login' in title_lower:
            if input_validity == 'Valid':
                results.append("- User session cookie/token is created")
                results.append("- Last login timestamp is updated in database")
            else:
                results.append("- No session created")
                results.append("- Failed login attempt logged")

        elif 'checkout' in title_lower or 'payment' in title_lower:
            if input_validity == 'Valid':
                results.append("- Order record created in database with status 'Pending' or 'Processing'")
                results.append("- Payment transaction recorded")
                results.append("- Inventory updated")
                if data:
                    email = data.data_fields.get('Email', 'user@example.com')
                    results.append(f"- Confirmation email sent to {email}")
            else:
                results.append("- No order created")
                results.append("- No payment processed")
                results.append("- Inventory unchanged")

        else:
            # Generic result
            if input_validity == 'Valid':
                results.append("- System state updated correctly")
                results.append("- All business rules satisfied")
            else:
                results.append("- System state unchanged")
                results.append("- Error logged appropriately")

        # Add browser/device verification
        browser = params.get('Browser', 'Chrome')
        device = params.get('Device', 'Desktop')
        results.append(f"- Verified on {browser}/{device}")

        return results

    def _format_parameters(self, parameters: Dict[str, str]) -> str:
        """Format parameters for display"""
        lines = []
        for key, value in sorted(parameters.items()):
            lines.append(f"  {key}: {value}")
        return '\n'.join(lines) if lines else '  N/A'

    def _format_test_data(self, data: Optional[TestData]) -> str:
        """Format test data for display"""
        if not data:
            return '  N/A'

        lines = []
        for key, value in sorted(data.data_fields.items()):
            # Truncate long values
            display_value = value if len(value) <= 50 else value[:47] + '...'
            lines.append(f"  {key}: {display_value}")
        return '\n'.join(lines)

    def generate_all_scripts(self, output_dir: str):
        """Generate test scripts for all variants"""
        self.logger.info(f"Generating test scripts to {output_dir}")
        self.start_time = time.time()

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        total_variants = len(self.variants)
        self.logger.info(f"Total variants to process: {total_variants}")

        # Progress tracking
        progress_interval = max(100, total_variants // 20)  # Report every 5%

        for idx, (variant_id, variant) in enumerate(self.variants.items(), 1):
            # Generate script content
            script_content = self.generate_script_content(variant)

            # Write to file: TS-XXX_VXXX.txt
            filename = f"{variant.scenario_id}_{variant_id}.txt"
            filepath = output_path / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(script_content)

            self.scripts_generated += 1

            # Progress reporting
            if idx % progress_interval == 0 or idx == total_variants:
                elapsed = time.time() - self.start_time
                rate = idx / elapsed if elapsed > 0 else 0
                eta = (total_variants - idx) / rate if rate > 0 else 0
                percentage = (idx / total_variants) * 100

                self.logger.info(
                    f"[{percentage:.1f}%] Generated {idx}/{total_variants} scripts "
                    f"({rate:.0f} scripts/sec, ETA: {eta:.0f}s)"
                )

        elapsed = time.time() - self.start_time
        self.logger.info(
            f"✓ Generated {self.scripts_generated} test scripts in {elapsed:.1f} seconds "
            f"({self.scripts_generated/elapsed:.0f} scripts/sec)"
        )

    def generate_summary_report(self, output_dir: str):
        """Generate summary report of generated scripts"""
        summary_file = Path(output_dir) / "00_GENERATION_SUMMARY.txt"

        # Group variants by scenario
        by_scenario = {}
        for variant in self.variants.values():
            if variant.scenario_id not in by_scenario:
                by_scenario[variant.scenario_id] = []
            by_scenario[variant.scenario_id].append(variant.variant_id)

        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("TEST SCRIPT GENERATION SUMMARY\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Scripts: {self.scripts_generated}\n")
            f.write(f"Total Scenarios: {len(by_scenario)}\n")
            f.write(f"Generation Time: {time.time() - self.start_time:.1f} seconds\n\n")

            f.write("SCRIPTS BY SCENARIO:\n")
            f.write("-" * 80 + "\n")

            for scenario_id in sorted(by_scenario.keys()):
                variant_count = len(by_scenario[scenario_id])
                scenario = self.scenarios.get(scenario_id)
                title = scenario.title if scenario else "Unknown"

                f.write(f"\n{scenario_id}: {title}\n")
                f.write(f"  Variants: {variant_count}\n")
                f.write(f"  Files: {scenario_id}_V*.txt\n")

        self.logger.info(f"✓ Generated summary report: {summary_file}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate test scripts from variants and test data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with default deliverables directory
  python3 generate_test_scripts_from_variants.py \\
      deliverables/03_test_scenarios.md \\
      deliverables/04_variants.csv \\
      deliverables/05_test_data.csv \\
      -o deliverables/06_test_scripts

  # With custom output directory
  python3 generate_test_scripts_from_variants.py \\
      custom_dir/03_test_scenarios.md \\
      custom_dir/04_variants.csv \\
      custom_dir/05_test_data.csv \\
      -o custom_dir/06_test_scripts --verbose

  # Using OUTPUT_DIR variable (set in skill workflow)
  python3 generate_test_scripts_from_variants.py \\
      $OUTPUT_DIR/03_test_scenarios.md \\
      $OUTPUT_DIR/04_variants.csv \\
      $OUTPUT_DIR/05_test_data.csv \\
      -o $OUTPUT_DIR/06_test_scripts
        """
    )

    parser.add_argument(
        'scenarios_file',
        help='Path to test scenarios markdown file (03_test_scenarios.md)'
    )
    parser.add_argument(
        'variants_file',
        help='Path to variants CSV file (04_variants.csv)'
    )
    parser.add_argument(
        'test_data_file',
        help='Path to test data CSV file (05_test_data.csv)'
    )
    parser.add_argument(
        '-o', '--output',
        default='06_test_scripts',
        help='Output directory for test scripts (default: 06_test_scripts)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Validate input files exist
    for file_path in [args.scenarios_file, args.variants_file, args.test_data_file]:
        if not Path(file_path).exists():
            print(f"ERROR: File not found: {file_path}", file=sys.stderr)
            return 1

    # Create generator
    generator = TestScriptGenerator(verbose=args.verbose)

    try:
        # Load inputs
        generator.load_scenarios(args.scenarios_file)
        generator.load_variants(args.variants_file)
        generator.load_test_data(args.test_data_file)

        # Generate scripts
        generator.generate_all_scripts(args.output)

        # Generate summary
        generator.generate_summary_report(args.output)

        print(f"\n✓ SUCCESS: Generated {generator.scripts_generated} test scripts")
        print(f"  Output directory: {args.output}")

        return 0

    except Exception as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
