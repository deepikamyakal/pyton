## SECTION 2: HIGHER-ORDER FUNCTIONS
'''
(A higher-order function is a function that takes another function as an argument.)

# 4. Function as Argument

**Question:**
Create a function apply_operation(func, a, b)
It should take a function and two numbers.

**Test Case 1:**
Input:
apply_operation(lambda x, y: x + y, 5, 3)

Expected Output:
8
'''

def apply_operation(func,a,b):
    return func(a,b)

result = apply_operation(lambda x,y: x + y, 5, 3)
print(result)