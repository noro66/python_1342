class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if 0 < new_health <= 100:
            self._health = new_health
        if 0 > new_health:
            self._health = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if 0 <= new_mana <= 50:
            self._mana = new_mana
        if 0 > new_mana:
            self._mana = 0

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        name = f"Name: {self.name}\n"
        level = f"Level: {self.level}\n"
        health = f"Health: {self.health}\n"
        mana = f"Mana: {self.mana}\n"
        return f"{name}{level}{health}{mana}"


hero = GameCharacter('Kratos')  # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)
