from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    lead_to_gold_result = lead_to_gold()
    healing_potion_result = healing_potion()
    return (
        "Philosophers stone created using " +
        f"{lead_to_gold_result} and {healing_potion_result}"
    )


def elixir_of_life():
    return "Elixir of life: eternal youth achieved!"
