from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict, Any, Union, Optional, List
import random


class FantasyCardFactory(CardFactory):
    def get_supported_types(self) -> Dict[str, List[str]]:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }

    def create_creature(
         self, name_or_power: Optional[Union[str, int]] = None
         ) -> CreatureCard:
        if name_or_power == "Fire Dragon":
            return CreatureCard("Fire Dragon", 5, "Common", 5, 7)
        elif name_or_power == "Goblin Warrior":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        else:
            creatures = [("Fire Dragon", 5), ("Goblin Warrior", 2)]
            name, cost = random.choice(creatures)
            return CreatureCard(name, cost, "Common", 5, 7)

    def create_spell(
         self, name_or_power: Optional[Union[str, int]] = None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(
        self, name_or_power: Optional[Union[str, int]] = None
         ) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 1, "Epic", 6, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck = []
        for _ in range(size):
            card_type = \
                random.choice(
                    [self.create_creature,
                     self.create_spell,
                     self.create_artifact]
                    )
            deck.append(card_type())
        return {"deck": deck, "size": len(deck)}
