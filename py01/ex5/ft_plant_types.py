"""Exercise 5: Plant Type Hierarchy.

This program demonstrates inheritance by creating specialized
plant types that inherit from a base Plant class.
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


class Flower(Plant):
    """A flowering plant with color and blooming ability.

    Attributes:
        color: The color of the flower petals.
    """

    def __init__(self, name: str, height: int, age: int,
                 color: str) -> None:
        """Initialize a new Flower instance.

        Args:
            name: The name of the flower.
            height: The height in centimeters.
            age: The age in days.
            color: The color of the petals.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Print a blooming message."""
        print(f"{self.name} is blooming beautifully with {self.color} petals!")


class Tree(Plant):
    """A tree with trunk diameter and shade production.

    Attributes:
        trunk_diameter: The diameter of the trunk in centimeters.
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a new Tree instance.

        Args:
            name: The name of the tree.
            height: The height in centimeters.
            age: The age in days.
            trunk_diameter: The trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and print shade area."""
        shade_area = self.trunk_diameter * 2
        print(f"{self.name} provides {shade_area}m² of shade")


class Vegetable(Plant):
    """A vegetable with harvest season and nutritional value.

    Attributes:
        harvest_season: The season for harvesting.
        nutritional_value: The main nutritional benefit.
    """

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a new Vegetable instance.

        Args:
            name: The name of the vegetable.
            height: The height in centimeters.
            age: The age in days.
            harvest_season: The harvest season.
            nutritional_value: The nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def product_nutrition(self) -> None:
        """Print nutritional information."""
        print(f"{self.name} is rich in {self.nutritional_value}")


flowers = [
    ("Rose", 30, 60, "red"),
    ("Tulip", 25, 45, "yellow"),
]

trees = [
    ("Oak", 500, 3650, 80),
    ("Pine", 400, 2920, 60),
]

vegetables = [
    ("Carrot", 20, 90, "autumn", "vitamin A"),
    ("Tomato", 45, 75, "summer", "vitamin C"),
]

flowers_list = []
trees_list = []
vegetables_list = []

for flower in flowers:
    flowers_list.append(Flower(*flower))

for tree in trees:
    trees_list.append(Tree(*tree))

for vegetable in vegetables:
    vegetables_list.append(Vegetable(*vegetable))

for f in flowers_list:
    print(f"{f.name} (Flower): {f.height}cm, {f.age} days, {f.color} color")
    f.bloom()

for t in trees_list:
    print(f"{t.name} (Tree): {t.height}cm, ",
          f"{t.age} days, {t.trunk_diameter}cm²")
    t.produce_shade()

for v in vegetables_list:
    print(f"{v.name} (Vegetable): {v.height}cm, "
          f"{v.age} days, {v.harvest_season}")
    v.product_nutrition()
