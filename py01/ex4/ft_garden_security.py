class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._age = age
        self._height = height

    def set_height(self, height):
        if height < 0:
            print(f"""Invalid operation attempted: height {height}cm [REJECTED]
Security: Negative height rejected""")
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"""Invalid operation attempted: {age}d [REJECTED]
Security: Negative age rejected""")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


print("=== Garden Security System ===")
rose = SecurePlant("Rose", 21, 23)
print(f"Plant created: {rose.name}")
rose.set_height(25)
rose.set_age(30)
rose.set_height(-5)
rose_info = f"{rose.name} ({rose.get_height()}cm, {rose.get_age()} days)"
print(f"\nCurrent plant: {rose_info}")
