"""Exercise 1: Plant Class.

This program demonstrates creating a Plant class to store
and display information about multiple plants.
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


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
for plant in (rose, sunflower, cactus):
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
