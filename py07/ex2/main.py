from ex2.EliteCard import EliteCard, DamageType, SpellCategory, CombatStance
from ex0.Card import Rarity
from typing import Dict, Any

print("=== DataDeck Ability System ===")
try:
    print("EliteCard capabilities with Multiple Inheritance:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nCreating Arcane Warrior (Elite Card):\n")

    # Create elite card with comprehensive type hints
    card: EliteCard = \
        EliteCard("Arcane Warrior", 5, Rarity.LEGENDARY, 8, 5, 12, 15)

    # Test card functionality
    print("=== Card Functionality ===")
    game_state: Dict[str, Any] = \
        {"effect": "Powerful warrior-mage enters battle"}
    play_result: Dict[str, Any] = card.play(game_state)
    print(f"Play result: {play_result}")

    card_info: Dict[str, Any] = card.get_card_info()
    print(f"Card info: {card_info}")
    print()

    # Test stance changes and combat
    print("=== Combat System with Stances ===")

    # Test different combat stances
    stance_change: Dict[str, str] = card.change_stance(CombatStance.AGGRESSIVE)
    print(f"Stance change: {stance_change}")

    attack_result: Dict[str, Any] = card.attack("Orc Berserker")
    print(f"Aggressive attack: {attack_result}")

    # Change to defensive stance
    stance_change = card.change_stance(CombatStance.DEFENSIVE)
    print(f"Stance change: {stance_change}")

    defense_result: Dict[str, Any] = card.defend(10)
    print(f"Defensive result: {defense_result}")

    combat_stats: Dict[str, Any] = card.get_combat_stats()
    print(f"Combat stats: {combat_stats}")
    print()

    # Test magic system
    print("=== Magic System with Categories ===")

    magic_stats: Dict[str, Any] = card.get_magic_stats()
    print(f"Initial magic stats: {magic_stats}")

    # Test different spell categories
    offensive_spell: Dict[str, Any] = \
        card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Offensive spell: {offensive_spell}")

    healing_spell: Dict[str, Any] = card.cast_spell("Heal", ["Ally1"])
    print(f"Healing spell: {healing_spell}")

    defensive_spell: Dict[str, Any] = card.cast_spell("Shield", ["Self"])
    print(f"Defensive spell: {defensive_spell}")

    # Test mana channeling with random bonuses
    print("\n=== Mana Channeling Tests ===")
    for i in range(3):
        mana_result: Dict[str, Any] = card.channel_mana(3)
        print(f"Channel attempt {i+1}: {mana_result}")

    updated_magic_stats: Dict[str, Any] = card.get_magic_stats()
    print(f"Updated magic stats: {updated_magic_stats}")
    print()

    # Test invalid operations
    print("=== Error Handling Tests ===")

    # Try unknown spell
    unknown_spell: Dict[str, Any] = card.cast_spell("Meteor", ["Target"])
    print(f"Unknown spell attempt: {unknown_spell}")

    # Try spell without enough mana
    card.mana = 1  # Reduce mana to test insufficient mana
    expensive_spell: Dict[str, Any] = \
        card.cast_spell("Lightning Bolt", ["Enemy1", "Enemy2", "Enemy3"])
    print(f"Insufficient mana attempt: {expensive_spell}")
    print()

    # Test multiple inheritance demonstration
    print("=== Multiple Inheritance Verification ===")
    print(f"EliteCard MRO: {[cls.__name__ for cls in EliteCard.__mro__]}")
    print(f"Is Card: {isinstance(card, type(card).__bases__[0])}")
    print(f"Is Combatable: {isinstance(card, type(card).__bases__[1])}")
    print(f"Is Magical: {isinstance(card, type(card).__bases__[2])}")

    # Show available enums
    print(f"\nAvailable Damage Types: {[dt.value for dt in DamageType]}")
    print(f"Available Spell Categories: {[sc.value for sc in SpellCategory]}")
    print(f"Available Combat Stances: {[cs.value for cs in CombatStance]}")

except Exception as e:
    print("ERROR:", e)
    import traceback
    traceback.print_exc()
