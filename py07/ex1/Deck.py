from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

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
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        creatures_len = len([card
                            for card in self.cards
                            if card.type == "Creature"]
                            )
        spells_len = len([card
                          for card in self.cards
                          if card.type == "Spell"]
                         )
        artifact_len = len([card
                            for card in self.cards
                            if card.type == "Artifact"]
                           )
        total = len(self.cards)
        total_cost = sum(card.cost for card in self.cards)
        avg_cost = total_cost / total if total > 0 else 0
        return {'total_cards': total,
                'creatures': creatures_len,
                'spells': spells_len,
                'artifacts': artifact_len,
                'avg_cost': f"{avg_cost:1.f}"
                }
