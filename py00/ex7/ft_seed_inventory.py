def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        last_sintence: str = f"{quantity} {unit} available"
    elif unit == "grams":
        last_sintence: str = f"{quantity} {unit} total"
    elif unit == "area":
        last_sintence: str = f"covers {quantity} sqauare meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {last_sintence}")
