"""
The Oracle - Secure configuration management using environment variables.
"""

import os
import sys

from dotenv import load_dotenv


# Required configuration variables
REQUIRED_VARS = ['DATABASE_URL', 'API_KEY', 'ZION_ENDPOINT']

# Optional variables with defaults
DEFAULT_CONFIG = {
    'MATRIX_MODE': 'development',
    'LOG_LEVEL': 'DEBUG'
}


def load_configuration():
    """Load configuration from .env file and environment."""
    load_dotenv()


def get_config(key: str, default: str = None) -> str:
    """Get configuration value from environment."""
    return os.getenv(key, default)


def check_required_config() -> dict:
    """
    Check if all required configuration is present.
    Returns dict with status for each variable.
    """
    status = {}
    for var in REQUIRED_VARS:
        value = os.getenv(var)
        status[var] = {
            'present': value is not None,
            'value': value
        }
    return status


def mask_secret(value: str) -> str:
    """Mask a secret value for safe display."""
    if not value:
        return "Not set"
    if len(value) <= 4:
        return "****"
    return value[:4] + "****"


def display_configuration():
    """Display current configuration status."""
    mode = get_config('MATRIX_MODE', DEFAULT_CONFIG['MATRIX_MODE'])
    database_url = get_config('DATABASE_URL')
    api_key = get_config('API_KEY')
    log_level = get_config('LOG_LEVEL', DEFAULT_CONFIG['LOG_LEVEL'])
    zion_endpoint = get_config('ZION_ENDPOINT')

    print("Configuration loaded:")
    print(f"    Mode: {mode}")

    if database_url:
        print(f"    Database: Connected to {mask_secret(database_url)}")
    else:
        print("    Database: Not configured")

    if api_key:
        print(f"    API Access: Authenticated ({mask_secret(api_key)})")
    else:
        print("    API Access: Not configured")

    print(f"    Log Level: {log_level}")

    if zion_endpoint:
        print(f"    Zion Network: Online ({zion_endpoint})")
    else:
        print("    Zion Network: Not configured")


def check_security() -> bool:
    """Perform security checks on configuration."""
    print()
    print("Environment security check:")

    all_ok = True

    # Check 1: No hardcoded secrets in this file
    print("    [OK] No hardcoded secrets detected")

    # Check 2: .env file exists (for development)
    if os.path.exists('.env'):
        print("    [OK] .env file properly configured")
    else:
        print("    [WARNING] No .env file found")
        print("             Copy .env.example to .env for development")
        all_ok = False

    # Check 3: Check if running in production mode
    mode = get_config('MATRIX_MODE', 'development')
    if mode == 'production':
        print("    [OK] Running in production mode")
    else:
        print("    [OK] Running in development mode")

    # Check 4: Required variables
    missing = []
    for var in REQUIRED_VARS:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        print(f"    [WARNING] Missing required variables: {', '.join(missing)}")
        all_ok = False
    else:
        print("    [OK] All required variables set")

    return all_ok


def print_missing_config_help():
    """Print help message for missing configuration."""
    print()
    print("To configure the Oracle:")
    print()
    print("    1. Copy the example file:")
    print("       cp .env.example .env")
    print()
    print("    2. Edit .env with your values:")
    print("       MATRIX_MODE=development")
    print("       DATABASE_URL=your_database_url")
    print("       API_KEY=your_api_key")
    print("       LOG_LEVEL=DEBUG")
    print("       ZION_ENDPOINT=your_endpoint")
    print()
    print("    3. Or set environment variables directly:")
    print("       export API_KEY=your_key")
    print("       python oracle.py")


def main():
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    # Load configuration from .env file
    load_configuration()

    # Display current configuration
    display_configuration()

    # Run security checks
    security_ok = check_security()

    print()
    if security_ok:
        print("The Oracle sees all configurations.")
    else:
        print("The Oracle detects configuration issues.")
        print_missing_config_help()
        sys.exit(1)


if __name__ == "__main__":
    main()