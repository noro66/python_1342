def ft_count_harvest_recursive(day: int = None) -> None:
    is_initial = day is None
    if day is not None and day <= 0:
        return
    if day is None:
        day = int(input("Days until harvest: "))
    ft_count_harvest_recursive(day - 1)
    print(f"Day {day}")
    if is_initial:
        print("Harvest time!")
