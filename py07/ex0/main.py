from ex0 import CreatureCard, Card
from ex0.Card import Rarity
from typing import Dict, Any


try:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:")

    creature: CreatureCard = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)

    print("CreatureCard Info:", creature.get_card_info())

    print()

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(6))
    
    game_state: Dict[str, Any] = {}
    print("Play result:", creature.play(game_state))

    print()

    print(f"{creature.name} attacks Goblin Warrior")
    print("Attack result:", creature.attack_target("Goblin Warrior"))

    print()

    print("Testing insufficient mana (3 available):")
    print("Playable:", creature.is_playable(3))

    print()

    print("Testing different rarities:")
    common_creature: CreatureCard = CreatureCard("Goblin", 2, Rarity.COMMON, 2, 1)
    rare_creature: CreatureCard = CreatureCard("Ancient Dragon", 8, Rarity.RARE, 8, 8)
    
    print(f"Common creature: {common_creature.get_card_info()}")
    print(f"Rare creature: {rare_creature.get_card_info()}")

    print()

    print("Abstract pattern successfully demonstrated!\n")

    try:
        card = Card("Test", 3, Rarity.COMMON)  # type: ignore
    except TypeError as e:
        print(f"Cannot instantiate Card directly: {e}")

except Exception as e:
    print("ERROR:", e)
