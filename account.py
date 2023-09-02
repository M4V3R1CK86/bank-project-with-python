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

    def can_withdraw(self, amount_to_withdraw):
        amount_available = (self.__balance + self.__limit)
        return amount_to_withdraw <= amount_available

    def withdraw(self, amount):

        if (self.can_withdraw(amount)):
            self.__balance -= amount
        else:
            print("The Amount ${} has passed the limit".format(amount))

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)

# Getters
    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

# Setters
    @limit.setter
    def limit(self, limit):
        self.__limit = limit
