"""
Demonstrates package management with pip and Poetry.
"""

import sys
import importlib.metadata
from typing import Dict, Tuple

REQUIRED_PACKAGES = {
    'pandas': 'Data manipulation',
    'requests': 'Network access',
    'matplotlib': 'Visualization',
    'numpy': 'Numerical computations'
}


def check_all_dependencies() -> Dict[str, Tuple[bool, str]]:
    """
    Check all required packages.
    Returns: {'pandas': (True, '2.1.0'),
    'numpy': (False, 'Not installed'), ...}
    """
    result = {}
    for pkg in REQUIRED_PACKAGES:
        try:
            version = importlib.metadata.version(pkg)
            result[pkg] = (True, version)
        except importlib.metadata.PackageNotFoundError:
            result[pkg] = (False, "Not installed")
    return result


def print_dependency_status(deps: Dict[str, Tuple[bool, str]]) -> bool:
    """
    Print status of each dependency.
    Returns True if ALL are installed, False otherwise.
    """
    is_all_installed = True
    req_pkg = REQUIRED_PACKAGES

    for pkg, (is_installed, version) in deps.items():
        if is_installed:
            print(f"    [OK] {pkg} ({version}) - {req_pkg.get(pkg, 'Ready')}")
        else:
            print(f"    [MISSING] {pkg} - Not installed")
            is_all_installed = False

    return is_all_installed


def print_installation_instructions() -> None:
    """Print how to install missing packages."""
    print()
    print("To install with pip:")
    print("    pip install -r requirements.txt")
    print("    python loading.py")
    print()
    print("To install with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def run_analysis():
    """Simple demonstration that all dependencies work."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import requests

    # 1. Use requests - fetch something from internet
    try:
        response = requests.get("https://httpbin.org/get", timeout=5)
        print(f"    Request status: {response.status_code}")
    except requests.RequestException as e:
        print(f"    Request failed: {e}")
        print("    (This is OK - just demonstrating requests is installed)")

    # 2. Use numpy - create random numbers
    data = np.random.rand(100) * 100
    print(f"    Generated {len(data)} random numbers")

    # 3. Use pandas - put data in DataFrame
    df = pd.DataFrame({'signal': data})
    print(f"    Mean value: {df['signal'].mean():.2f}")

    # 4. Use matplotlib - create simple plot
    plt.plot(df['signal'])
    plt.title('Matrix Signal Analysis')
    plt.savefig('matrix_analysis.png')
    plt.close()


def show_package_management_comparison():
    """Display differences between pip and Poetry approaches."""
    print()
    print("=" * 60)
    print("PACKAGE MANAGEMENT COMPARISON")
    print("=" * 60)
    print()
    print("pip + requirements.txt:")
    print("-" * 40)
    print("  • Manual virtual environment creation")
    print("    Command: python -m venv venv")
    print("  • No automatic lock file")
    print("    Must run: pip freeze > requirements.txt")
    print("  • Simple format, widely compatible")
    print("  • No built-in dependency groups")
    print()
    print("Poetry + pyproject.toml:")
    print("-" * 40)
    print("  • Automatic virtual environment management")
    print("    Command: poetry install")
    print("  • Automatic lock file (poetry.lock)")
    print("    Ensures reproducible installations")
    print("  • Structured TOML format")
    print("  • Built-in dev/prod dependency groups")
    print("  • Advanced dependency resolver")
    print()
    print("=" * 60)


def main():
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    # Check dependencies
    deps = check_all_dependencies()
    all_installed = print_dependency_status(deps)

    if not all_installed:
        print()
        print_installation_instructions()
        sys.exit(1)

    show_package_management_comparison()

    # Generate and analyze data
    print()
    print("Analyzing Matrix data...")
    run_analysis()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
