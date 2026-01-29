from ex0 import CreatureCard, Card


try:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:", creature.get_card_info())

    print()

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(6))
    print("Play result:", creature.play({}))

    print()

    print(f"{creature.name} attacks Goblin Warrior")
    print("Attack result:", creature.attack_target("Goblin Warrior"))

    print()

    print("Testing insufficient mana (3 available):")
    print("Playable:", creature.is_playable(3))

    print()

    print("Abstract pattern successfully demonstrated!\n")

    try:
        card = Card("Test", 3, "Common")  # type: ignore
    except TypeError as e:
        print(f"Cannot instantiate Card directly: {e}")

except Exception as e:
    print("ERROR:", e)
