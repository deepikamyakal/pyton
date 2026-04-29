# 11. Find Product of List Using reduce()
'''
**Question:**
Use reduce() to find product of elements.

**Test Case 1:**
Input:
[1,2,3,4]

Expected Output:
24
'''
from functools import reduce
num = [1,2,3,4]
product = reduce(lambda x,y : x * y, num)
print(product)