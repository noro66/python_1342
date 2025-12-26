"""Exercise 4: Secure Plant.

This program demonstrates encapsulation and data validation
using getters and setters to protect plant data.
"""


class SecurePlant:
    """A secure plant class with protected data.

    Attributes:
        name: The name of the plant.
        _height: Protected height in centimeters.
        _age: Protected age in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new SecurePlant instance.

        Args:
            name: The name of the plant.
            height: The starting height in centimeters.
            age: The starting age in days.
        """
        self.name = name
        self._age = age
        self._height = height

    def set_height(self, height: int) -> None:
        """Set plant height with validation.

        Args:
            height: The new height in centimeters.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set plant age with validation.

        Args:
            age: The new age in days.
        """
        if age < 0:
            print(f"Invalid operation attempted: {age} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return the plant height.

        Returns:
            The height in centimeters.
        """
        return self._height

    def get_age(self) -> int:
        """Return the plant age.

        Returns:
            The age in days.
        """
        return self._age


print("=== Garden Security System ===")
rose = SecurePlant("Rose", 21, 23)
print(f"Plant created: {rose.name}")
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
rose_info = f"{rose.name} ({rose.get_height()}cm, {rose.get_age()} days)"
print(f"\nCurrent plant: {rose_info}")
