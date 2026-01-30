from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self, defense, attack_power: int) -> None:
        self.attack_power = attack_power
        self.defense = defense

    @abstractmethod
    def attack(self, target: str) -> dict:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        ...
