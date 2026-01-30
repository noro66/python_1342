from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from enum import Enum
import random


class EliteCard(Card, Combatable, Magical):
    class DamageType(Enum):
        MELEE = 1
        MAGIC = 2
        POISON = 3

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int, mana: int, health: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, defense, attack_power)
        Magical.__init__(self, mana, health)
        self.spells_available = ['Fireball', 'Lightning Bolt', 'Heal',
                                 'Shield']

    def play(self, game_state: dict) -> dict:

        return {'card_played': self.name, 'mana_used': self.mana,
                'effect': game_state.get("effect", "some effect")}

    def attack(self, target) -> dict:
        combat_type = random.choice(list(self.DamageType))

        return {
                'attacker': self.name,
                'target': target.name if isinstance(target, Card) else target,
                'damage': self.attack_power,
                'combat_type': combat_type.name.lower()
                }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.defense)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        return {'defender': self.name,
                'damage_taken': damage_taken,
                'damage_blocked': damage_blocked,
                'still_alive': self.health > 0
                }

    def get_combat_stats(self) -> dict:
        return {'attack': self.attack_power,
                'defense': self.defense,
                'health': self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2

        if self.mana < mana_cost:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': [],
                'mana_used': 0,
                'success': False,
                'error': 'Not enough mana'
            }

        self.mana -= mana_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost,
            'success': True
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        return {'mana': self.mana, 'spells_available': self.spells_available}
