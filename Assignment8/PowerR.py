'''
15.Power Function Using Recursion

**Question:**
Find power without using ** operator.

**Test Case 1:**
Input:
power(2,3)

Expected Output:
8
'''

def power(a,n):
    if n == 0:
        return 1
    return a * power(a,n-1)

print(power(2,3))