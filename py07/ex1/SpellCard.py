from ex0.Card import Card
from typing import Dict, Any, List
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type not in ["damage", "heal", "buff", "debuff"]:
            raise ValueError(
                "Effect type must be one of: damage, heal, buff, debuff"
                )
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type
        self.type: str = "Spell"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Deal {self.cost} {self.effect_type} to target'
        }

    def get_card_info(self) -> Dict[str, Any]:
        card_info = super().get_card_info()
        card_info.update({
            'type': self.type,
            'effect_type': self.effect_type
        })
        return card_info

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        return {
            'spell': self.name,
            'targets': targets,
            'effect_type': self.effect_type,
            'spell_resolved': True
        }
