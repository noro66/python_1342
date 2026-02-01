from .Card import Card, Rarity
from typing import Dict, Any, Union


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: Rarity, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not (isinstance(health, int) and health > 0):
            raise ValueError("the health must be a valid positive integer")

        if not (isinstance(attack, int) and attack > 0):
            raise ValueError("the attack must be a valid positive integer")

        self.attack: int = attack
        self.health: int = health
        self.type: str = "Creature"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        play_info: Dict[str, Any] = {"card_played": self.name,
                                     "mana_used": self.cost,
                                     "effect": game_state.get(
                                         "effect",
                                         "Creature summoned to battlefield"
                                         )
                                     }
        return play_info

    def get_card_info(self) -> Dict[str, Any]:
        card_info: Dict[str, Any] = super().get_card_info()
        card_info["type"] = self.type

        return card_info

    def attack_target(self, target: Union['CreatureCard',
                                          str]) -> Dict[str, Any]:
        target_name: str = ""
        if isinstance(target, CreatureCard):
            target.health -= self.attack
            target_name = target.name
        elif isinstance(target, str):
            target_name = target
        attack_info: Dict[str, Any] = {"attacker": self.name,
                                       "target": target_name,
                                       "damage_dealt": self.attack,
                                       "combat_resolved": True
                                       }
        return attack_info
