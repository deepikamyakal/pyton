# 3. Lambda with Conditional Expression
'''
**Question:**
Create a lambda function that checks whether a number is even or odd.

**Test Case 1:**
Input:
check = lambda x: "Even" if x % 2 == 0 else "Odd"
check(10)

Expected Output:
Even
'''

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))