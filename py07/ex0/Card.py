from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict) -> dict:
        ...
    play = abstractmethod(play)

    def get_card_info(self) -> dict:
        return vars(self)

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
