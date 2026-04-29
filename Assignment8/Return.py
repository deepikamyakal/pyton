# SECTION 3: RETURN VS PRINT
'''
6) Print vs Return (Square)
**Question:**
Create:

* One function that prints square
* One function that returns square

**Test Case 1:**
Input:
square_print(5)

Output:
25

Input:
result = square_return(5)
print(result * 10)

Output:
250
'''

def square_print(n):
    print(n*n)

def square_return(n):
    return n * n

square_print(5)
result = square_return(5)
print(result * 10)