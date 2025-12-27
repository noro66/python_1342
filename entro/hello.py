class BankAccount:
    def __init__(self, balance):
        self._balance = balance       # Protected (convention)
        self.__secret = "hidden"      # Private (name mangling)

    # Getter method
    def get_balance(self):
        return self._balance

    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount


account = BankAccount(1000)
print(account.get_balance())    # 1000
account._balance = 300
print(account._balance)          # 1000 (accessible but discouraged)
print(dict(account.__dict__))        # secret attribute is not totaly privat
# print(account._BankAccount__secret) # you can also get it like this


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter with validation"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Computed property"""
        return 3.14159 * self._radius ** 2


circle = Circle(5)
print(circle.radius)    # 5 (using getter)
print(circle.area)      # 78.53975
circle.radius = 10      # Using setter
# circle.radius = -1    # ❌ ValueError
