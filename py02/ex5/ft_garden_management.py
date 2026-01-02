class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(plant_name)

    def water_plants(self):
        print("Watering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise WaterError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise WaterError(f"Water level {water_level} is too high (max 10)")
        if sunlight < 2:
            raise GardenError(f"Sunlight hours {sunlight} is too low (min 2)")
        if sunlight > 12:
            raise GardenError(
                f"Sunlight hours {sunlight} is too high (max 12)"
                )
        print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight})")


def test_garden_management():
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
    except PlantError as e:
        print(e)
    try:
        garden.add_plant("lettuce")
    except PlantError as e:
        print(e)
    try:
        garden.add_plant("")
    except PlantError as e:
        print(e)

    garden.water_plants()

    # Section 3: Checking plant health
    print("Checking plant health...")
    # Check tomato with good values (5, 8)
    garden.check_plant_health("tomato", 5, 8)
    # Check lettuce with bad water level (15, 6)

    # Section 4: Error recovery
    print("Testing error recovery...")
    # Raise and catch a GardenError

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()