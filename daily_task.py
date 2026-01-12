"""
do this daily
-print statements
-variable assigning
-conditions (if else, case)
-loops(for and while)
-user input
-list
-dictionary
-functions
-try catch or try except since this is python
"""

import datetime


class Bank:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def owner(self):
        print(f"Account is accessed at {datetime.datetime.now()}")
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        print(f"Account is edited at {datetime.datetime.now()}")
        self._owner = new_owner

    @property
    def balance(self):
        print(f"Balance is accessed at {datetime.datetime.now()}")
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        print(f"Balance is edited at {datetime.datetime.now()}")
        self._balance = new_balance

    def withdraw(self, number):
        if self._balance < number:
            print("insufficient balance")
        else:
            self._balance -= number

    def deposit(self, number):
        if number <= 0:
            print("depositted number must be greater than 0")
        else:
            self._balance += number


user = input("name : ")
balance = int(input("Deposit : "))

owner = Bank(user, balance)

print(owner.balance)
con = input("Continue?(Y/N) : ")


while con != "N":
    answer = input(
        "Press B to see balance\nPress D to deposit\nPress W to withdraw\nAsnwer: "
    )

    match answer:
        case "B":
            print(owner.balance)
            con = input("Continue?(Y/N) : ")
        case "D":
            num = int(input("Deposit : "))
            owner.deposit(num)
            print(owner.balance)
            con = input("Continue?(Y/N) : ")
        case "W":
            num = int(input("Withdraw : "))
            owner.withdraw(num)
            print(owner.balance)
            con = input("Continue?(Y/N) : ")
        case _:
            print("Invalid Answer")
            con = input("Continue?(Y/N) : ")
print("Thank You and have a Great Day")
