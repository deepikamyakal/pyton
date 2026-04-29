'''
12. Sum of Digits (Recursion)

**Question:**
Return sum of digits using recursion.

**Test Case 1:**
Input:
1234

Expected Output:
10
'''
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n//10)

print(sum_digits(1234))
   