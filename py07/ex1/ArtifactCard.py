from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str):
        if not isinstance(durability, (int, float)) or durability <= 0:
            raise ValueError("Durability should be a positive integer")

        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name,
                'mana_used': self.cost, 'effect': f"Permanent: {self.effect}"}

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "Artifact"
        return card_info

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {'artifact': self.name, 'effect': self.effect,
                'durability_remaining': self.durability,
                'active': self.durability > 0
                }
