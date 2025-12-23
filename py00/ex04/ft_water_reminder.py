def ft_water_reminder() -> None:
    no_water_days: int = int(input("Days since last watering: "))
    if no_water_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
