import random
from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }

    def create_creature(self, name_or_power=None) -> CreatureCard:
        if name_or_power == "Fire Dragon":
            return CreatureCard("Fire Dragon", cost=5, rarity="Common",
                                attack=5, health=7)
        elif name_or_power == "Goblin Warrior":
            return CreatureCard("Goblin Warrior", cost=2, rarity="Common",
                                attack=5, health=7)
        else:
            creatures = [
                ("Fire Dragon", 5),
                ("Goblin Warrior", 2)
            ]
            name, cost = random.choice(creatures)
            return CreatureCard(name, cost=cost, rarity="Common",
                                attack=5, health=7)

    def create_spell(self, name_or_power=None) -> SpellCard:
        return SpellCard("Lightning Bolt", 3, "Rare", "damage")

    def create_artifact(self, name_or_power=None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 1, "Epic", 6, "artifact_effect")

    def create_themed_deck(self, size: int) -> dict:
        card_list = (self.create_artifact,
                     self.create_creature, self.create_spell)

        deck = [random.choice(card_list)() for _ in range(size)]
        return {"deck": deck, "size": len(deck)}
