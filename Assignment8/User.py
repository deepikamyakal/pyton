# 2) User-Defined Max, Min, Sum (Without Built-ins)
'''
Write your own functions to calculate:
* Maximum
* Minimum
* Sum
Do NOT use max(), min(), sum().

**Test Case 1:**
Input:
[4, 8, 1, 9]

Expected Output:
Maximum: 9
Minimum: 1
Sum: 22
'''
   
 
def find_max(num):
    max_val = num[0]
    for n in num:
        if n > max_val:
            max_val = n
    return max_val

def find_min(num):
    min_val = num[0]
    for n in num:
        if n < min_val:
            min_val = n
    return min_val

def find_sum(num):
    total = 0
    for n in num:
        total += n
    return total

num = [-5,-2,-10] 
print("Maximum :", find_max(num))
print("Minimum :", find_min(num))
print("Sum of element :", find_sum(num))