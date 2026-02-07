"""Memory Depths - Lexical scoping and closures."""

import sys
from typing import Callable, Any


def mage_counter() -> Callable:
    """Create a counting closure."""
    count = 0

    def counter() -> int:
        nonlocal count
        try:
            count = count + 1
            return count
        except Exception as e:
            print("MAGE COUNTER ERROR:", e, file=sys.stderr)
            return 0

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Create power accumulator."""
    total = initial_power

    def add_power(amount: int) -> int:
        nonlocal total
        try:
            total = total + amount
            return total
        except Exception as e:
            print("SPELL ACCUMULATOR ERROR:", e, file=sys.stderr)
            return total

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create enchantment functions."""
    def enchant(item: str) -> str:
        try:
            return f"{enchantment_type} {item}"
        except Exception as e:
            print("ENCHANTMENT FACTORY ERROR:", e, file=sys.stderr)
            return ""

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Create memory management system."""
    storage: dict = {}

    def store(key: str, value: Any) -> None:
        try:
            storage[key] = value
        except Exception as e:
            print("MEMORY VAULT (STORE) ERROR:", e, file=sys.stderr)

    def recall(key: str) -> Any:
        try:
            return storage.get(key, "Memory not found")
        except Exception as e:
            print("MEMORY VAULT (RECALL) ERROR:", e, file=sys.stderr)
            return "Memory not found"

    return {'store': store, 'recall': recall}


def main() -> None:
    """Test closures."""
    # Test mage_counter
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    # Test spell_accumulator
    print("\nTesting spell accumulator...")
    power = spell_accumulator(100)
    print(f"Add 10: {power(10)}")
    print(f"Add 20: {power(20)}")
    print(f"Add -5: {power(-5)}")

    # Test enchantment_factory
    print("\nTesting enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(ice("Shield"))

    # Test memory_vault
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 'password123')
    print(vault['recall']('secret'))
    print(vault['recall']('unknown'))


if __name__ == "__main__":
    main()
