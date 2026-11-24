class Bankaccount:
    """A Bank account class for a person holding name and money."""

    def __init__(self, name: str, money: float):
        self._name = name
        self._money = money

    def __repr__(self):
        return f"Bank account(owner={self._name},bank_balance={self._money})"

    def deposit(self, amount):
        if amount <= 0:
            print("Please deposit right values of amount")
            return
        self._money = self._money + amount
        print(f"Amount deposited in account {amount}, final balance {self._money}")

    def withdraw(self, amount):
        if self._money < amount:
            print("You don't have enough amount of money to withraw")
            return
        self._money = self._money - amount
        print(f"Amount withdrawed from account {amount}, final balance {self._money}")

    def check_balance(self):
        print(f"current balance is {self._money}")


acc = Bankaccount("Yash Chauhan", 10000)
acc.deposit(500)
acc.withdraw(100)

acc.check_balance()
