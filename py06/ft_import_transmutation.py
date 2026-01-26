import alchemy.elements
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion, create_fire, create_earth

if __name__ == "__main__":
    try:
        print("=== Import Transmutation Mastery ===\n")
        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire():",
              alchemy.elements.create_fire())

        print("\nMethod 2 - Specific function import:")
        print("create_water():", create_water())

        print("\nMethod 3 - Aliased import:")
        print("heal():", heal())

        print("\nMethod 4 - Multiple imports:")
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}")

        print("\nAll import transmutation methods mastered!")
    except Exception as e:
        print("ERROR:", e)
