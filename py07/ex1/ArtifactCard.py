from ex0.Card import Card, Rarity
from typing import Dict, Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, durability: int, effect: str):
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability should be a positive integer")

        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect
        self.type: str = "Artifact"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        play_result: Dict[str, Any] = {'card_played': self.name,
                                       'mana_used': self.cost,
                                       'effect': f"Permanent: {self.effect}"}
        return play_result

    def get_card_info(self) -> Dict[str, Any]:
        card_info: Dict[str, Any] = super().get_card_info()
        card_info["type"] = self.type
        card_info["durability"] = self.durability
        card_info["effect"] = self.effect
        return card_info

    def activate_ability(self) -> Dict[str, Any]:
        self.durability -= 1
        activation_result: Dict[str, Any] = {
            'artifact': self.name,
            'effect': self.effect,
            'durability_remaining': self.durability,
            'active': self.durability > 0
        }
        return activation_result
