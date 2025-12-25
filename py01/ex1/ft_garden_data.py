class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


rose_obj = Plant("Rose", 25, 30)
sunflower_obj = Plant("Sunflower", 80, 45)
cactus_obj = Plant("Cactus", 15, 120)


def print_plant_info(plant: Plant) -> None:
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


print("=== Garden Plant Registry ===")
for obj in (rose_obj, sunflower_obj, cactus_obj):
    print_plant_info(obj)
