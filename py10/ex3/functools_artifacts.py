"""Ancient Library - functools artifacts."""

import sys
from typing import Callable
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using specified operation."""
    try:
        if not spells:
            return 0

        operations = {
            "add": operator.add,
            "multiply": operator.mul,
            "max": max,
            "min": min
        }

        chosen_operator = operations.get(operation)
        if chosen_operator:
            return functools.reduce(chosen_operator, spells)

        print("UNKNOWN OPERATOR!!", file=sys.stderr)
        return 0

    except Exception as e:
        print(f"SPELL REDUCER ERROR: {e}", file=sys.stderr)
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create partial applications for enchantments."""
    try:
        return {
            "fire_enchant": functools.partial(base_enchantment, 50, "fire"),
            "ice_enchant": functools.partial(base_enchantment, 50, "ice"),
            "lightning_enchant": functools.partial(base_enchantment,
                                                   50, "lightning")
        }
    except Exception as e:
        print(f"PARTIAL ENCHANTER ERROR: {e}", file=sys.stderr)
        return {}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate fibonacci with memoization."""
    try:
        if n < 0:
            return 0
        if n < 2:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    except Exception as e:
        print(f"FIBONACCI ERROR: {e}", file=sys.stderr)
        return 0


def spell_dispatcher() -> Callable:
    """Create type-based spell dispatcher."""
    @functools.singledispatch
    def cast(spell) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register(int)
    def _(spell) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def main() -> None:
    """Test functools artifacts."""
    # Test spell_reducer
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    # Test partial_enchanter
    print("\nTesting partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element} enchantment ({power}) on {target}"

    enchants = partial_enchanter(enchant)
    print(enchants['fire_enchant']("Sword"))
    print(enchants['ice_enchant']("Shield"))
    print(enchants['lightning_enchant']("Staff"))

    # Test memoized_fibonacci
    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Fib(20): {memoized_fibonacci(20)}")

    # Test spell_dispatcher
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(50))
    print(cast("Fire"))
    print(cast([1, 2, 3]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
