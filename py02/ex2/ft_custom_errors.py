class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(day_since_watering, water_amount_in_tank):
    if day_since_watering > 7:
        raise PlantError("The tomato plant is wilting!")
    if water_amount_in_tank < 75:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
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
