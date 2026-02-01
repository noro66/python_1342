from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.SpellCard import SpellCard, SpellEffect
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck, CardType
from typing import Dict, Any, Union


print("=== DataDeck Deck Builder ===\n")

print("Building deck with different card types...")
try:
    creature_card: CreatureCard = \
        CreatureCard("Fire Dragon", 5, Rarity.RARE, 6, 8)
    spell_card: SpellCard = \
        SpellCard("Lightning Bolt", 3, Rarity.RARE, SpellEffect.DAMAGE)
    artifact_card: ArtifactCard = ArtifactCard("Mana Crystal",
                                               2, Rarity.COMMON,
                                               3,
                                               "+1 mana per turn")

    deck: Deck = Deck()
    for card in (creature_card, spell_card, artifact_card):
        deck.add_card(card)

    deck_stats: Dict[str, Union[int, float]] = deck.get_deck_stats()
    print("Deck stats:", deck_stats)
    print()

    # Test new enum-based functionality
    print("Testing spell effects:")
    heal_spell: SpellCard = \
        SpellCard("Healing Light", 2, Rarity.COMMON, SpellEffect.HEAL)
    buff_spell: \
        SpellCard = SpellCard(
            "Giant Growth", 1, Rarity.UNCOMMON, SpellEffect.BUFF)
    deck.add_card(heal_spell)
    deck.add_card(buff_spell)

    print(f"Heal spell effect: {heal_spell.effect_type.value}")
    print(f"Buff spell effect: {buff_spell.effect_type.value}")
    print()

    # Test deck filtering by type
    spell_cards = deck.find_cards_by_type(CardType.SPELL)
    print(f"Found {len(spell_cards)} spell cards in deck")
    print()

    print("Drawing and playing cards:\n")
    deck.shuffle()
    current_stats: Dict[str, Union[int, float]] = deck.get_deck_stats()
    total_cards: int = int(current_stats['total_cards'])

    for i in range(total_cards):
        card = deck.draw_card()
        card_info: Dict[str, Any] = card.get_card_info()
        print(f"Drew: {card.name} ({card_info['type']})")

        game_state: Dict[str, Any] = {}
        play_result: Dict[str, Any] = card.play(game_state)
        print("Play result:", play_result)

        # Test spell-specific functionality
        if isinstance(card, SpellCard):
            targets = ["Enemy Player"]
            effect_result = card.resolve_effect(targets)
            print("Effect resolved:", effect_result)

        # Test artifact-specific functionality
        elif isinstance(card, ArtifactCard):
            ability_result = card.activate_ability()
            print("Ability activated:", ability_result)

        print()

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
        )
    print("Type safety enforced with Enums and comprehensive type hints!")

except Exception as e:
    print("ERROR:", e)
