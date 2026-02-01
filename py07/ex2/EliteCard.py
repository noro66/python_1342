from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Dict, Any, List, Union
from enum import Enum
import random


class DamageType(Enum):
    MELEE = "melee"
    MAGIC = "magic"
    POISON = "poison"
    FIRE = "fire"
    ICE = "ice"
    LIGHTNING = "lightning"


class SpellCategory(Enum):
    OFFENSIVE = "offensive"
    DEFENSIVE = "defensive"
    UTILITY = "utility"
    HEALING = "healing"


class CombatStance(Enum):
    AGGRESSIVE = "aggressive"
    DEFENSIVE = "defensive"
    BALANCED = "balanced"


class EliteCard(Card, Combatable, Magical):
    """
    Elite card that inherits from multiple interfaces:
    - Card: Basic card functionality
    - Combatable: Combat abilities
    - Magical: Magical abilities
    """

    def __init__(self, name: str, cost: int, rarity: Rarity,
                 attack_power: int, defense: int, mana: int, health: int):
        # Initialize all parent classes
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, defense, attack_power)
        Magical.__init__(self, mana, health)

        self.max_health: int = health
        self.current_stance: CombatStance = CombatStance.BALANCED
        self.spells_available: Dict[str, SpellCategory] = {
            'Fireball': SpellCategory.OFFENSIVE,
            'Lightning Bolt': SpellCategory.OFFENSIVE,
            'Heal': SpellCategory.HEALING,
            'Shield': SpellCategory.DEFENSIVE,
            'Teleport': SpellCategory.UTILITY
        }
        self.damage_types_mastery: List[DamageType] = [
            DamageType.MELEE, DamageType.MAGIC, DamageType.FIRE
        ]

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        play_result: Dict[str, Any] = {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': game_state.get(
                "effect", "Elite warrior enters battlefield"
                ),
            'combat_ready': True,
            'magic_ready': self.mana > 0
        }
        return play_result

    def attack(self, target) -> dict:
        # Randomly choose damage type from mastered types
        damage_type: DamageType = random.choice(self.damage_types_mastery)

        # Apply stance modifiers
        damage_modifier: float = 1.0
        if self.current_stance == CombatStance.AGGRESSIVE:
            damage_modifier = 1.5
        elif self.current_stance == CombatStance.DEFENSIVE:
            damage_modifier = 0.7

        final_damage: int = int(self.attack_power * damage_modifier)

        # Critical hit chance (20%)
        critical_hit: bool = random.random() < 0.2
        if critical_hit:
            final_damage = int(final_damage * 1.5)

        target_name: str = \
            target.name if hasattr(target, 'name') else str(target)

        attack_result: Dict[str, Any] = {
            'attacker': self.name,
            'target': target_name,
            'damage': final_damage,
            'damage_type': damage_type.value,
            'stance': self.current_stance.value,
            'critical_hit': critical_hit
        }
        return attack_result

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        # Apply stance modifiers to defense
        defense_modifier: float = 1.0
        if self.current_stance == CombatStance.DEFENSIVE:
            defense_modifier = 1.5
        elif self.current_stance == CombatStance.AGGRESSIVE:
            defense_modifier = 0.5

        effective_defense: int = int(self.defense * defense_modifier)
        damage_blocked: int = min(incoming_damage, effective_defense)
        damage_taken: int = max(0, incoming_damage - damage_blocked)

        self.health = max(0, self.health - damage_taken)

        defense_result: Dict[str, Any] = {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'effective_defense': effective_defense,
            'stance': self.current_stance.value,
            'still_alive': self.health > 0,
            'current_health': self.health
        }
        return defense_result

    def get_combat_stats(self) -> dict:
        combat_stats: Dict[str, Union[int, bool, str, List[str]]] = {
            'attack_power': self.attack_power,
            'defense': self.defense,
            'health': self.health,
            'max_health': self.max_health,
            'stance': self.current_stance.value,
            'is_alive': self.health > 0,
            'damage_types': [dt.value for dt in self.damage_types_mastery]
        }
        return combat_stats

    def cast_spell(
         self, spell_name: str, targets: List[str]) -> Dict[str, Any]:
        if spell_name not in self.spells_available:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': [],
                'mana_used': 0,
                'success': False,
                'error': f'Spell "{spell_name}" not available'
            }

        spell_category: SpellCategory = self.spells_available[spell_name]
        mana_cost: int = \
            self._calculate_mana_cost(spell_category, len(targets))

        if self.mana < mana_cost:
            return {
                'caster': self.name,
                'spell': spell_name,
                'targets': [],
                'mana_used': 0,
                'success': False,
                'error': 'Insufficient mana.' +
                f" Required: {mana_cost}, Available: {self.mana}"
            }

        self.mana -= mana_cost
        spell_effect: str = \
            self._generate_spell_effect(spell_name, spell_category, targets)

        cast_result: Dict[str, Any] = {
            'caster': self.name,
            'spell': spell_name,
            'category': spell_category.value,
            'targets': targets,
            'mana_used': mana_cost,
            'effect': spell_effect,
            'success': True,
            'remaining_mana': self.mana
        }
        return cast_result

    def channel_mana(self, amount: int) -> Dict[str, Union[int, str]]:
        # Random chance for bonus mana (30% chance for +1 bonus)
        bonus_mana: int = 1 if random.random() < 0.3 else 0
        total_gained: int = amount + bonus_mana

        self.mana += total_gained

        channel_result: Dict[str, Union[int, str]] = {
            'channeled': amount,
            'bonus': bonus_mana,
            'total_gained': total_gained,
            'current_mana': self.mana,
            'efficiency': 'High' if bonus_mana > 0 else 'Normal'
        }
        return channel_result

    def get_magic_stats(self) -> Dict[str, Any]:
        magic_stats: Dict[str, Any] = {
            'mana': self.mana,
            'spells_available': list(self.spells_available.keys()),
            'spell_categories': {spell: category.value
                                 for spell, category
                                 in self.spells_available.items()
                                 },
            'can_cast': self.mana > 0
        }
        return magic_stats

    def change_stance(self, new_stance: CombatStance) -> Dict[str, str]:
        """Change combat stance for tactical advantages"""
        old_stance: CombatStance = self.current_stance
        self.current_stance = new_stance

        stance_change: Dict[str, str] = {
            'warrior': self.name,
            'old_stance': old_stance.value,
            'new_stance': new_stance.value,
            'effect': self._get_stance_description(new_stance)
        }
        return stance_change

    def _calculate_mana_cost(
        self, category: SpellCategory, target_count: int
         ) -> int:
        """Calculate mana cost based on spell category and target count"""
        base_costs: Dict[SpellCategory, int] = {
            SpellCategory.OFFENSIVE: 3,
            SpellCategory.DEFENSIVE: 2,
            SpellCategory.HEALING: 4,
            SpellCategory.UTILITY: 2
        }
        return base_costs[category] + (target_count - 1)

    def _generate_spell_effect(
            self, spell_name: str, category: SpellCategory, targets: List[str]
         ) -> str:
        """Generate appropriate spell effect description"""
        effects: Dict[str, str] = {
            'Fireball': f'Deals fire damage to {", ".join(targets)}',
            'Lightning Bolt': f'Strikes {", ".join(targets)} with lightning',
            'Heal': f'Restores health to {", ".join(targets)}',
            'Shield': f'Protects {", ".join(targets)} with magical barrier',
            'Teleport': f'Transports {", ".join(targets)} to new location'
        }
        return effects.get(
             spell_name, f'Casts {spell_name} on {", ".join(targets)}'
            )

    def _get_stance_description(self, stance: CombatStance) -> str:
        """Get description of stance effects"""
        descriptions: Dict[CombatStance, str] = {
            CombatStance.AGGRESSIVE: '+50% attack damage, -50% defense',
            CombatStance.DEFENSIVE: '+50% defense, -30% attack damage',
            CombatStance.BALANCED: 'Normal attack and defense values'
        }
        return descriptions[stance]
