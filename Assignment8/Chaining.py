#  Function Chaining
'''
**Question:**
Create two functions: add(a, b) and multiply(a, b).
Call multiply using result of add.

**Test Case 1:**
Input:
multiply(add(2,3),4)

Expected Output:
20
'''
def add(a,b):
    return a+b

def multiply(a,b):
    return a * b

result = multiply(add(2,3),4)
print(result)