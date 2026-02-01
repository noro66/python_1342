from .Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    def __init__(
         self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)

        if not (isinstance(attack, int) and attack > 0):
            raise ValueError("Attack must be a positive integer")
        if not (isinstance(health, int) and health > 0):
            raise ValueError("Health must be a positive integer")

        self.attack: int = attack
        self.health: int = health
        self.type: str = "Creature"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> Dict[str, Any]:
        card_info = super().get_card_info()
        card_info.update({
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        })
        return card_info

    def attack_target(self, target: str) -> Dict[str, Any]:
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
