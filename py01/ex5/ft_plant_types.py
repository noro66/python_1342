class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully with {self.color} petals!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 2
        print(f"{self.name} provides {shade_area}m² of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def product_nutrition(self):
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
    s = f"{t.name} (Tree): {t.height}cm, {t.age} days, {t.trunk_diameter}cm²"
    print(s)
    t.produce_shade()
for v in vegetables_list:
    s = f"{v.name} (Vegetable): {v.height}cm, {v.age} days, {v.harvest_season}"
    print(s)
    v.product_nutrition()
