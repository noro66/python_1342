class Plant:
    """A class representing a plant in the garden.
    Attributes:
        name: The name of the plant.
        height: The height in centimeters.
        age: The age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_class_name(self) -> str:
        return "regular"

    def grow(self):
        """Increase plant height by 1cm and print growth message."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self):
        print(f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str,
                 is_blooming: bool) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = is_blooming

    def get_class_name(self) -> str:
        return "flowering"

    def get_info(self):
        s_blmn = "(blooming)" if self.is_blooming else ""
        print(f"{self.name}: {self.height}cm, {self.color} flowers {s_blmn}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, is_blooming: bool, prize: int) -> None:
        super().__init__(name, height, age, color, is_blooming)
        self.prize = prize

    def get_class_name(self) -> str:
        return "prize flowers"

    def get_info(self):
        is_blmn = "(blooming)" if self.is_blooming else ""
        print(f"{self.name}: {self.height}cm, {self.color} flowers "
              f"{is_blmn}, Prize points: {self.prize}")


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []
        self.garden_stats = self.GardenStats()

    class GardenStats:
        def __init__(self) -> None:
            self.plant_total = 0
            self.plants_type = {}
            self.total_grow = 0

        def add_plant_type(self, plant: Plant):
            name = plant.get_class_name()
            if name in self.plants_type:
                self.plants_type[name] += 1
            else:
                self.plants_type[name] = 1

        def get_stats(self):
            print(f"Plants added: {self.plant_total},",
                  f" Total growth: {self.total_grow}cm")
            str_p_type = ""
            for p_type, number in self.plants_type.items():
                str_p_type += f"{number} {p_type}"
                str_p_type += ', '
            str_p_type = str_p_type.strip(', ')
            print("Plant types: ", str_p_type)

    def add_plant(self, plant):
        self.plants.append(plant)
        self.garden_stats.add_plant_type(plant)
        self.garden_stats.plant_total += 1

        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_all(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.garden_stats.total_grow += 1

    @staticmethod
    def validate_height(height):
        return height > 0

    @classmethod
    def create_garden_network(cls):
        alice = cls("Alice")
        bob = cls("Bob")
        return [alice, bob], 2

    def get_report(self):
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print("- ", end="")
            plant.get_info()

    def get_score(self):
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
