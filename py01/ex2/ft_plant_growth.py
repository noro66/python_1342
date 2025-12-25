class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.growth = 0

    def grow(self, height_in_cm):
        self.height += height_in_cm
        self.growth += 1

    def age(self, age_in_days):
        self._age += age_in_days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")


rose_obj = Plant("Rose", 25, 30)
sunflower_obj = Plant("Sunflower", 80, 45)
cactus_obj = Plant("Cactus", 15, 120)

for day in range(0, 7):
    print(f"=== Day {day + 1} ===")
    for obj in (rose_obj, sunflower_obj, cactus_obj):
        obj.get_info()
        obj.grow(1)
        obj.age(1)

for obj in (rose_obj, sunflower_obj, cactus_obj):
    print(f"Growth this week for {obj.name}: +{obj.growth - 1}")
