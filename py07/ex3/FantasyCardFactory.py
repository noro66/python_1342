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
        name = name_or_power if isinstance(name_or_power, str) \
                else random.choice(["Dragon", "Goblin"])
        return CreatureCard(name, cost=random.randint(1, 5), rarity="Common",
                            attack=5, health=7)

    def create_spell(self, name_or_power=None):
        return SpellCard("Fireball", 3, "Rare", "spell")

    def create_artifact(self, name_or_power=None):
        return ArtifactCard("Mana Ring", 1, "Epic", 6, "artifact_effect")

    def create_themed_deck(self, size: int) -> dict:
        card_list = (self.create_artifact,
                     self.create_creature, self.create_spell)

        deck = [random.choice(card_list)() for _ in range(size)]
        return {"deck": deck, "size": len(deck)}
