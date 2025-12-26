"""Exercise 3: Plant Factory.

This program demonstrates efficient plant creation using
data lists and tuple unpacking.
"""


class Plant:
    """A class representing a plant in the garden.

    Attributes:
        name: The name of the plant.
        height: The height in centimeters.
        age: The age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance.

        Args:
            name: The name of the plant.
            height: The height in centimeters.
            age: The age in days.
        """
        self.name = name
        self.height = height
        self.age = age


plant_data = [
    ("Rose", 25, 30),
    ("Sunflower", 80, 45),
    ("Cactus", 15, 120),
    ("Tulip", 20, 15),
    ("Orchid", 35, 60),
]

plants = []
plants_number = 0

for plant in plant_data:
    plants.append(Plant(*plant))
    plants_number += 1

print("=== Plant Factory Output ===")
for plant in plants:
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
print(f"\nTotal plants created: {plants_number}")
