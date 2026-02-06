"""Higher Realm - Functions operating on functions."""

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one returning tuple of results."""
    def combined(*args, **kwargs) -> tuple:
        try:
            res1 = spell1(*args, **kwargs)
            res2 = spell2(*args, **kwargs)
            return (res1, res2)
        except Exception:
            return (None, None)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify spell result by multiplier."""
    def amplified(*args, **kwargs):
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception:
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
        except Exception:
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
        except Exception:
            return []
    return sequence

