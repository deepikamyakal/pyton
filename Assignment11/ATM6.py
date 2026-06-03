'''
6. ATM Withdrawal Simulation

**Question:**
Simulate ATM withdrawal:

* Ask user for withdrawal amount
* If amount > balance → raise error
* Handle invalid input

Balance = 5000

**Test Case 1:**
Input: 2000

Output:
Withdrawal successful. Remaining balance: 3000

**Test Case 2:**
Input: 6000

Output:
Error: Insufficient balance.
'''

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance.")
    
    balance -= amount
    print("Withdrawal successful. Remaining balance:", balance)

except ValueError as e:
    print("Error:", e)
    