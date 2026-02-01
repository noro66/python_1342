from ex0.Card import Card
from typing import List, Dict, Union, Optional
from enum import Enum
import random


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("the card should be  subclass of Card")
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
        creatures_len: int = len([card
                                  for card in self.cards
                                  if hasattr(card, 'type')
                                  and card.type == CardType.CREATURE.value]
                                 )
        spells_len: int = len([card
                               for card in self.cards
                               if hasattr(card, 'type')
                               and card.type == CardType.SPELL.value]
                              )
        artifact_len: int = len([card
                                 for card in self.cards
                                 if hasattr(card, 'type')
                                 and card.type == CardType.ARTIFACT.value]
                                )
        total: int = len(self.cards)
        total_cost: int = sum(card.cost for card in self.cards)
        avg_cost: float = round(total_cost / total, 1) if total > 0 else 0.0

        stats: Dict[str, Union[int, float]] = {'total_cards': total,
                                               'creatures': creatures_len,
                                               'spells': spells_len,
                                               'artifacts': artifact_len,
                                               'avg_cost': avg_cost}
        return stats

    def find_cards_by_type(self, card_type: CardType) -> List[Card]:
        matching_cards: List[Card] = [card for card in self.cards
                                      if hasattr(card, 'type')
                                      and card.type == card_type.value
                                      ]
        return matching_cards

    def get_card_by_name(self, name: str) -> Optional[Card]:
        for card in self.cards:
            if card.name == name:
                return card
        return None
