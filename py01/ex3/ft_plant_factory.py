class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
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
