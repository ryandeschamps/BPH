#!/usr/bin/env python3
"""
Summary Aggregator - Aggregate metrics across all test scenarios.

VERSION 1.0.0

This script collects metrics from individual scenario directories and generates
comprehensive summary reports and analytics.

Features:
- Aggregate variant counts across all scenarios
- Generate cross-scenario coverage matrix
- Create metrics dashboard
- Generate scenario index for navigation
- Optional: Combine all variants into one CSV for legacy compatibility

Usage:
    # Generate all summary reports
    python3 summary_aggregator.py --scenarios-dir deliverables/scenarios

    # Generate specific reports
    python3 summary_aggregator.py --scenarios-dir deliverables/scenarios \\
        --reports metrics,coverage

    # Include combined variants CSV
    python3 summary_aggregator.py --scenarios-dir deliverables/scenarios \\
        --combine-variants
"""

import argparse
import json
import csv
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
import re


@dataclass
class ScenarioSummary:
    """Summary metrics for a scenario"""
    scenario_id: str
    scenario_title: str
    scenario_dir: Path
    variant_count: int = 0
    test_data_count: int = 0
    script_count: int = 0
    optimized_count: int = 0
    coverage_pct: float = 0.0
    parameters: Dict[str, int] = field(default_factory=dict)
    status: str = "unknown"


class SummaryAggregator:
    """
    Aggregates metrics from scenario directories.
    """

    def __init__(self, scenarios_dir: Path, verbose: bool = False):
        """
        Initialize aggregator.

        Args:
            scenarios_dir: Base directory containing scenario folders
            verbose: Enable verbose output
        """
        self.scenarios_dir = Path(scenarios_dir)
        self.verbose = verbose
        self.scenarios: List[ScenarioSummary] = []

    def log(self, message: str, level: str = "INFO"):
        """Log a message"""
        if self.verbose or level in ["WARN", "ERROR"]:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {level}: {message}")

    def discover_scenarios(self) -> List[Path]:
        """
        Discover all scenario directories.

        Returns:
            List of scenario directory paths
        """
        if not self.scenarios_dir.exists():
            raise FileNotFoundError(f"Scenarios directory not found: {self.scenarios_dir}")

        # Find all TS-XXX_* directories
        scenario_dirs = sorted(self.scenarios_dir.glob('TS-*'))

        self.log(f"Found {len(scenario_dirs)} scenario directories")
        return scenario_dirs

    def load_scenario_metrics(self, scenario_dir: Path) -> Optional[ScenarioSummary]:
        """
        Load metrics from a scenario directory.

        Args:
            scenario_dir: Path to scenario directory

        Returns:
            ScenarioSummary or None if metrics not found
        """
        # Extract scenario ID from directory name
        dir_name = scenario_dir.name
        match = re.match(r'(TS-\d+)_(.+)', dir_name)
        if not match:
            self.log(f"Invalid scenario directory name: {dir_name}", "WARN")
            return None

        scenario_id = match.group(1)
        scenario_title = match.group(2).replace('_', ' ')

        summary = ScenarioSummary(
            scenario_id=scenario_id,
            scenario_title=scenario_title,
            scenario_dir=scenario_dir
        )

        # Load metrics.json
        metrics_file = scenario_dir / 'metrics.json'
        if metrics_file.exists():
            try:
                with open(metrics_file) as f:
                    metrics = json.load(f)
                    summary.variant_count = metrics.get('variant_count', 0)
                    summary.parameters = metrics.get('parameters', {})
                    summary.status = metrics.get('status', 'unknown')
            except Exception as e:
                self.log(f"Error loading metrics for {scenario_id}: {e}", "WARN")

        # Count test data rows
        test_data_file = scenario_dir / 'test_data.csv'
        if test_data_file.exists():
            try:
                with open(test_data_file) as f:
                    summary.test_data_count = sum(1 for _ in f) - 1  # Subtract header
            except Exception as e:
                self.log(f"Error counting test data for {scenario_id}: {e}", "WARN")

        # Count scripts
        scripts_dir = scenario_dir / 'scripts'
        if scripts_dir.exists():
            summary.script_count = len(list(scripts_dir.glob('*.txt')))

        # Parse combinatorial plan
        combo_file = scenario_dir / 'combinatorial_plan.md'
        if combo_file.exists():
            try:
                with open(combo_file) as f:
                    content = f.read()
                    # Extract coverage and optimized count
                    coverage_match = re.search(r'Coverage Percentage:\s*(\d+\.?\d*)%', content)
                    if coverage_match:
                        summary.coverage_pct = float(coverage_match.group(1))

                    count_match = re.search(r'Test Cases Generated:\s*(\d+)', content)
                    if count_match:
                        summary.optimized_count = int(count_match.group(1))
            except Exception as e:
                self.log(f"Error parsing combinatorial plan for {scenario_id}: {e}", "WARN")

        return summary

    def collect_all_metrics(self):
        """Collect metrics from all scenario directories"""
        scenario_dirs = self.discover_scenarios()

        self.log("Collecting metrics from all scenarios...")

        for scenario_dir in scenario_dirs:
            summary = self.load_scenario_metrics(scenario_dir)
            if summary:
                self.scenarios.append(summary)

        self.log(f"Collected metrics for {len(self.scenarios)} scenarios")

    def generate_metrics_dashboard(self, output_file: Path):
        """Generate metrics dashboard markdown"""
        if not self.scenarios:
            self.log("No scenarios to report", "WARN")
            return

        self.log(f"Generating metrics dashboard: {output_file}")

        with open(output_file, 'w') as f:
            f.write("# QA Artifacts Metrics Dashboard\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Source:** {self.scenarios_dir}\n\n")

            # Overall statistics
            total_variants = sum(s.variant_count for s in self.scenarios)
            total_test_data = sum(s.test_data_count for s in self.scenarios)
            total_scripts = sum(s.script_count for s in self.scenarios)
            total_optimized = sum(s.optimized_count for s in self.scenarios)

            f.write("## Overall Statistics\n\n")
            f.write(f"- **Total Scenarios:** {len(self.scenarios)}\n")
            f.write(f"- **Total Variants (Exhaustive):** {total_variants:,}\n")

            if total_test_data > 0:
                f.write(f"- **Total Test Data Rows:** {total_test_data:,}\n")
            if total_scripts > 0:
                f.write(f"- **Total Test Scripts:** {total_scripts:,}\n")
            if total_optimized > 0:
                f.write(f"- **Total Optimized Test Cases:** {total_optimized:,}\n")
                reduction_pct = ((total_variants - total_optimized) / total_variants * 100) if total_variants > 0 else 0
                f.write(f"- **Overall Reduction:** {reduction_pct:.1f}%\n")

            avg_variants = total_variants / len(self.scenarios) if self.scenarios else 0
            f.write(f"- **Avg Variants per Scenario:** {avg_variants:.1f}\n\n")

            # Variant distribution
            f.write("## Variant Distribution\n\n")

            variant_scenarios = [s for s in self.scenarios if s.variant_count > 0]
            if variant_scenarios:
                min_scenario = min(variant_scenarios, key=lambda s: s.variant_count)
                max_scenario = max(variant_scenarios, key=lambda s: s.variant_count)

                f.write(f"- **Min:** {min_scenario.variant_count:,} variants ({min_scenario.scenario_id}: {min_scenario.scenario_title})\n")
                f.write(f"- **Max:** {max_scenario.variant_count:,} variants ({max_scenario.scenario_id}: {max_scenario.scenario_title})\n\n")

            # Top 10 scenarios by variant count
            top_scenarios = sorted(variant_scenarios, key=lambda s: s.variant_count, reverse=True)[:10]
            if top_scenarios:
                f.write("### Top 10 Scenarios by Variant Count\n\n")
                f.write("| Rank | Scenario ID | Title | Variants |\n")
                f.write("|------|-------------|-------|----------|\n")
                for idx, scenario in enumerate(top_scenarios, 1):
                    f.write(f"| {idx} | {scenario.scenario_id} | {scenario.scenario_title[:40]} | {scenario.variant_count:,} |\n")
                f.write("\n")

            # Combinatorial optimization statistics
            optimized_scenarios = [s for s in self.scenarios if s.optimized_count > 0]
            if optimized_scenarios:
                f.write("## Combinatorial Optimization\n\n")

                avg_coverage = sum(s.coverage_pct for s in optimized_scenarios) / len(optimized_scenarios)
                f.write(f"- **Scenarios Optimized:** {len(optimized_scenarios)}\n")
                f.write(f"- **Average Coverage:** {avg_coverage:.1f}%\n\n")

                f.write("### Optimization Results\n\n")
                f.write("| Scenario ID | Exhaustive | Optimized | Reduction | Coverage |\n")
                f.write("|-------------|------------|-----------|-----------|----------|\n")
                for scenario in sorted(optimized_scenarios, key=lambda s: s.scenario_id):
                    reduction = ((scenario.variant_count - scenario.optimized_count) / scenario.variant_count * 100) if scenario.variant_count > 0 else 0
                    f.write(f"| {scenario.scenario_id} | {scenario.variant_count:,} | {scenario.optimized_count:,} | {reduction:.1f}% | {scenario.coverage_pct:.1f}% |\n")
                f.write("\n")

            # Artifacts completion status
            f.write("## Artifacts Completion Status\n\n")
            f.write("| Scenario ID | Variants | Test Data | Scripts | Optimized |\n")
            f.write("|-------------|----------|-----------|---------|----------|\n")
            for scenario in sorted(self.scenarios, key=lambda s: s.scenario_id):
                variants_check = "✓" if scenario.variant_count > 0 else "✗"
                data_check = "✓" if scenario.test_data_count > 0 else "✗"
                scripts_check = "✓" if scenario.script_count > 0 else "✗"
                opt_check = "✓" if scenario.optimized_count > 0 else "✗"

                f.write(f"| {scenario.scenario_id} | {variants_check} ({scenario.variant_count:,}) | {data_check} ({scenario.test_data_count:,}) | {scripts_check} ({scenario.script_count:,}) | {opt_check} ({scenario.optimized_count:,}) |\n")

        self.log(f"✓ Metrics dashboard generated")

    def generate_scenario_index(self, output_file: Path):
        """Generate scenario index JSON"""
        self.log(f"Generating scenario index: {output_file}")

        index = {
            'generated_at': datetime.now().isoformat(),
            'scenarios_dir': str(self.scenarios_dir),
            'total_scenarios': len(self.scenarios),
            'scenarios': []
        }

        for scenario in sorted(self.scenarios, key=lambda s: s.scenario_id):
            index['scenarios'].append({
                'scenario_id': scenario.scenario_id,
                'title': scenario.scenario_title,
                'directory': str(scenario.scenario_dir.relative_to(self.scenarios_dir)),
                'variant_count': scenario.variant_count,
                'test_data_count': scenario.test_data_count,
                'script_count': scenario.script_count,
                'optimized_count': scenario.optimized_count,
                'coverage_pct': scenario.coverage_pct,
                'parameters': scenario.parameters,
                'status': scenario.status
            })

        with open(output_file, 'w') as f:
            json.dump(index, f, indent=2)

        self.log(f"✓ Scenario index generated")

    def combine_all_variants(self, output_file: Path):
        """Combine all scenario variants into one CSV (legacy compatibility)"""
        self.log(f"Combining all variants: {output_file}")

        all_variants = []
        variant_id_counter = 1

        for scenario in sorted(self.scenarios, key=lambda s: s.scenario_id):
            variants_file = scenario.scenario_dir / 'variants.csv'
            if not variants_file.exists():
                continue

            with open(variants_file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Reassign global variant ID
                    row['Variant_ID'] = f'V{variant_id_counter:05d}'
                    variant_id_counter += 1
                    all_variants.append(row)

        if all_variants:
            # Write combined CSV
            with open(output_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=all_variants[0].keys())
                writer.writeheader()
                writer.writerows(all_variants)

            self.log(f"✓ Combined {len(all_variants):,} variants from {len(self.scenarios)} scenarios")
        else:
            self.log("No variants found to combine", "WARN")

    def run(self, reports: List[str], combine_variants: bool = False):
        """
        Run aggregation and generate reports.

        Args:
            reports: List of report types to generate
            combine_variants: Whether to generate combined variants CSV
        """
        # Collect metrics
        self.collect_all_metrics()

        # Create summary directory
        summary_dir = self.scenarios_dir.parent / 'summary'
        summary_dir.mkdir(exist_ok=True)

        # Generate requested reports
        if 'metrics' in reports or 'all' in reports:
            self.generate_metrics_dashboard(summary_dir / 'metrics_dashboard.md')

        if 'index' in reports or 'all' in reports:
            self.generate_scenario_index(summary_dir / 'scenario_index.json')

        if combine_variants:
            self.combine_all_variants(summary_dir / 'all_variants.csv')

        print(f"\n{'='*60}")
        print(f"SUMMARY AGGREGATION COMPLETE")
        print(f"{'='*60}")
        print(f"  Scenarios Processed: {len(self.scenarios)}")
        print(f"  Total Variants: {sum(s.variant_count for s in self.scenarios):,}")
        print(f"  Output Directory: {summary_dir}")
        print(f"{'='*60}\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Summary Aggregator - Aggregate metrics across test scenarios',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all summary reports
  python3 summary_aggregator.py --scenarios-dir deliverables/scenarios

  # Generate specific reports
  python3 summary_aggregator.py --scenarios-dir deliverables/scenarios \\
      --reports metrics,index

  # Include combined variants CSV
  python3 summary_aggregator.py --scenarios-dir deliverables/scenarios \\
      --combine-variants
        """
    )

    parser.add_argument(
        '--scenarios-dir',
        type=Path,
        required=True,
        help='Directory containing scenario folders'
    )
    parser.add_argument(
        '--reports',
        default='all',
        help='Comma-separated list of reports to generate (metrics,index,all) [default: all]'
    )
    parser.add_argument(
        '--combine-variants',
        action='store_true',
        help='Generate combined variants CSV for legacy compatibility'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    try:
        # Parse reports list
        reports = [r.strip() for r in args.reports.split(',')]

        # Create aggregator
        aggregator = SummaryAggregator(
            scenarios_dir=args.scenarios_dir,
            verbose=args.verbose
        )

        # Run aggregation
        aggregator.run(
            reports=reports,
            combine_variants=args.combine_variants
        )

        return 0

    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return 130
    except Exception as e:
        print(f"\n✗ ERROR: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
