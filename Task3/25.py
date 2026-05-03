# 25. Program to Generate Fibonacci Series
'''
*Problem Statement:** Write a program to generate Fibonacci series up to N terms.

**Test Cases:**
• Test Case 1:
Input: n = 5
Expected Output: 0 1 1 2 3
'''

n = int(input("Enter number :"))

a,b = 0,1

for i in range(n):
    print(a,end=" ")
    a,b = b,a+b