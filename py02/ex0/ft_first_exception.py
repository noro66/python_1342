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
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold" +
                         " for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too" +
                         " hot for plants (max 40°C)")
    return (temp)


def test_temperature_input():
    """Test temperature validation with various inputs."""

    try:
        temp = check_temperature("25")
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        temp = check_temperature("abc")
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        temp = check_temperature("100")
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        temp = check_temperature("-50")
        print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
    print("")
    print("All tests completed - program didn't crash!")
