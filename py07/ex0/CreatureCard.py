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
        play_info = {"card_played": self.name,
                     "mana_used": self.cost,
                     "effect": game_state.get(
                         "effect", "Creature summoned to battlefield"
                         )
                     }
        return play_info

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "Creature"

        return card_info

    def attack_target(self, target) -> dict:
        target_name = ""
        if isinstance(target, CreatureCard):
            target.health -= self.attack
            target_name = target.name
        elif isinstance(target, str):
            target_name = target
        attack_info = {"attacker": self.name,
                       "target": target_name,
                       "damage_dealt": self.attack,
                       "combat_resolved": True
                       }
        return attack_info
