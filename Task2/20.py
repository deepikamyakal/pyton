# 20. Program to Find Sum of First N Numbers
'''
**Problem Statement:** Write a program to calculate the sum of first N natural numbers.

**Test Cases:**
• Test Case 1:
Input: n = 5
Expected Output: 15
'''

num = int(input("Enter the number :"))

sum = 0
for i in range(1, num+1):
    sum += i
print("Sum of first natural no :", sum)