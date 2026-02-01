from abc import ABC, abstractmethod
from typing import Dict, Any, Union


class Combatable(ABC):
    def __init__(self, defense: int, attack_power: int) -> None:
        self.attack_power: int = attack_power
        self.defense: int = defense

    @abstractmethod
    def attack(self, target: Union['Combatable', str]) -> Dict[str, Any]:
        """Execute an attack on a target"""
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Defend against incoming damage"""
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Union[int, bool]]:
        """Get current combat statistics"""
        pass
