from .TournamentCard import TournamentCard
from typing import Dict, List, Any
import random


class TournamentPlatform:
    def __init__(self):
        self.registered_cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        name_part = card.name.lower().replace(' ', '_')
        id_part = len(self.registered_cards) + 1
        card_id = f"{name_part}_{id_part:03d}"
        self.registered_cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        if card1_id not in self.registered_cards \
         or card2_id not in self.registered_cards:
            return {"error": "One or both cards not found"}

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        card1_power = card1.attack_power + random.randint(-3, 3)
        card2_power = card2.attack_power + random.randint(-3, 3)

        if card1_power >= card2_power:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = card1, card2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> List[Dict[str, Any]]:
        leaderboard = []
        for card_id, card in self.registered_cards.items():
            leaderboard.append({
                "id": card_id,
                "name": card.name,
                "rating": card.calculate_rating(),
                "record": f"{card.wins}-{card.losses}"
            })

        leaderboard.sort(key=lambda x: x["rating"], reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> Dict[str, Any]:
        if not self.registered_cards:
            avg_rating = 0
        else:
            total_rating = sum(card.calculate_rating()
                               for card in self.registered_cards.values())
            avg_rating = total_rating // len(self.registered_cards)

        return {
            "total_cards": len(self.registered_cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
