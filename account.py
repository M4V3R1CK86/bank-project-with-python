# Class Account
class Account:

    # Counstructor
    def __init__(self, number, holder, balance, limit):
        print("Construindo objeto ...{}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
