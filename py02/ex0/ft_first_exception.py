def check_temperature(temp_str: str) -> int | None:
    """Validate temperature input.
    Args:
        temp_str: A string representing temperature.
    Returns:
        The temperature as int if valid, or None if invalid.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number")
    if -1 <= temp <= 40:
        return temp
    elif temp < -1:
        raise ValueError(f"Error: {temp}°C is too cold" +
                         " for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too" +
                         " hot for plants (max 40°C)")


def test_temperature_input(temp_str):
    """Test temperature validation with various inputs."""

    try:
        temp = check_temperature(temp_str)
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input("25")
    print("")
    test_temperature_input("abc")
    print("")
    test_temperature_input("100")
    print("")
    test_temperature_input("-50")
    print("")
    print("All tests completed - program didn't crash!")
