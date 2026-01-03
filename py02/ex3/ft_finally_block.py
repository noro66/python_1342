def water_plants(plant_list):
    """Water all plants in the list with guaranteed cleanup.

    Args:
        plant_list: List of plant names to water.
    Raises:
        ValueError: If any plant in list is None.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate finally block always executes."""
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("Testing with error...")
    water_plants(["tomato", None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
