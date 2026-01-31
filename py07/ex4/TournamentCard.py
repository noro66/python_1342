from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, attack_power, defense):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, defense, attack_power)
        self.wins = 0
        self.losses = 0
        self.base_rating = 1200

    def play(self, game_state: dict) -> dict:
        return {
            "action": "card_played",
            "card": self.name,
            "cost": self.cost,
            "game_state": game_state
        }

    def attack(self, target) -> dict:
        damage = self.attack_power + random.randint(-2, 2)
        return {
            "attacker": self.name,
            "target": str(target),
            "damage_dealt": damage,
            "attack_power": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        actual_damage = max(0, incoming_damage - self.defense)
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage,
            "defense": self.defense,
            "actual_damage": actual_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack_power": self.attack_power,
            "defense": self.defense
        }

    def calculate_rating(self) -> int:
        return self.base_rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}",
            "interfaces": ["Card", "Combatable", "Rankable"]
        }
