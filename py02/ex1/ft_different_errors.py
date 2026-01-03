def garden_operations(error_value):
    """Trigger different types of errors based on input.

    Args:
        error_value: String indicating which error to trigger.
    Raises:
        ValueError: When error_value is "value_error".
        ZeroDivisionError: When error_value is "zero_div_error".
        FileNotFoundError: When error_value is "file_not_found_error".
        KeyError: When error_value is "key_error".
    """
    if error_value == "value_error":
        i = int('abc')
        return (i)
    if error_value == "zero_div_error":
        y = 1/0
        return (y)
    if error_value == "file_not_found_error":
        open("missing.txt", 'r')
    if error_value == "key_error":
        dictionary = {"tomato": 1, "carrot": 2}
        plant = dictionary["missing_plant"]
        return (plant)


def test_error_types():
    """Demonstrate handling different types of Python errors."""
    print("=== Garden Error Types Demo ===")

    print("Testing ValueError...")
    try:
        garden_operations("value_error")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero_div_error")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file_not_found_error")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        garden_operations("key_error")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("Testing multiple errors together...")
    try:
        garden_operations("key_error")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
