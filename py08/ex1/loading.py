"""
Demonstrates package management with pip and Poetry.
"""

import sys
import importlib.util
import importlib.metadata
from typing import Dict, List, Tuple
REQUIRED_PACKAGES = ['pandas', 'requests', 'matplotlib']


def check_package(package_name: str) -> bool:
    """Check if package is installed (without importing)."""
    return importlib.util.find_spec(package_name, package=None) is not None


def get_package_version(package_name: str) -> str:
    """Get version of installed package and Not installed if not installed."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "Not installed"


def check_all_dependencies() -> Dict[str, Tuple[bool, str]]:
    """
    Check all required packages.
    Returns: {'pandas': (True, '2.1.0'), 'numpy': (False, 'Not installed'), ...}
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

    for pkg, (is_installed, version) in deps.items():
        if is_installed:
            print(f"    [OK] {pkg} ({version}) - Ready")
        else:
            print(f"    [MISSING] {pkg} - Not installed")
            is_all_installed = False
    
    return is_all_installed


def print_installation_instructions() -> None:
    """Print how to install missing packages."""
    print()
    print("To install with pip:")
    print("    pip install -r requirements.txt")
    print()
    print("To install with Poetry:")
    print("    poetry install")


def generate_matrix_data(n_points: int = 1000):
    """Generate fake Matrix monitoring data."""
    import numpy as np
    import pandas as pd
    
    np.random.seed(42)
    
    data = {
        'timestamp': np.arange(n_points),
        'anomalies': np.random.randint(0, 100, size=n_points),
        'agents': np.random.randint(1, 50, size=n_points),
    }
    
    return pd.DataFrame(data)


def analyze_data(df):
    """Perform analysis on the data."""
    pass  # You implement


def create_visualization(df, filename: str = 'matrix_analysis.png'):
    """Create and save visualization."""
    import matplotlib.pyplot as plt
    
    pass  # You implement


def main():
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    
    # Step 1: Check dependencies
    deps = check_all_dependencies()
    all_installed = print_dependency_status(deps)
    
    if not all_installed:
        print()
        print_installation_instructions()
        sys.exit(1)
    
    # Step 2: Generate and analyze data
    print()
    print("Analyzing Matrix data...")
    df = generate_matrix_data(1000)
    print(f"Processing {len(df)} data points...")
    
    analyze_data(df)
    
    # Step 3: Create visualization
    print("Generating visualization...")
    create_visualization(df)
    
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()