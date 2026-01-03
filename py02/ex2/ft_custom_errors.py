class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception raised for water-related problems."""
    pass


def check_plant(day_since_watering, water_amount_in_tank):
    """Check plant and water conditions.

    Args:
        day_since_watering: Number of days since last watering.
        water_amount_in_tank: Amount of water in tank.
    Raises:
        PlantError: If plant has not been watered for too long.
        WaterError: If water tank is too low.
    """
    if day_since_watering > 7:
        raise PlantError("The tomato plant is wilting!")
    if water_amount_in_tank < 75:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """Demonstrate custom exception handling and inheritance."""
    try:
        print("Testing PlantError...")
        check_plant(9, 89)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("Testing WaterError...")
        check_plant(2, 49)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    try:
        check_plant(9, 89)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_plant(2, 49)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
