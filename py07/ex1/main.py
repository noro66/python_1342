from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...\n")
# Deck stats: {'total_cards': 3, 'creatures': 1, 'spells': 1,
# 'artifacts': 1, 'avg_cost': 4.0}
try:
    creature_card = CreatureCard("Fire Dragon", 5, "Rare", 6, 8)
    spell_card = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    artifact_card = ArtifactCard("Mana Crystal",
                                 2, "Common",
                                 3,
                                 "+1 mana per turn"
                                 )

    deck = Deck()
    for card in (creature_card, spell_card, artifact_card):
        deck.add_card(card)
    deck_stats = deck.get_deck_stats()
    print("Deck stats:", deck_stats)
    print()

    print("Drawing and playing cards:\n")
    deck.shuffle()
    for i in range(deck_stats['total_cards']):

        card = deck.draw_card()
        card_info = card.get_card_info()
        print(f"Drew: {card.name} ({card_info['type']})")
        print("Play result:", card.play({}), "\n")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
        )
except Exception as e:
    print("ERROR:", e)
