# 23. Program to Reverse a Number
'''
**Problem Statement:** Write a program to reverse the digits of a number.

**Test Cases:**
• Test Case 1:
Input: number = 123
Expected Output: 321
'''

num = int(input("Enter the number :"))

rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse no :", rev)
