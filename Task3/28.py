# 28. Program to Find Sum of Digits
'''
**Problem Statement:** Write a program to calculate the sum of digits of a number.

**Test Cases:**
• Test Case 1:
Input: number = 123
Expected Output: 6
'''

num = int(input("Enter number: "))

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)