
class Bank:
    def __init__(self, client_name, card_number, balance):
        self.__client_name = client_name
        self.__card_number = card_number
        self.__balance = balance

    def print_balance(self):
        print(f"Balance: {self.__balance}")

    def change_balance(self, money):
        self.__balance += money
bank_account = Bank("Alice", "1234-5678-9012-3456", 1000)
bank_account.print_balance()
bank_account.change_balance(200)
bank_account.print_balance()

class Bank:
    def __init__(self, client_name, card_number, balance):
        self.__client_name = client_name
        self.__card_number = card_number
        self.__balance = balance

    def print_balance(self):
        print(f"Balance: {self.__balance}")

    def change_balance(self, money):
        self.__balance += money

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    @balance.deleter
    def balance(self):
        self.__balance = 0


bank_account = Bank("Masha", "9876-5432-1098-7654", 1500)
print(bank_account.balance)
bank_account.balance = 2000
print(bank_account.balance)
del bank_account.balance
print(bank_account.balance)
