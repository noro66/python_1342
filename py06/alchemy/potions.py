from .elements import create_fire, create_air, create_earth, create_water


def healing_potion():
    fire_result = create_fire()
    water_result = create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    fire_result = create_fire()
    earth_result = create_earth()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    air_result = create_air()
    water_result = create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    water_result = create_water()
    fire_result = create_fire()
    air_result = create_air()
    earth_result = create_earth()
    return (
        "Wisdom potion brewed with all elements:" +
        f"{water_result} {fire_result} {air_result} {earth_result}"
        )
