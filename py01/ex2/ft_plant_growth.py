class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age
        self.growth = 0

    def grow(self, height_in_cm):
        self.height += height_in_cm
        self.growth += 1

    def age(self, age_in_days):
        self.age_in_days += age_in_days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)
day = 0
while day < 7:
    print(f"=== Day {day + 1} ===")
    for obj in (rose, sunflower, cactus):
        obj.get_info()
        obj.grow(1)
        obj.age(1)
    day += 1

for obj in (rose, sunflower, cactus):
    print(f"Growth this week for {obj.name}: +{obj.growth}cm")
