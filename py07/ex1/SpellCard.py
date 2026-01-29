from ex0 import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type not in ("damage", "heal", "buff", "debuff"):
            raise ValueError(
                "ERROR: Effect type should be in",
                "('damage', 'heal', 'buff', 'debuff')"
                )
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
         'card_played': self.name,
         'mana_used': self.cost,
         'effect': game_state.get(
                                 "effect " +
                                 f"Deal {self.cost} {self.effect_type}" +
                                 " to target"
                                 )
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'targets': targets,
            'effect_type': self.effect_type,
            'spell_resolved': True
        }
