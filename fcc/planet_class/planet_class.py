class Planet:
    def __init__(self, name, planet_type, star) -> None:
        if not (isinstance(name, str)
                and isinstance(planet_type, str)
                and isinstance(star, str)
                ):
            raise ValueError("name, planet type, and star must be strings")
        if not (name and planet_type and star):
            raise ValueError(
                "name, planet_type, and star must be non-empty strings"
                )
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self) -> str:
        return (
            f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
        )


plantet_1 = Planet("eart", "blabla", "son")
print(plantet_1)
print(plantet_1.orbit())
plantet_2 = Planet("eart", "blabla", "son")
print(plantet_2)
print(plantet_2.orbit())
plantet_2 = Planet("eart", "blabla", "son")
print(plantet_2)
print(plantet_2.orbit())
