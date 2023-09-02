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

# Getters
    def get_number(self):
        return self.__number

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def get_limit(self):
        return self.__limit

# Setters

    def set_limit(self, limit):
        self.__limit = limit
