# Class Account
class Account:

    # Counstructor
    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto ...{}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print("The Balance is {} from Holder {}".format(
            self.__balance,
            self.__holder
        ))

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)
