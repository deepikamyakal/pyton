# 1. Program to Calculate Total Shopping Bill
'''
Problem Statement:** Write a program to calculate the total bill amount for a customer. 
The program should take prices of three items as input and display the total amount.

**Test Cases:**
• Test Case 1:
Input: item1 = 100, item2 = 200, item3 = 50
Expected Output: 350
'''

item1 = int(input("Enter your first no:"))
item2 = int(input("Enter your second no:"))
item3 = int(input("Enter your third no:"))

total_amount = item1+item2+item3
print("Total bill amount ",total_amount)