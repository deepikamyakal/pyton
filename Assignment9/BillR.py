# 14. Calculate Total Bill Using reduce()
'''
**Question:**
Given a list of item prices in cart, calculate total bill.

**Test Case 1:**
Input:
[250, 150, 100]

Expected Output:
500
'''
from functools import reduce
prices = [250,150,100]
total_bill = reduce(lambda x,y:x+y,prices)
print(total_bill)