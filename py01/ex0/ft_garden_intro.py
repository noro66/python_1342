"""Exercise 0: First Python Program.

This program displays information about a plant in the garden.
Demonstrates the use of if __name__ == "__main__" pattern.
"""

if __name__ == "__main__":
    plant_name: str = "Rose"
    plant_height: int = 13
    plant_age: int = 42
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_name}")
    print(f"Height: {plant_height}cm")
    print(f"Age: {plant_age} days")
    print("\n=== End of Program ===")
