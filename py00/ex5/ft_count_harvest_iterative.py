def ft_count_harvest_iterative() -> None:
    harvest_count: int = int(input("Days until harvest: "))
    for day in range(1, harvest_count + 1):
        print(f"Day {day}")
    print("Harvest time!")
