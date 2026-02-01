from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Any, List
from enum import Enum
import random


class DamageType(Enum):
    MELEE = "melee"
    MAGIC = "magic"
    POISON = "poison"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int, mana: int, health: int):
        Card.__init__(self, name, cost, rarity)
        self.attack_power: int = attack_power
        self.defense: int = defense
        self.mana: int = mana
        self.health: int = health
        self.spells_available: List[str] = \
            ['Fireball', 'Lightning Bolt', 'Heal', 'Shield']

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite warrior enters battlefield'
        }

    def attack(self, target) -> Dict[str, Any]:
        damage_type = random.choice(list(DamageType))
        return {
            'attacker': self.name,
            'target': target if isinstance(target, str) else str(target),
            'damage': self.attack_power,
            'combat_type': damage_type.value
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        damage_blocked = min(incoming_damage, self.defense)
        damage_taken = max(0, incoming_damage - damage_blocked)
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            'attack_power': self.attack_power,
            'defense': self.defense,
            'health': self.health
        }

    def cast_spell(
         self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        mana_cost = len(targets) * 2
        if self.mana < mana_cost:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': [],
                'mana_used': 0,
                'success': False,
                'error': 'Insufficient mana'
            }

        self.mana -= mana_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost,
            'success': True
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            'mana': self.mana,
            'spells_available': self.spells_available
        }
