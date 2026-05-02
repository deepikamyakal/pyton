# 3. Program to Check Even or Odd Number
'''
**Problem Statement:** Write a program to check whether a given number is even or odd.

**Test Cases:**
•Test Case 1:
Input: number = 4
Expected Output: Even
'''

num = int(input("Enter your no:"))
if (num % 2 == 0):
    print("Even no")
else:
    print("Odd no")