class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)


def print_plant_info(plant: Plant) -> None:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


print("=== Garden Plant Registry ===")
for obj in (rose, sunflower, cactus):
    print_plant_info(obj)
