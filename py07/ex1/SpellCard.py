from ex0.Card import Card, Rarity
from typing import Dict, Any, List
from enum import Enum


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, effect_type: SpellEffect
         ):
        super().__init__(name, cost, rarity)
        self.effect_type: SpellEffect = effect_type
        self.type: str = "Spell"

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        play_result: Dict[str, Any] = {
         'card_played': self.name,
         'mana_used': self.cost,
         'effect': f"Deal {self.cost} {self.effect_type.value} to target"
        }
        return play_result

    def get_card_info(self) -> Dict[str, Any]:
        card_info: Dict[str, Any] = super().get_card_info()
        card_info["type"] = self.type
        card_info["effect_type"] = self.effect_type.value
        return card_info

    def resolve_effect(self, targets: List[str]) -> Dict[str, Any]:
        effect_result: Dict[str, Any] = {
            'spell': self.name,
            'targets': targets,
            'effect_type': self.effect_type.value,
            'spell_resolved': True
        }
        return effect_result
