from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union


class Magical(ABC):
    def __init__(self, mana: int, health: int) -> None:
        self.mana: int = mana
        self.health: int = health

    @abstractmethod
    def cast_spell(
         self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        """Cast a spell targeting specified entities"""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Union[int, str]]:
        """Channel additional mana"""
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """Get current magical statistics"""
        pass
