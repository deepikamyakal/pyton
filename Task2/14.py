# 14. Program to Simulate ATM Withdrawal
'''
**Problem Statement:** Write a program to simulate ATM withdrawal. 
Check if the withdrawal amount is less than or equal to balance.

**Test Cases:**
• Test Case 1:
Input: balance = 1000, withdraw = 500
Expected Output: Transaction Successful
'''

balance = int(input("Enter account balance :"))
withdraw = int(input("Enter withdrawal amount :"))

if withdraw <= balance:
    print("Transaction sucessful")
else:
    print("Insufficient balance")