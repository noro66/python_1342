from abc import ABC, abstractmethod
from typing import Dict, Any
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity):
        self.name: str = name
        self.cost: int = cost
        self.rarity: Rarity = rarity

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        ...
    play = abstractmethod(play)

    def get_card_info(self) -> Dict[str, Any]:
        card_info = vars(self).copy()
        card_info['rarity'] = self.rarity.value
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
