# 29. Program to Print Star Pattern
'''
**Problem Statement:** Write a program to print the following pattern based on given number of rows.
Example pattern:
```
*
**
***
****
```
**Test Cases:**
• Test Case 1:
Input: rows = 4
Expected Output:
'''

num = int(input("Enter number :"))

for i in range(1,num+1):
    print("*" * i)

