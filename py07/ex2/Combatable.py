from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self, defense, attack_power: int) -> None:
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target: str) -> dict:
        ...
    attack = abstractmethod(attack)

    def defend(self, incoming_damage: int) -> dict:
        ...
    defend = abstractmethod(defend)

    def get_combat_stats(self) -> dict:
        ...
    get_combat_stats = abstractmethod(get_combat_stats)
