'''
SECTION 5: RECURSION

10) Factorial Using Recursion

**Question:**
Write a recursive function to find factorial.

**Test Case 1:**
Input:
factorial(5)

Expected Output:
120

'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))