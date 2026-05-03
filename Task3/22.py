# 22. Program to Generate Multiplication Table
'''
**Problem Statement:** Write a program to generate the multiplication table of a given number up to 10.

**Test Cases:**
• Test Case 1:
Input: number = 2
Expected Output: 2 4 6 8 10 12 14 16 18 20
'''

num = int(input("Enter your no :"))

for i in range(1,11):
    print(num * i , end=" ")
