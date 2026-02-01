from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("=== DataDeck Deck Builder ===")

try:
    print("Building deck with different card types...")

    creature = CreatureCard("Fire Dragon", 5, "Rare", 6, 8)
    spell = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Common", 3, "+1 mana per turn")

    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    print("Deck stats:", deck.get_deck_stats())

    print("\nDrawing and playing cards:")
    deck.shuffle()

    while deck.cards:
        card = deck.draw_card()
        card_info = card.get_card_info()
        print(f"\nDrew: {card.name} ({card_info['type']})")
        print("Play result:", card.play({}))

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
        )
except Exception as e:
    print("ERROR:", e)
