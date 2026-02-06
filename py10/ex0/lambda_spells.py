"""Lambda Sanctum - Master anonymous functions."""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by power level (descending)."""
    try:
        if not artifacts:
            return []
        return sorted(artifacts, key=lambda x: x["power"], reverse=True)
    except (KeyError, TypeError) as e:
        print("ARTIFACT SORT ERROR:", e)
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages with power >= min_power."""
    try:
        if not mages:
            return []
        return list(filter(lambda x: x["power"] >= min_power, mages))
    except (KeyError, TypeError) as e:
        print("POWER_FILTER ERROR:", e)
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    """Add decorations to spell names."""
    try:
        if not spells:
            return []
        return list(map(lambda x: f"* {x} *", spells))
    except TypeError as e:
        print("SPLEE TRANSORMER ERROR:", e)
        return []


def mage_stats(mages: list[dict]) -> dict:
    """Calculate power statistics."""
    default_stats = {
        "max_power": 0,
        "min_power": 0,
        "avg_power": 0.0
    }

    try:
        if not mages:
            return default_stats

        mage_power = list(map(lambda x: x['power'], mages))

        if not mage_power:
            return default_stats

        return {
            "max_power": max(mage_power),
            "min_power": min(mage_power),
            "avg_power": round(sum(mage_power) / len(mage_power), 2)
        }
    except (KeyError, TypeError, ZeroDivisionError) as e:
        print("MAGE STATS ERROR:", e)
        return default_stats


def main() -> None:
    # Test artifact_sorter
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magical'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'fire'},
        {'name': 'Ice Wand', 'power': 78, 'type': 'ice'}
    ]
    print("Sorted artifacts:")
    for a in artifact_sorter(artifacts):
        print(f"  {a['name']}: {a['power']}")

    # Test power_filter
    mages = [
        {'name': 'Alice', 'power': 80, 'element': 'fire'},
        {'name': 'Bob', 'power': 50, 'element': 'water'},
        {'name': 'Charlie', 'power': 90, 'element': 'earth'}
    ]
    print("\nPowerful mages (>= 75):")
    for m in power_filter(mages, 75):
        print(f"  {m['name']}: {m['power']}")

    # Test spell_transformer
    spells = ['fireball', 'heal', 'shield']
    print("\nTransformed spells:")
    print(spell_transformer(spells))

    # Test mage_stats
    print("\nMage stats:")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
