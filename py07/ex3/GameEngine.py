class GameEngine:
    def configure_engine(self, factory, strategy):
        self.factory = factory
        self.strategy = strategy
        # Match these names exactly!
        self.history = {
            "turns_simulated": 0,
            "total_damage": 0,
            "cards_created": 0
        }

    def simulate_turn(self) -> dict:
        # 1. Create the hand
        hand = [self.factory.create_creature() for _ in range(3)]

        # 2. Update stats using the CORRECT keys
        self.history["cards_created"] += len(hand)
        self.history["turns_simulated"] += 1

        # 3. Get the strategy result
        turn_results = self.strategy.execute_turn(hand, [])

        # 4. Extract damage from the dictionary and add to total
        # Make sure your AggressiveStrategy returns this exact path!
        self.history["total_damage"] += turn_results['actions']['damage_dealt']

        return turn_results

    def get_engine_status(self) -> dict:
        # Return the history in the format the subject expects
        return {
            'turns_simulated': self.history['turns_simulated'],
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.history['total_damage'],
            'cards_created': self.history['cards_created']
        }
