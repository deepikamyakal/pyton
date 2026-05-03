# 11. Program to Check Divisibility by 3 and 5
'''
Problem Statement:** Write a program to check whether a number is divisible by both 3 and 5.

**Test Cases:**
• Test Case 1:
Input: number = 15
Expected Output: Divisible by both
'''

num = int(input("Enter your number :"))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not Divisible by both")
    