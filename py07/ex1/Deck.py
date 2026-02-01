from ex0.Card import Card
from typing import List, Dict, Union
import random


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("Only Card instances can be added to deck")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot draw from empty deck")
        return self.cards.pop()

    def get_deck_stats(self) -> Dict[str, Union[int, float]]:
        creatures = len([card for card in self.cards
                         if hasattr(card, 'type') and card.type == "Creature"])
        spells = len([card for card in self.cards
                      if hasattr(card, 'type') and card.type == "Spell"])
        artifacts = len([card for card in self.cards
                         if hasattr(card, 'type') and card.type == "Artifact"])
        total = len(self.cards)
        avg_cost = round(
            sum(
                card.cost for card in self.cards
                ) / total, 1) if total > 0 else 0.0

        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
