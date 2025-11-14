#!/usr/bin/env python3
"""
Requirements Traceability Matrix (RTM) Builder

This script builds a comprehensive Requirements Traceability Matrix by mapping
requirements from specification documents to test scenarios and scripts.

Production Features:
- Comprehensive input validation
- Rich RTM output with metadata
- Automatic requirement metadata extraction
- Coverage statistics and gap analysis
- Test script availability checking
- Multiple requirement format support
- Detailed logging and reporting
- Configurable output options

Author: QA Automation Skill
Version: 2.0.0
"""

import csv
import sys
import re
import os
import argparse
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict
from datetime import datetime


@dataclass
class Requirement:
    """Represents a requirement with metadata"""
    req_id: str
    description: str = "N/A"
    priority: str = "N/A"
    source_file: str = ""
    scenarios: List[str] = field(default_factory=list)


@dataclass
class TestScenario:
    """Represents a test scenario"""
    scenario_id: str
    title: str = "N/A"
    priority: str = "N/A"
    requirements: List[str] = field(default_factory=list)
    has_script: bool = False


@dataclass
class RTMStats:
    """Statistics about RTM coverage"""
    total_requirements: int = 0
    covered_requirements: int = 0
    uncovered_requirements: int = 0
    total_scenarios: int = 0
    orphaned_scenarios: int = 0
    scenarios_with_scripts: int = 0
    scenarios_without_scripts: int = 0
    coverage_percentage: float = 0.0


class RTMBuilder:
    """
    Production-ready Requirements Traceability Matrix builder.

    Extracts requirements and test scenarios from documents, maps them together,
    and generates a comprehensive traceability matrix with coverage analysis.
    """

    def __init__(self, verbose: bool = False):
        """
        Initialize the RTM builder.

        Args:
            verbose: Enable detailed logging
        """
        self.verbose = verbose
        self._setup_logging()

        # Regex patterns
        # Only match REQ-XXX format since that's what the extraction step produces
        # (Original BRD uses FR/NFR, but 00_requirements.md normalizes to REQ-XXX)
        self.req_pattern = re.compile(
            r'\b(REQ[-_]?\d+)\b',
            re.IGNORECASE
        )
        self.scenario_pattern = re.compile(
            r'\b(TS[-_]?\d+)\b',
            re.IGNORECASE
        )

        # Data storage
        self.requirements: Dict[str, Requirement] = {}
        self.scenarios: Dict[str, TestScenario] = {}

    def _setup_logging(self):
        """Configure logging with appropriate level"""
        level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)

    def validate_file(self, file_path: str, file_type: str = "input") -> bool:
        """
        Validate that a file exists and is readable.

        Args:
            file_path: Path to the file
            file_type: Description of file type for error messages

        Returns:
            True if valid

        Raises:
            FileNotFoundError: If file doesn't exist
            PermissionError: If file isn't readable
            ValueError: If path is not a file
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_type} file not found: {file_path}")

        if not path.is_file():
            raise ValueError(f"{file_type} path is not a file: {file_path}")

        if not os.access(path, os.R_OK):
            raise PermissionError(f"Cannot read {file_type} file: {file_path}")

        self.logger.debug(f"✓ Validated {file_type}: {file_path}")
        return True

    def extract_requirements(self, requirement_files: List[str]):
        """
        Extract requirements from requirement documents.

        Args:
            requirement_files: List of requirement file paths
        """
        self.logger.info(f"Extracting requirements from {len(requirement_files)} file(s)")

        for req_file in requirement_files:
            try:
                self.validate_file(req_file, "requirement")

                with open(req_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                    # Find all requirement IDs
                    found_ids = self.req_pattern.findall(content)

                    if not found_ids:
                        self.logger.warning(f"No requirement IDs found in {req_file}")
                        continue

                    # Try to extract metadata for each requirement
                    for req_id in found_ids:
                        req_id_normalized = req_id.upper().replace('_', '-')

                        if req_id_normalized not in self.requirements:
                            # Extract description and priority if available
                            description, priority = self._extract_req_metadata(
                                content, req_id
                            )

                            self.requirements[req_id_normalized] = Requirement(
                                req_id=req_id_normalized,
                                description=description,
                                priority=priority,
                                source_file=os.path.basename(req_file)
                            )

                    unique_count = len(set(r.upper().replace('_', '-') for r in found_ids))
                    self.logger.info(
                        f"  Found {unique_count} unique requirement(s) in {os.path.basename(req_file)}"
                    )

            except FileNotFoundError:
                self.logger.warning(f"Requirement file not found: {req_file}, skipping")
            except Exception as e:
                self.logger.error(f"Error processing {req_file}: {e}")
                if self.verbose:
                    import traceback
                    traceback.print_exc()

        self.logger.info(f"✓ Extracted {len(self.requirements)} total requirement(s)")

    def _extract_req_metadata(
        self,
        content: str,
        req_id: str
    ) -> Tuple[str, str]:
        """
        Extract requirement description and priority from content.

        Args:
            content: File content
            req_id: Requirement ID to search for

        Returns:
            Tuple of (description, priority)
        """
        description = "N/A"
        priority = "N/A"

        # Try to find the requirement in a table or structured format
        # Look for patterns like: FR-001 | Description | Priority
        # or FR-001: Description (Priority: High)
        # or - **REQ-001**: Description (markdown bold format)

        # Pattern 0: Markdown list with bold - matches: - **REQ-001**: Description
        markdown_bold_pattern = re.compile(
            rf'-\s*\*\*{re.escape(req_id)}\*\*\s*:\s*([^\n]+)',
            re.IGNORECASE
        )
        match = markdown_bold_pattern.search(content)
        if match:
            line = match.group(1).strip()
            # Check if priority is mentioned
            priority_match = re.search(
                r'\(?\s*(?:Priority|P):\s*(\w+(?:\s*\(\d+\))?)\)?',
                line,
                re.IGNORECASE
            )
            if priority_match:
                priority = priority_match.group(1).strip()
                # Remove priority from description
                description = re.sub(
                    r'\(?\s*(?:Priority|P):\s*\w+(?:\s*\(\d+\))?\)?',
                    '',
                    line
                ).strip()
            else:
                description = line

            return description, priority

        # Pattern 1: Table format with pipes
        table_pattern = re.compile(
            rf'{re.escape(req_id)}\s*[|,]\s*([^|,\n]+)\s*[|,]\s*([^|,\n]+)',
            re.IGNORECASE
        )
        match = table_pattern.search(content)
        if match:
            description = match.group(1).strip()
            priority = match.group(2).strip()
            return description, priority

        # Pattern 2: Line format with colon (without bold)
        line_pattern = re.compile(
            rf'{re.escape(req_id)}\s*:\s*([^\n]+)',
            re.IGNORECASE
        )
        match = line_pattern.search(content)
        if match:
            line = match.group(1).strip()
            # Check if priority is mentioned
            priority_match = re.search(
                r'\(?\s*(?:Priority|P):\s*(\w+(?:\s*\(\d+\))?)\)?',
                line,
                re.IGNORECASE
            )
            if priority_match:
                priority = priority_match.group(1).strip()
                # Remove priority from description
                description = re.sub(
                    r'\(?\s*(?:Priority|P):\s*\w+(?:\s*\(\d+\))?\)?',
                    '',
                    line
                ).strip()
            else:
                description = line

            return description, priority

        # Pattern 3: Markdown header
        header_pattern = re.compile(
            rf'###+\s*{re.escape(req_id)}\s*[:-]\s*([^\n]+)',
            re.IGNORECASE
        )
        match = header_pattern.search(content)
        if match:
            description = match.group(1).strip()
            return description, priority

        return description, priority

    def extract_scenarios(
        self,
        scenarios_file: str,
        test_scripts_dir: Optional[str] = None
    ):
        """
        Extract test scenarios from scenarios file.

        Args:
            scenarios_file: Path to test scenarios file
            test_scripts_dir: Optional directory containing test scripts
        """
        self.logger.info(f"Extracting test scenarios from {scenarios_file}")

        try:
            self.validate_file(scenarios_file, "scenarios")

            with open(scenarios_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Split content by scenario IDs
            parts = self.scenario_pattern.split(content)

            # Process in pairs (scenario_id, scenario_content)
            for i in range(1, len(parts), 2):
                if i + 1 < len(parts):
                    scenario_id = parts[i].upper().replace('_', '-')
                    scenario_content = parts[i + 1]

                    # Extract title, priority, and related requirements
                    title, priority, requirements = self._extract_scenario_metadata(
                        scenario_content
                    )

                    # Debug output for first few scenarios
                    if i < 20 and self.verbose:
                        self.logger.debug(f"Scenario {scenario_id}: {len(requirements)} reqs: {requirements}")

                    # Check if test script exists
                    has_script = False
                    if test_scripts_dir:
                        script_path = Path(test_scripts_dir) / f"{scenario_id}.txt"
                        has_script = script_path.exists()

                    # Only store if this scenario hasn't been stored yet (avoid duplicates)
                    # OR if this one has requirements and the previous one didn't
                    if scenario_id not in self.scenarios or (requirements and not self.scenarios[scenario_id].requirements):
                        self.scenarios[scenario_id] = TestScenario(
                            scenario_id=scenario_id,
                            title=title,
                            priority=priority,
                            requirements=requirements,
                            has_script=has_script
                        )

            self.logger.info(f"✓ Extracted {len(self.scenarios)} test scenario(s)")

        except Exception as e:
            self.logger.error(f"Error processing scenarios file: {e}")
            raise

    def _extract_scenario_metadata(
        self,
        content: str
    ) -> Tuple[str, str, List[str]]:
        """
        Extract scenario title, priority, and related requirements.

        Args:
            content: Scenario content

        Returns:
            Tuple of (title, priority, requirements_list)
        """
        title = "N/A"
        priority = "N/A"
        requirements = []

        # Extract title (usually first line or after ###)
        title_match = re.search(r'###\s*([^\n]+)', content)
        if title_match:
            title = title_match.group(1).strip()
            # Remove scenario ID if it's in the title
            title = self.scenario_pattern.sub('', title).strip(':- ').strip()

        # Extract priority
        priority_match = re.search(
            r'\*\*Priority\*\*:\s*(\w+)',
            content,
            re.IGNORECASE
        )
        if priority_match:
            priority = priority_match.group(1).strip()

        # Extract related requirements (with or without bold markers)
        req_match = re.search(
            r'\*\*Related Requirements\*\*:\s*([^\n]+)',
            content,
            re.IGNORECASE
        )
        if not req_match:
            # Try without bold markers for backward compatibility
            req_match = re.search(
                r'Related Requirements:\s*([^\n]+)',
                content,
                re.IGNORECASE
            )
        if req_match:
            req_line = req_match.group(1)
            found_reqs = self.req_pattern.findall(req_line)
            requirements = [r.upper().replace('_', '-') for r in found_reqs]

        return title, priority, requirements

    def build_rtm(self):
        """
        Build the requirements traceability matrix by mapping requirements to scenarios.
        """
        self.logger.info("Building requirements traceability matrix")

        # Map scenarios to requirements
        mapped_count = 0
        for scenario_id, scenario in self.scenarios.items():
            if self.verbose and scenario_id in ['TS-001', 'TS-002', 'TS-003']:
                self.logger.debug(f"Mapping {scenario_id} with {len(scenario.requirements)} requirements: {scenario.requirements}")
            for req_id in scenario.requirements:
                if req_id in self.requirements:
                    if scenario_id not in self.requirements[req_id].scenarios:
                        self.requirements[req_id].scenarios.append(scenario_id)
                        mapped_count += 1
                        if self.verbose and req_id in ['REQ-001', 'REQ-002']:
                            self.logger.debug(f"Mapped {req_id} -> {scenario_id}")
                else:
                    # Requirement mentioned in scenario but not in requirement files
                    self.logger.warning(
                        f"Scenario {scenario_id} references unknown requirement {req_id}"
                    )
                    # Create placeholder requirement
                    self.requirements[req_id] = Requirement(
                        req_id=req_id,
                        description="Referenced in scenario but not found in requirement files",
                        priority="Unknown"
                    )
                    self.requirements[req_id].scenarios.append(scenario_id)

        self.logger.info("✓ RTM mapping complete")

    def calculate_statistics(self) -> RTMStats:
        """
        Calculate RTM coverage statistics.

        Returns:
            RTMStats object with coverage information
        """
        stats = RTMStats()

        stats.total_requirements = len(self.requirements)
        stats.covered_requirements = sum(
            1 for req in self.requirements.values() if req.scenarios
        )
        stats.uncovered_requirements = stats.total_requirements - stats.covered_requirements

        stats.total_scenarios = len(self.scenarios)
        stats.orphaned_scenarios = sum(
            1 for scenario in self.scenarios.values() if not scenario.requirements
        )

        stats.scenarios_with_scripts = sum(
            1 for scenario in self.scenarios.values() if scenario.has_script
        )
        stats.scenarios_without_scripts = stats.total_scenarios - stats.scenarios_with_scripts

        if stats.total_requirements > 0:
            stats.coverage_percentage = (
                stats.covered_requirements / stats.total_requirements * 100
            )

        return stats

    def write_rtm(
        self,
        output_file: str,
        include_summary: bool = True
    ):
        """
        Write RTM to CSV file.

        Args:
            output_file: Output CSV file path
            include_summary: Whether to print summary to console
        """
        self.logger.info(f"Writing RTM to {output_file}")

        # Ensure output directory exists
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)

                # Write header
                writer.writerow([
                    "Requirement_ID",
                    "Requirement_Description",
                    "Priority",
                    "Test_Scenario_IDs",
                    "Test_Script_Available",
                    "Coverage_Status",
                    "Notes"
                ])

                # Write requirements (sorted by ID)
                if not self.requirements:
                    writer.writerow([
                        "No requirements found",
                        "N/A", "N/A", "N/A", "N/A", "Not Covered", ""
                    ])
                else:
                    for req_id in sorted(self.requirements.keys()):
                        req = self.requirements[req_id]

                        # Get linked scenarios
                        scenario_ids = ", ".join(sorted(req.scenarios)) if req.scenarios else "N/A"

                        # Check coverage status
                        if not req.scenarios:
                            coverage_status = "Not Covered"
                            test_script_available = "N/A"
                            notes = "No test scenarios mapped to this requirement"
                        else:
                            coverage_status = "Covered"
                            # Check if all scenarios have scripts
                            scenarios_with_scripts = [
                                sid for sid in req.scenarios
                                if sid in self.scenarios and self.scenarios[sid].has_script
                            ]
                            if len(scenarios_with_scripts) == len(req.scenarios):
                                test_script_available = "Yes"
                                notes = ""
                            elif scenarios_with_scripts:
                                test_script_available = "Partial"
                                notes = f"Scripts available for: {', '.join(scenarios_with_scripts)}"
                            else:
                                test_script_available = "No"
                                notes = "Test scenarios defined but scripts not created"

                        writer.writerow([
                            req_id,
                            req.description,
                            req.priority,
                            scenario_ids,
                            test_script_available,
                            coverage_status,
                            notes
                        ])

            self.logger.info(f"✓ RTM written to {output_file}")

            # Print summary
            if include_summary:
                stats = self.calculate_statistics()
                self._print_summary(stats)

        except IOError as e:
            raise IOError(f"Failed to write RTM file: {e}")

    def _print_summary(self, stats: RTMStats):
        """Print RTM summary statistics"""
        print(f"\n{'='*60}")
        print("RTM GENERATION SUMMARY")
        print(f"{'='*60}")
        print(f"\n📋 Requirements:")
        print(f"  Total Requirements: {stats.total_requirements}")
        print(f"  Covered: {stats.covered_requirements} ({stats.coverage_percentage:.1f}%)")
        print(f"  Uncovered: {stats.uncovered_requirements}")

        print(f"\n🧪 Test Scenarios:")
        print(f"  Total Scenarios: {stats.total_scenarios}")
        print(f"  Orphaned (no requirements): {stats.orphaned_scenarios}")
        print(f"  With Test Scripts: {stats.scenarios_with_scripts}")
        print(f"  Without Test Scripts: {stats.scenarios_without_scripts}")

        # Warnings
        if stats.uncovered_requirements > 0:
            print(f"\n⚠️  Warning: {stats.uncovered_requirements} requirement(s) not covered by test scenarios")

        if stats.orphaned_scenarios > 0:
            print(f"⚠️  Warning: {stats.orphaned_scenarios} scenario(s) not linked to any requirement")

        if stats.scenarios_without_scripts > 0:
            print(f"ℹ️  Info: {stats.scenarios_without_scripts} scenario(s) missing test scripts")

        if stats.coverage_percentage == 100 and stats.orphaned_scenarios == 0:
            print("\n✅ Perfect traceability! All requirements covered and all scenarios linked.")

        print(f"\n{'='*60}\n")

    def generate_gap_report(self, output_file: str):
        """
        Generate a detailed gap analysis report.

        Args:
            output_file: Path for gap report markdown file
        """
        self.logger.info("Generating gap analysis report")

        stats = self.calculate_statistics()

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# RTM Gap Analysis Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Summary
            f.write("## Summary\n\n")
            f.write(f"- **Total Requirements:** {stats.total_requirements}\n")
            f.write(f"- **Coverage:** {stats.coverage_percentage:.1f}%\n")
            f.write(f"- **Uncovered Requirements:** {stats.uncovered_requirements}\n")
            f.write(f"- **Orphaned Scenarios:** {stats.orphaned_scenarios}\n\n")

            # Uncovered requirements
            if stats.uncovered_requirements > 0:
                f.write("## ⚠️ Uncovered Requirements\n\n")
                f.write("The following requirements have no test scenarios:\n\n")
                f.write("| Requirement ID | Description | Priority |\n")
                f.write("|----------------|-------------|----------|\n")
                for req_id, req in sorted(self.requirements.items()):
                    if not req.scenarios:
                        f.write(f"| {req_id} | {req.description} | {req.priority} |\n")
                f.write("\n")

            # Orphaned scenarios
            if stats.orphaned_scenarios > 0:
                f.write("## ⚠️ Orphaned Test Scenarios\n\n")
                f.write("The following scenarios are not linked to any requirement:\n\n")
                f.write("| Scenario ID | Title | Priority |\n")
                f.write("|-------------|-------|----------|\n")
                for scenario_id, scenario in sorted(self.scenarios.items()):
                    if not scenario.requirements:
                        f.write(f"| {scenario_id} | {scenario.title} | {scenario.priority} |\n")
                f.write("\n")

            # Missing test scripts
            if stats.scenarios_without_scripts > 0:
                f.write("## ℹ️ Scenarios Without Test Scripts\n\n")
                f.write("| Scenario ID | Title | Requirements |\n")
                f.write("|-------------|-------|-------------|\n")
                for scenario_id, scenario in sorted(self.scenarios.items()):
                    if not scenario.has_script:
                        reqs = ", ".join(scenario.requirements) if scenario.requirements else "None"
                        f.write(f"| {scenario_id} | {scenario.title} | {reqs} |\n")
                f.write("\n")

        self.logger.info(f"✓ Gap report written to {output_file}")

    def process(
        self,
        scenarios_file: str,
        requirement_files: List[str],
        output_file: str,
        test_scripts_dir: Optional[str] = None,
        generate_gap_report: bool = False
    ):
        """
        Main processing function to build RTM.

        Args:
            scenarios_file: Path to test scenarios file
            requirement_files: List of requirement file paths
            output_file: Output RTM CSV file path
            test_scripts_dir: Optional test scripts directory
            generate_gap_report: Whether to generate gap analysis report
        """
        self.logger.info("Starting RTM generation")
        self.logger.info(f"Scenarios file: {scenarios_file}")
        self.logger.info(f"Requirement files: {len(requirement_files)} file(s)")
        self.logger.info(f"Output: {output_file}")

        try:
            # Extract data
            self.extract_requirements(requirement_files)
            self.extract_scenarios(scenarios_file, test_scripts_dir)

            # Build mapping
            self.build_rtm()

            # Write RTM
            self.write_rtm(output_file, include_summary=True)

            # Generate gap report if requested
            if generate_gap_report:
                gap_report_path = output_file.replace('.csv', '_gap_report.md')
                self.generate_gap_report(gap_report_path)

            self.logger.info("✓ RTM generation completed successfully")

        except Exception as e:
            self.logger.error(f"✗ RTM generation failed: {e}")
            raise


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description='Build Requirements Traceability Matrix (RTM) from requirements and test scenarios',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python rtm_builder.py deliverables/03_test_scenarios.md requirements.md

  # Multiple requirement files
  python rtm_builder.py deliverables/03_test_scenarios.md req1.md req2.md req3.md

  # With test scripts directory for availability check
  python rtm_builder.py deliverables/03_test_scenarios.md requirements.md \\
      --test-scripts deliverables/06_test_scripts

  # Custom output path
  python rtm_builder.py deliverables/03_test_scenarios.md requirements.md \\
      --output custom_rtm.csv

  # Generate gap analysis report
  python rtm_builder.py deliverables/03_test_scenarios.md requirements.md \\
      --gap-report

  # Verbose logging
  python rtm_builder.py deliverables/03_test_scenarios.md requirements.md --verbose
        """
    )

    parser.add_argument(
        'scenarios_file',
        help='Path to test scenarios file (e.g., deliverables/03_test_scenarios.md)'
    )

    parser.add_argument(
        'requirement_files',
        nargs='+',
        help='One or more requirement files (e.g., BRD.md requirements.md)'
    )

    parser.add_argument(
        '--output', '-o',
        default='deliverables/09_rtm.csv',
        help='Output RTM CSV file path (default: deliverables/09_rtm.csv)'
    )

    parser.add_argument(
        '--test-scripts', '-t',
        help='Directory containing test scripts (for availability check)'
    )

    parser.add_argument(
        '--gap-report', '-g',
        action='store_true',
        help='Generate gap analysis report'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 2.0.0'
    )

    args = parser.parse_args()

    try:
        builder = RTMBuilder(verbose=args.verbose)
        builder.process(
            scenarios_file=args.scenarios_file,
            requirement_files=args.requirement_files,
            output_file=args.output,
            test_scripts_dir=args.test_scripts,
            generate_gap_report=args.gap_report
        )
        sys.exit(0)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
