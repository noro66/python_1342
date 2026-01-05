class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        transtaction = {'amount': amount, 'description': description}
        self.ledger.append(transtaction)

    def withdraw(self, amount, description=""):
        if amount > 0 and self.check_funds(amount):
            transtaction = {'amount': -amount, 'description': description}
            self.ledger.append(transtaction)
            return True
        return False

    def get_balance(self):
        balance = 0
        for trans in self.ledger:
            balance += trans['amount']
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(
                amount, f"Transfer from {self.name}"
                )
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self) -> str:
        header = self.name.center(30, "*") + '\n'
        details = ""
        for led in self.ledger:
            description = led["description"][:23]
            amount_str = f"{led['amount']:>7.2f}"
            line = f"{description:<23}{amount_str}\n"
            details += line
        total = f"Total: {self.get_balance()}"
        return header + details + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    total_spent = sum(
        [ledger['amount']
         for cate in categories
         for ledger in cate.ledger
         if ledger['amount'] <= 0
         ]
        )
    pesentage = []

    for cat in categories:
        ledger_sum = 0
        for ledger in cat.ledger:
            ledger_sum += ledger['amount'] if ledger['amount'] <= 0 else 0
        pers = (ledger_sum / total_spent) * 100
        rounded = int(pers // 10) * 10
        pesentage.append(rounded)

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pers in pesentage:
            if pers >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += '\n'
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    names = [cat.name for cat in categories]
    max_names_length = max(len(name) for name in names)

    for i in range(max_names_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    chart.rstrip('\n')
    return chart
