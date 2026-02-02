import sys
import os
from typing import Tuple


def in_virtualenv() -> bool:
    return sys.base_prefix != sys.prefix


def get_virtualenv_info() -> Tuple[str, str]:
    return os.path.basename(sys.prefix), sys.prefix


def get_site_packages_path() -> str:
    """Find where pip actually installs packages"""
    candidates = [p for p in sys.path if 'site-packages' in p]
    if candidates:
        return candidates[0]  # First one is always the active one
    return "Unable to determine"


def main() -> None:
    print("MATRIX STATUS:", "Welcome to the construct"
          if in_virtualenv() else "You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")

    if in_virtualenv():
        venv_name, venv_path = get_virtualenv_info()
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        print(get_site_packages_path())
    else:
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("    python3 -m venv matrix_env")
        if os.name != 'nt':  # Unix
            print("    source matrix_env/bin/activate")
        else:  # Windows
            print("    matrix_env\\Scripts\\activate")
        print("Then run this program again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
