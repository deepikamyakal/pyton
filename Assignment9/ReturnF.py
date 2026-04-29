### 5. Returning a Function
'''
**Question:**
Create a function multiplier(n) that returns a function to multiply any number by n.

**Test Case 1:**
Input:
double = multiplier(2)
double(5)

Expected Output:
10
'''
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(5))