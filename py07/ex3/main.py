from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

try:
    print("=== DataDeck Game Engine ===")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}")

    print("\nSimulating aggressive turn...")

    turn_execution = engine.simulate_turn()

    hand = turn_execution['hand']
    hand_display = [f"{card.name} ({card.cost})" for card in hand]
    print(f"Hand: {hand_display}")

    print("Turn execution:")
    print(f"Strategy: {turn_execution['strategy']}")
    print(f"Actions: {turn_execution['actions']}")

    print("\nGame Report:")
    status = engine.get_engine_status()
    print(status)

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )

except Exception as e:
    print("ERROR:", e)
