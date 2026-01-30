from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")
try:
    # Show EliteCard capabilities from each interface
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    card = EliteCard("Arcane Warrior", 5, "Legendary", 5, 3, 8, 10)

    print("Combat phase:")
    attack_result = card.attack("Enemy")
    print(f"Attack result: {attack_result}")

    defense_result = card.defend(5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")

    mana_result = card.channel_mana(3)
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")
except Exception as e:
    print("ERROR:", e)
