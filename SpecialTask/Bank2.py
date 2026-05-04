# 2. Program to Design a Bank Account System
'''
**Problem Statement:**
Create a `BankAccount` class where the constructor initializes account holder name and balance. 
Implement methods to deposit, withdraw, and display balance.

**Task Requirements:**

* Use constructor for initialization
* Ensure withdrawal doesn’t exceed balance
* Update balance after each operation

**Test Cases:**
• Test Case 1:
Input: balance = 1000, withdraw = 500
Expected Output: Balance: 500
'''

class BankAccount:

    def __init__(self, ac_name, balance):
        self.ac_name = ac_name
        self.balance = balance

    def deposite(self, amount):
        self.balance += amount
        print(f"deposited: {amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw : {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Balance : {self.balance}")

B = BankAccount("Deepika", 1000)
B.withdraw(500)
B.display_balance()

B1 = BankAccount("Anu",1000)
B1.withdraw(1500)
B1.display_balance()
        
B2 = BankAccount("Uma",500)
B2.deposite(200)
B2.display_balance()
        