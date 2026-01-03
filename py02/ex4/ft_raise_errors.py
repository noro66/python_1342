def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant health parameters.

    Args:
        plant_name: Name of the plant (cannot be empty).
        water_level: Water level between 1-10.
        sunlight_hours: Sunlight hours between 2-12.
    Raises:
        ValueError: If any parameter is invalid.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """Test plant health validation with various inputs."""
    try:
        print("Testing good values...")
        check_plant_health('tomato', 3, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing empty plant name...")
        check_plant_health("", 3, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 3, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
