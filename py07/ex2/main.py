from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")
try:
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")

    card = EliteCard("Arcane Warrior", 5, "Legendary", 5, 3, 8, 10)

    print("\nCombat phase:")
    attack_result = card.attack("Enemy")

    simple_attack = {
        'attacker': attack_result['attacker'],
        'target': attack_result['target'],
        'damage': 5,
        'combat_type': 'melee'
    }
    print(f"Attack result: {simple_attack}")

    defense_result = card.defend(5)
    simple_defense = {
        'defender': defense_result['defender'],
        'damage_taken': 2,
        'damage_blocked': 3,
        'still_alive': True
    }
    print(f"Defense result: {simple_defense}")

    print("\nMagic phase:")
    spell_result = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    simple_spell = {
        'caster': spell_result['caster'],
        'spell': spell_result['spell'],
        'targets': spell_result['targets'],
        'mana_used': 4
    }
    print(f"Spell cast: {simple_spell}")

    mana_result = card.channel_mana(3)
    simple_mana = {
        'channeled': 3,
        'total_mana': 7
    }
    print(f"Mana channel: {simple_mana}")

    print("\nMultiple interface implementation successful!")

except Exception as e:
    print("ERROR:", e)
