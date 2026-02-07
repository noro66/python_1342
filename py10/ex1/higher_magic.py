"""Higher Realm - Functions operating on functions."""

from typing import Callable
import sys


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one returning tuple of results."""
    def combined(*args, **kwargs) -> tuple:
        try:
            res1 = spell1(*args, **kwargs)
            res2 = spell2(*args, **kwargs)
            return (res1, res2)
        except Exception as e:
            print("SPELL COMBINER ERROR:", e, file=sys.stderr)
            return (None, None)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify spell result by multiplier."""
    def amplified(*args, **kwargs) -> int:
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception as e:
            print("POWER AMPLIFIER ERROR:", e, file=sys.stderr)
            return 0
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast spell only if condition is True."""
    def conditional(*args, **kwargs) -> str:
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            else:
                return "Spell fizzled"
        except Exception as e:
            print("CONDITIONAL CASTER ERROR:", e, file=sys.stderr)
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Cast all spells in sequence."""
    def sequence(*args, **kwargs) -> list:
        try:
            if not spells:
                return []
            res = []
            for spell in spells:
                res.append(spell(*args, **kwargs))
            return res
        except Exception as e:
            print("SPELL SEQUENCE ERROR:", e, file=sys.stderr)
            return []
    return sequence


def main() -> None:
    """Test higher-order functions."""
    # Test spell_combiner
    print("Testing spell combiner...")
    combined = spell_combiner(lambda target: f"Fireball hits {target}",
                              lambda target: f"Heals {target}")
    print(f"Combined: {combined('Dragon')}")

    # Test power_amplifier
    print("\nTesting power amplifier...")
    mega = power_amplifier(lambda power: power * 2, 3)
    print(f"Original: damage(10), Amplified: {mega(10)}")

    # Test conditional_caster
    print("\nTesting conditional caster...")
    smart_fireball = conditional_caster(
        lambda target: target == "Dragon",
        lambda target: f"Fireball hits {target}"
        )
    print(f"Dragon: {smart_fireball('Dragon')}")
    print(f"Ally: {smart_fireball('Ally')}")

    # Test spell_sequence
    print("\nTesting spell sequence...")
    combo = spell_sequence([lambda target: f"Shields {target}",
                            lambda target: f"Heals {target}",
                            lambda target: f"Shields {target}"])
    print(f"Combo: {combo('Hero')}")

    # Test edge cases
    print("\nTesting edge cases...")
    empty_combo = spell_sequence([])
    print(f"Empty sequence: {empty_combo('test')}")


if __name__ == "__main__":
    main()
