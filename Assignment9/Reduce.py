## SECTION 5: reduce()
'''
(Note: Import reduce from functools)
10. Find Sum of List Using reduce()

**Question:**
Use reduce() to find sum of elements.

**Test Case 1:**
Input:
[1,2,3,4]

Expected Output:
10
'''
from functools import reduce
num = [1,2,3,4]

result = reduce(lambda x,y: x + y, num)

print(result)