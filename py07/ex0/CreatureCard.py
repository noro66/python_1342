from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not (isinstance(health, int) and health > 0):
            raise ValueError("the health must be a valid positive integer")

        if not (isinstance(attack, int) and attack > 0):
            raise ValueError("the attack must be a valid positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        pass


    def attack_target(self, target) -> dict:
        pass
