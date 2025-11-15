#!/usr/bin/env python3
"""
Scenario Orchestrator - Master script for managing per-scenario QA artifact generation.

VERSION 1.0.0

This script orchestrates the generation of all QA artifacts for test scenarios in
the new scenario-based architecture.

Features:
- Generate artifacts for single or multiple scenarios
- Selective step execution (variants, test-data, scripts, combinatorial)
- Progress tracking and error recovery
- Parallel execution support
- Comprehensive summary reports

Usage:
    # Generate all artifacts for one scenario
    python3 scenario_orchestrator.py --scenario TS-001 --all-steps

    # Generate variants for all scenarios
    python3 scenario_orchestrator.py --all --steps variants

    # Generate specific scenarios with specific steps
    python3 scenario_orchestrator.py --scenarios TS-001,TS-002,TS-010 --steps variants,test-data

    # Parallel generation (4 workers)
    python3 scenario_orchestrator.py --all --steps variants --parallel 4
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime
import time

@dataclass
class StepResult:
    """Result from executing a step"""
    step_name: str
    status: str  # success, failed, skipped
    duration: float = 0.0
    output_file: str = ""
    error_message: str = ""
    metrics: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ScenarioResult:
    """Result from processing a scenario"""
    scenario_id: str
    status: str  # success, partial, failed
    steps: List[StepResult] = field(default_factory=list)
    total_duration: float = 0.0
    artifacts_generated: Dict[str, str] = field(default_factory=dict)


class ScenarioOrchestrator:
    """
    Orchestrates QA artifact generation for test scenarios.
    """

    def __init__(
        self,
        base_dir: Path,
        scenarios_file: Optional[Path] = None,
        verbose: bool = False
    ):
        """
        Initialize the orchestrator.

        Args:
            base_dir: Base output directory for scenarios
            scenarios_file: Path to 03_test_scenarios.md
            verbose: Enable verbose output
        """
        self.base_dir = Path(base_dir)
        self.scenarios_file = Path(scenarios_file) if scenarios_file else None
        self.verbose = verbose
        self.scripts_dir = Path(__file__).parent

    def log(self, message: str, level: str = "INFO"):
        """Log a message"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = f"[{timestamp}] {level}:"
        print(f"{prefix} {message}")

    def run_command(
        self,
        cmd: List[str],
        description: str,
        capture_output: bool = True
    ) -> tuple[int, str, str]:
        """
        Run a shell command.

        Args:
            cmd: Command and arguments
            description: Human-readable description
            capture_output: Capture stdout/stderr

        Returns:
            (return_code, stdout, stderr)
        """
        if self.verbose:
            self.log(f"Running: {' '.join(str(c) for c in cmd)}", "DEBUG")

        try:
            if capture_output:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=600  # 10 minute timeout
                )
                return result.returncode, result.stdout, result.stderr
            else:
                result = subprocess.run(cmd, timeout=600)
                return result.returncode, "", ""

        except subprocess.TimeoutExpired:
            return 1, "", f"Command timed out after 600 seconds"
        except Exception as e:
            return 1, "", str(e)

    def step_generate_variants(
        self,
        scenario_id: str,
        scenario_dir: Path
    ) -> StepResult:
        """
        Execute: Generate variants for scenario.

        Args:
            scenario_id: e.g., "TS-001"
            scenario_dir: Scenario output directory

        Returns:
            StepResult
        """
        start_time = time.time()

        cmd = [
            'python3',
            str(self.scripts_dir / 'generate_variants.py'),
            '--scenario', scenario_id,
            '--output-dir', str(self.base_dir)
        ]

        if self.verbose:
            cmd.append('--verbose')

        returncode, stdout, stderr = self.run_command(
            cmd,
            f"Generate variants for {scenario_id}"
        )

        duration = time.time() - start_time

        if returncode == 0:
            # Load metrics to get variant count
            metrics_file = scenario_dir / 'metrics.json'
            metrics = {}
            if metrics_file.exists():
                with open(metrics_file) as f:
                    metrics = json.load(f)

            return StepResult(
                step_name="variants",
                status="success",
                duration=duration,
                output_file=str(scenario_dir / 'variants.csv'),
                metrics=metrics
            )
        else:
            return StepResult(
                step_name="variants",
                status="failed",
                duration=duration,
                error_message=stderr or stdout
            )

    def step_generate_test_data(
        self,
        scenario_id: str,
        scenario_dir: Path
    ) -> StepResult:
        """
        Execute: Generate test data for scenario.

        Args:
            scenario_id: e.g., "TS-001"
            scenario_dir: Scenario output directory

        Returns:
            StepResult
        """
        start_time = time.time()

        variants_file = scenario_dir / 'variants.csv'
        if not variants_file.exists():
            return StepResult(
                step_name="test-data",
                status="failed",
                duration=0,
                error_message=f"Variants file not found: {variants_file}"
            )

        test_data_file = scenario_dir / 'test_data.csv'

        cmd = [
            'python3',
            str(self.scripts_dir / 'generate_test_data.py'),
            '--scenario', scenario_id,
            '--variants', str(variants_file),
            '--output', str(test_data_file)
        ]

        if self.verbose:
            cmd.append('--verbose')

        returncode, stdout, stderr = self.run_command(
            cmd,
            f"Generate test data for {scenario_id}"
        )

        duration = time.time() - start_time

        if returncode == 0:
            # Count rows
            row_count = 0
            if test_data_file.exists():
                with open(test_data_file) as f:
                    row_count = sum(1 for _ in f) - 1  # Subtract header

            return StepResult(
                step_name="test-data",
                status="success",
                duration=duration,
                output_file=str(test_data_file),
                metrics={'row_count': row_count}
            )
        else:
            return StepResult(
                step_name="test-data",
                status="failed",
                duration=duration,
                error_message=stderr or stdout
            )

    def step_generate_scripts(
        self,
        scenario_id: str,
        scenario_dir: Path
    ) -> StepResult:
        """
        Execute: Generate test scripts for scenario.

        Args:
            scenario_id: e.g., "TS-001"
            scenario_dir: Scenario output directory

        Returns:
            StepResult
        """
        start_time = time.time()

        variants_file = scenario_dir / 'variants.csv'
        test_data_file = scenario_dir / 'test_data.csv'
        scripts_dir = scenario_dir / 'scripts'

        # Check prerequisites
        if not variants_file.exists():
            return StepResult(
                step_name="scripts",
                status="failed",
                duration=0,
                error_message=f"Variants file not found: {variants_file}"
            )

        if not test_data_file.exists():
            return StepResult(
                step_name="scripts",
                status="failed",
                duration=0,
                error_message=f"Test data file not found: {test_data_file}"
            )

        if not self.scenarios_file or not self.scenarios_file.exists():
            return StepResult(
                step_name="scripts",
                status="failed",
                duration=0,
                error_message=f"Scenarios file not provided or not found"
            )

        cmd = [
            'python3',
            str(self.scripts_dir / 'generate_test_scripts_from_variants.py'),
            str(self.scenarios_file),
            str(variants_file),
            str(test_data_file),
            '--output', str(scripts_dir)
        ]

        if self.verbose:
            cmd.append('--verbose')

        returncode, stdout, stderr = self.run_command(
            cmd,
            f"Generate test scripts for {scenario_id}"
        )

        duration = time.time() - start_time

        if returncode == 0:
            # Count scripts
            script_count = 0
            if scripts_dir.exists():
                script_count = len(list(scripts_dir.glob('*.txt')))

            return StepResult(
                step_name="scripts",
                status="success",
                duration=duration,
                output_file=str(scripts_dir),
                metrics={'script_count': script_count}
            )
        else:
            return StepResult(
                step_name="scripts",
                status="failed",
                duration=duration,
                error_message=stderr or stdout
            )

    def step_combinatorial_optimization(
        self,
        scenario_id: str,
        scenario_dir: Path
    ) -> StepResult:
        """
        Execute: Run combinatorial optimization for scenario.

        Args:
            scenario_id: e.g., "TS-001"
            scenario_dir: Scenario output directory

        Returns:
            StepResult
        """
        start_time = time.time()

        variants_file = scenario_dir / 'variants.csv'
        combo_file = scenario_dir / 'combinatorial_plan.md'

        if not variants_file.exists():
            return StepResult(
                step_name="combinatorial",
                status="failed",
                duration=0,
                error_message=f"Variants file not found: {variants_file}"
            )

        cmd = [
            'python3',
            str(self.scripts_dir / 'combinatorial.py'),
            str(variants_file),
            '--output', str(combo_file)
        ]

        if self.verbose:
            cmd.append('--verbose')

        returncode, stdout, stderr = self.run_command(
            cmd,
            f"Run combinatorial optimization for {scenario_id}"
        )

        duration = time.time() - start_time

        if returncode == 0:
            # Extract coverage stats from output
            metrics = {}
            if combo_file.exists():
                with open(combo_file) as f:
                    content = f.read()
                    # Parse stats from markdown
                    for line in content.split('\n'):
                        if 'Coverage Percentage:' in line:
                            metrics['coverage_pct'] = line.split(':')[1].strip()
                        elif 'Test Cases Generated:' in line:
                            metrics['optimized_count'] = line.split(':')[1].strip()

            return StepResult(
                step_name="combinatorial",
                status="success",
                duration=duration,
                output_file=str(combo_file),
                metrics=metrics
            )
        else:
            return StepResult(
                step_name="combinatorial",
                status="failed",
                duration=duration,
                error_message=stderr or stdout
            )

    def process_scenario(
        self,
        scenario_id: str,
        steps_to_run: List[str]
    ) -> ScenarioResult:
        """
        Process a single scenario - run requested steps.

        Args:
            scenario_id: e.g., "TS-001"
            steps_to_run: List of steps to execute

        Returns:
            ScenarioResult
        """
        start_time = time.time()
        self.log(f"Processing scenario: {scenario_id}")

        # Find scenario directory (will be created by first step)
        scenario_dirs = list(self.base_dir.glob(f"{scenario_id}_*"))
        if scenario_dirs:
            scenario_dir = scenario_dirs[0]
        else:
            # Will be created by generate_variants step
            scenario_dir = self.base_dir / f"{scenario_id}_temp"

        result = ScenarioResult(
            scenario_id=scenario_id,
            status="success"
        )

        # Execute steps in order
        step_functions = {
            'variants': self.step_generate_variants,
            'test-data': self.step_generate_test_data,
            'scripts': self.step_generate_scripts,
            'combinatorial': self.step_combinatorial_optimization
        }

        for step_name in steps_to_run:
            if step_name not in step_functions:
                self.log(f"Unknown step: {step_name}", "WARN")
                continue

            self.log(f"  Step: {step_name}")
            step_func = step_functions[step_name]

            # Update scenario_dir after variants generation
            if step_name == 'variants':
                step_result = step_func(scenario_id, scenario_dir)
                # Find actual directory created
                scenario_dirs = list(self.base_dir.glob(f"{scenario_id}_*"))
                if scenario_dirs:
                    scenario_dir = scenario_dirs[0]
            else:
                step_result = step_func(scenario_id, scenario_dir)

            result.steps.append(step_result)

            if step_result.status == "success":
                self.log(f"    ✓ {step_name} completed in {step_result.duration:.1f}s")
                if step_result.output_file:
                    result.artifacts_generated[step_name] = step_result.output_file
            elif step_result.status == "failed":
                self.log(f"    ✗ {step_name} failed: {step_result.error_message}", "ERROR")
                result.status = "failed" if result.status == "success" else "partial"
                # Stop on failure (dependencies)
                break
            else:
                self.log(f"    - {step_name} skipped")

        result.total_duration = time.time() - start_time
        return result

    def run(
        self,
        scenario_ids: List[str],
        steps_to_run: List[str],
        parallel: int = 1
    ) -> List[ScenarioResult]:
        """
        Run orchestration for multiple scenarios.

        Args:
            scenario_ids: List of scenario IDs to process
            steps_to_run: List of steps to execute for each scenario
            parallel: Number of parallel workers (not implemented yet)

        Returns:
            List of ScenarioResult objects
        """
        if parallel > 1:
            self.log(f"Parallel execution not yet implemented, running sequentially", "WARN")

        self.log(f"Processing {len(scenario_ids)} scenarios")
        self.log(f"Steps: {', '.join(steps_to_run)}")
        self.log("=" * 60)

        results = []

        for idx, scenario_id in enumerate(scenario_ids, 1):
            self.log(f"\n[{idx}/{len(scenario_ids)}] {scenario_id}")

            result = self.process_scenario(scenario_id, steps_to_run)
            results.append(result)

            # Progress summary
            if result.status == "success":
                self.log(f"  ✓ Completed in {result.total_duration:.1f}s")
            elif result.status == "partial":
                self.log(f"  ⚠ Partially completed ({len([s for s in result.steps if s.status == 'success'])}/{len(result.steps)} steps)", "WARN")
            else:
                self.log(f"  ✗ Failed", "ERROR")

        return results

    def print_summary(self, results: List[ScenarioResult]):
        """Print summary report"""
        print("\n" + "=" * 60)
        print("ORCHESTRATION SUMMARY")
        print("=" * 60)

        total_scenarios = len(results)
        successful = len([r for r in results if r.status == "success"])
        partial = len([r for r in results if r.status == "partial"])
        failed = len([r for r in results if r.status == "failed"])

        print(f"Total Scenarios: {total_scenarios}")
        print(f"  ✓ Successful: {successful}")
        if partial > 0:
            print(f"  ⚠ Partial: {partial}")
        if failed > 0:
            print(f"  ✗ Failed: {failed}")

        # Step statistics
        all_steps = {}
        for result in results:
            for step in result.steps:
                if step.step_name not in all_steps:
                    all_steps[step.step_name] = {'success': 0, 'failed': 0, 'total_duration': 0}
                if step.status == 'success':
                    all_steps[step.step_name]['success'] += 1
                else:
                    all_steps[step.step_name]['failed'] += 1
                all_steps[step.step_name]['total_duration'] += step.duration

        if all_steps:
            print(f"\nStep Statistics:")
            for step_name, stats in sorted(all_steps.items()):
                total = stats['success'] + stats['failed']
                avg_duration = stats['total_duration'] / total if total > 0 else 0
                print(f"  {step_name}: {stats['success']}/{total} successful (avg {avg_duration:.1f}s)")

        # Aggregate metrics
        total_variants = 0
        total_test_data = 0
        total_scripts = 0

        for result in results:
            for step in result.steps:
                if step.step_name == 'variants' and step.status == 'success':
                    total_variants += step.metrics.get('variant_count', 0)
                elif step.step_name == 'test-data' and step.status == 'success':
                    total_test_data += step.metrics.get('row_count', 0)
                elif step.step_name == 'scripts' and step.status == 'success':
                    total_scripts += step.metrics.get('script_count', 0)

        if total_variants > 0:
            print(f"\nArtifacts Generated:")
            print(f"  Variants: {total_variants:,}")
        if total_test_data > 0:
            print(f"  Test Data Rows: {total_test_data:,}")
        if total_scripts > 0:
            print(f"  Test Scripts: {total_scripts:,}")

        print(f"\nOutput Directory: {self.base_dir}")
        print("=" * 60 + "\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Scenario Orchestrator - Manage per-scenario QA artifact generation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all artifacts for one scenario
  python3 scenario_orchestrator.py --scenario TS-001 --all-steps \\
      --scenarios-file deliverables/03_test_scenarios.md

  # Generate variants for all scenarios
  python3 scenario_orchestrator.py --all --steps variants \\
      --output-dir deliverables/scenarios

  # Generate specific scenarios with specific steps
  python3 scenario_orchestrator.py --scenarios TS-001,TS-002,TS-010 \\
      --steps variants,test-data --output-dir deliverables/scenarios

  # Full pipeline for specific scenarios
  python3 scenario_orchestrator.py --scenarios TS-001,TS-002 \\
      --all-steps --scenarios-file deliverables/03_test_scenarios.md
        """
    )

    # Scenario selection
    scenario_group = parser.add_mutually_exclusive_group(required=True)
    scenario_group.add_argument(
        '--scenario',
        help='Process single scenario (e.g., TS-001)'
    )
    scenario_group.add_argument(
        '--scenarios',
        help='Process specific scenarios (comma-separated, e.g., TS-001,TS-002,TS-010)'
    )
    scenario_group.add_argument(
        '--all',
        action='store_true',
        help='Process all scenarios (TS-001 through TS-106)'
    )

    # Step selection
    step_group = parser.add_mutually_exclusive_group(required=True)
    step_group.add_argument(
        '--steps',
        help='Steps to execute (comma-separated: variants,test-data,scripts,combinatorial)'
    )
    step_group.add_argument(
        '--all-steps',
        action='store_true',
        help='Execute all steps (variants, test-data, scripts, combinatorial)'
    )

    # Configuration
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('deliverables/scenarios'),
        help='Base output directory for scenarios (default: deliverables/scenarios)'
    )
    parser.add_argument(
        '--scenarios-file',
        type=Path,
        help='Path to 03_test_scenarios.md (required for scripts step)'
    )

    # Options
    parser.add_argument(
        '--parallel',
        type=int,
        default=1,
        help='Number of parallel workers (not yet implemented, default: 1)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Determine scenario list
    if args.scenario:
        scenario_ids = [args.scenario]
    elif args.scenarios:
        scenario_ids = [s.strip() for s in args.scenarios.split(',')]
    else:  # --all
        scenario_ids = [f'TS-{i:03d}' for i in range(1, 107)]

    # Determine steps to run
    if args.all_steps:
        steps_to_run = ['variants', 'test-data', 'scripts', 'combinatorial']
    else:
        steps_to_run = [s.strip() for s in args.steps.split(',')]

    # Validate steps
    valid_steps = ['variants', 'test-data', 'scripts', 'combinatorial']
    invalid_steps = [s for s in steps_to_run if s not in valid_steps]
    if invalid_steps:
        print(f"ERROR: Invalid steps: {', '.join(invalid_steps)}")
        print(f"Valid steps: {', '.join(valid_steps)}")
        return 1

    # Check scenarios file if needed
    if 'scripts' in steps_to_run and not args.scenarios_file:
        print("ERROR: --scenarios-file required when generating scripts")
        return 1

    try:
        # Create orchestrator
        orchestrator = ScenarioOrchestrator(
            base_dir=args.output_dir,
            scenarios_file=args.scenarios_file,
            verbose=args.verbose
        )

        # Run orchestration
        results = orchestrator.run(
            scenario_ids=scenario_ids,
            steps_to_run=steps_to_run,
            parallel=args.parallel
        )

        # Print summary
        orchestrator.print_summary(results)

        # Exit code based on results
        if all(r.status == "success" for r in results):
            return 0
        elif any(r.status == "failed" for r in results):
            return 1
        else:
            return 0  # Partial successes still return 0

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
