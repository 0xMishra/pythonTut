"""
restricting the direct access of a piece of data
"""

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance # private variable

    def deposit(self,amount):
        self.__balance += amount
        print(f'deposited {amount}. New balance: {self.__balance}')

    def get_balance(self):
        return self.__balance

account = BankAccount('1234',5000)
account.deposit(2000)
# print(account.__balance) -- this will throw attribute error

print(account.get_balance())
