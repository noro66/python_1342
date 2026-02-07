"""Higher Realm - Functions operating on functions."""

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one returning tuple of results."""
    def combined(*args, **kwargs) -> tuple:
        try:
            res1 = spell1(*args, **kwargs)
            res2 = spell2(*args, **kwargs)
            return (res1, res2)
        except Exception as e:
            print("SPELL COMBINER ERROR:", e)
            return (None, None)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify spell result by multiplier."""
    def amplified(*args, **kwargs):
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception as e:
            print("POWER AMPLIFIER ERROR:", e)
            return 0
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast spell only if condition is True."""
    def conditional(*args, **kwargs):
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            else:
                return "Spell fizzled"
        except Exception as e:
            print("CONDITIONAL CASTER ERROR:", e)
            return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Cast all spells in sequence."""
    def sequence(*args, **kwargs):
        try:
            if not spells:
                return []
            res = []
            for spell in spells:
                res.append(spell(*args, **kwargs))
            return res
        except Exception as e:
            print("SPELL SEQUENCE ERROR:", e)
            return []
    return sequence


def main() -> None:
    """Test higher-order functions."""
    # Test spell_combiner
    print("Testing spell combiner...")
    fireball = lambda target: f"Fireball hits {target}"
    heal = lambda target: f"Heals {target}"
    combined = spell_combiner(fireball, heal)
    print(f"Combined: {combined('Dragon')}")

    # Test power_amplifier
    print("\nTesting power amplifier...")
    damage = lambda power: power * 2
    mega = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {mega(10)}")

    # Test conditional_caster
    print("\nTesting conditional caster...")
    is_enemy = lambda target: target == "Dragon"
    smart_fireball = conditional_caster(is_enemy, fireball)
    print(f"Dragon: {smart_fireball('Dragon')}")
    print(f"Ally: {smart_fireball('Ally')}")

    # Test spell_sequence
    print("\nTesting spell sequence...")
    shield = lambda target: f"Shields {target}"
    combo = spell_sequence([fireball, heal, shield])
    print(f"Combo: {combo('Hero')}")

    # Test edge cases
    print("\nTesting edge cases...")
    empty_combo = spell_sequence([])
    print(f"Empty sequence: {empty_combo('test')}")


if __name__ == "__main__":
    main()
