from ex0 import CreatureCard, Card

print("=== DataDeck Card Foundation ===")

try:
    print("Testing Abstract Base Class Design:")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(creature.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(6))
    print("Play result:", creature.play({}))

    print(f"\n{creature.name} attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print("Playable:", creature.is_playable(3))

    print("\nAbstract pattern successfully demonstrated!")

    try:
        card = Card("Test", 3, "Common")  # type: ignore
    except TypeError as e:
        print(f"\nCannot instantiate Card directly: {e}")

except Exception as e:
    print("ERROR:", e)
