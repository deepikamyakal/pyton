# 13. Program to Check Leap Year
'''
**Problem Statement:** Write a program to check whether a given year is a leap year.

**Test Cases:**
• Test Case 1:
Input: year = 2020
Expected Output: Leap Year
'''

year = int(input("Enter your leap year :"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a Leap Year")