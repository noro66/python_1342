from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return sorted(available_targets)

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        playable_cards = sorted(hand, key=lambda x: x.cost)

        return {
            'strategy': self.get_strategy_name(),
            'actions': {
                'cards_played': [c.name for c in playable_cards[:2]],
                'mana_used': sum(c.cost for c in playable_cards[:2]),
                'targets_attacked': self.prioritize_targets(["Enemy Player"]),
                'damage_dealt': 8  # In a real game, this would be calculated
            }
        }
