# 39. Program to Check Prime Number using Function
'''
**Problem Statement:** Write a function to check whether a number is prime.

**Test Cases:**
• Test Case 1:
Input: number = 7
Expected Output: True
'''


def is_prime(number):
    if number <= 1:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

num = int(input("Enter number: "))
print(is_prime(num))