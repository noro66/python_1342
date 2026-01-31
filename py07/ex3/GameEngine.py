class GameEngine:
    def configure_engine(self, factory, strategy) -> None:
        self.factory = factory
        self.strategy = strategy
        self.history = {
            "turns_simulated": 0,
            "total_damage": 0,
            "cards_created": 0
        }

    def simulate_turn(self) -> dict:
        hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell()
        ]

        self.history["cards_created"] += len(hand)
        self.history["turns_simulated"] += 1

        turn_results = self.strategy.execute_turn(hand, [])

        turn_results["hand"] = hand

        self.history["total_damage"] += turn_results['actions']['damage_dealt']

        return turn_results

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.history['turns_simulated'],
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.history['total_damage'],
            'cards_created': self.history['cards_created']
        }
