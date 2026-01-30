from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        if effect_type not in ("damage", "heal", "buff", "debuff"):
            raise ValueError(
                "Effect type must be one of: " +
                "'damage', 'heal', 'buff', 'debuff'"
                )
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "Spell"

    def play(self, game_state: dict) -> dict:
        return {
         'card_played': self.name,
         'mana_used': self.cost,
         'effect': f"Deal {self.cost} {self.effect_type} to target"
        }

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = self.type
        card_info["effect_type"] = self.effect_type
        return card_info

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'targets': targets,
            'effect_type': self.effect_type,
            'spell_resolved': True
        }
