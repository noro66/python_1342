"""Exercise 6: Garden Analytics Platform.

This program demonstrates a comprehensive garden management system
using nested classes, inheritance chains, and different method types.
"""


class Plant:
    """Base class for all plants.

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

    def get_class_name(self) -> str:
        """Return the plant type name.

        Returns:
            A string identifying the plant type.
        """
        return "regular"

    def grow(self) -> None:
        """Increase plant height by 1cm and print growth message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> None:
        """Print plant information."""
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """A flowering plant with color and blooming state.

    Attributes:
        color: The color of the flower petals.
        is_blooming: Whether the plant is currently blooming.
    """

    def __init__(self, name: str, height: int, age: int, color: str,
                 is_blooming: bool) -> None:
        """Initialize a new FloweringPlant instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the petals.
            is_blooming: Whether the plant is blooming.
        """
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def get_class_name(self) -> str:
        """Return the plant type name.

        Returns:
            A string identifying the plant type.
        """
        return "flowering"

    def get_info(self) -> None:
        """Print flowering plant information."""
        s_blmn = "(blooming)" if self.is_blooming else ""
        print(f"{self.name}: {self.height}cm, {self.color} flowers {s_blmn}")


class PrizeFlower(FloweringPlant):
    """A prize-winning flower with points.

    Attributes:
        prize: The prize points for this flower.
    """

    def __init__(self, name: str, height: int, age: int,
                 color: str, is_blooming: bool, prize: int) -> None:
        """Initialize a new PrizeFlower instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the petals.
            is_blooming: Whether the plant is blooming.
            prize: The prize points.
        """
        super().__init__(name, height, age, color, is_blooming)
        self.prize = prize

    def get_class_name(self) -> str:
        """Return the plant type name.

        Returns:
            A string identifying the plant type.
        """
        return "prize flowers"

    def get_info(self) -> None:
        """Print prize flower information."""
        is_blmn = "(blooming)" if self.is_blooming else ""
        print(f"{self.name}: {self.height}cm, {self.color} flowers "
              f"{is_blmn}, Prize points: {self.prize}")


class GardenManager:
    """Manages a garden with plants and statistics.

    Attributes:
        name: The name of the garden owner.
        plants: List of plants in the garden.
        garden_stats: Statistics tracker for the garden.
    """

    class GardenStats:
        """Nested class for tracking garden statistics.

        Attributes:
            plant_total: Total number of plants.
            plants_type: Dictionary of plant types and counts.
            total_grow: Total growth in centimeters.
        """

        def __init__(self) -> None:
            """Initialize garden statistics."""
            self.plant_total = 0
            self.plants_type = {}
            self.total_grow = 0

        def add_plant_type(self, plant: Plant) -> None:
            """Track plant type count.

            Args:
                plant: The plant to track.
            """
            name = plant.get_class_name()
            if name in self.plants_type:
                self.plants_type[name] += 1
            else:
                self.plants_type[name] = 1

        def get_stats(self) -> None:
            """Print garden statistics."""
            print(f"Plants added: {self.plant_total},"
                  f" Total growth: {self.total_grow}cm")
            str_p_type = ""
            for p_type, number in self.plants_type.items():
                str_p_type += f"{number} {p_type}, "
            str_p_type = str_p_type.strip(", ")
            print(f"Plant types: {str_p_type}")

    def __init__(self, name: str) -> None:
        """Initialize a new GardenManager instance.

        Args:
            name: The name of the garden owner.
        """
        self.name = name
        self.plants = []
        self.garden_stats = self.GardenStats()

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden.

        Args:
            plant: The plant to add.
        """
        self.plants.append(plant)
        self.garden_stats.add_plant_type(plant)
        self.garden_stats.plant_total += 1
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self) -> None:
        """Make all plants grow and track total growth."""
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.garden_stats.total_grow += 1

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate that height is positive.

        Args:
            height: The height to validate.

        Returns:
            True if height is valid, False otherwise.
        """
        return height > 0

    @classmethod
    def create_garden_network(cls) -> tuple:
        """Create a network of gardens.

        Returns:
            A tuple containing list of gardens and count.
        """
        alice = cls("Alice")
        bob = cls("Bob")
        return [alice, bob], 2

    def get_report(self) -> None:
        """Print a detailed garden report."""
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end="")
            plant.get_info()

    def get_score(self) -> int:
        """Calculate total garden score.

        Returns:
            The sum of all plant heights.
        """
        total = 0
        for plant in self.plants:
            total += plant.height
        return total


print("=== Garden Management System Demo ===")

gardens, g_number = GardenManager.create_garden_network()
alice = gardens[0]
bob = gardens[1]

oak = Plant("Oak Tree", 100, 50)
rose = FloweringPlant("Rose", 25, 30, "red", True)
sunflower = PrizeFlower("Sunflower", 50, 20, "yellow", True, 10)

alice.add_plant(oak)
alice.add_plant(rose)
alice.add_plant(sunflower)

bob.add_plant(Plant("Cactus", 40, 100))
bob.add_plant(FloweringPlant("Tulip", 20, 15, "pink", True))

alice.grow_all()

alice.get_report()
alice.garden_stats.get_stats()

print(f"Garden scores - Alice: {alice.get_score()}, Bob: {bob.get_score()}")
print(f"Height validation test: {GardenManager.validate_height(50)}")
print(f"Total gardens managed: {g_number}")
