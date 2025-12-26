"""Exercise 2: Plant Growth Simulation.

This program simulates plant growth over time by adding
behaviors like grow() and age() to the Plant class.
"""


class Plant:
    """A class representing a plant that can grow and age.

    Attributes:
        name: The name of the plant.
        height: The height in centimeters.
        age_in_days: The age in days.
        growth: Total growth count.
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
        self.age_in_days = age
        self.growth = 0

    def grow(self, height_in_cm: int) -> None:
        """Increase plant height and track growth.

        Args:
            height_in_cm: Amount to grow in centimeters.
        """
        self.height += height_in_cm
        self.growth += 1

    def age(self, age_in_days: int) -> None:
        """Increase plant age.

        Args:
            age_in_days: Number of days to add.
        """
        self.age_in_days += age_in_days

    def get_info(self) -> None:
        """Print current plant information."""
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

day = 0
while day < 7:
    print(f"=== Day {day + 1} ===")
    for plant in (rose, sunflower, cactus):
        plant.get_info()
        plant.grow(1)
        plant.age(1)
    day += 1

for plant in (rose, sunflower, cactus):
    print(f"Growth this week for {plant.name}: +{plant.growth}cm")
