# 18. Program to Apply Discount
'''
**Problem Statement:** Write a program to apply discount based on purchase amount.
(>1000 → 10%, 500–1000 → 5%, <500 → No discount)

**Test Cases:**
• Test Case 1:
Input: amount = 1200
Expected Output: 10% Discount
'''

amount = int(input("Enter the Amount :"))

if amount > 1000:
    print("10% Discount")
elif amount >= 500:
    print("5% Discount")
else:
    print("No Discount")