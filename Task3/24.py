# 24. Program to Count Digits in a Number
'''
*Problem Statement:** Write a program to count the number of digits in a given number.

**Test Cases:**
• Test Case 1:
Input: number = 1234
Expected Output: 4
'''
# Program to Count Digits in a Number

num = int(input("Enter number: "))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print("Number of digits:", count)