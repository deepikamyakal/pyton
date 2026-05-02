# 7. Program to Calculate Simple Interest
'''
**Problem Statement:** Write a program to calculate simple interest using the formula SI = (P × T × R) / 100.

**Test Cases:**
• Test Case 1:
Input: P = 1000, T = 2, R = 10
Expected Output: 200
'''

P = int(input("Enter your Prnicipal amount:"))
T = int(input("Enter your time(years):"))
R = int(input("Enter your annual interest rate(in percent):"))

SI = (P * T * R) / 100

print("Simple interest :", int(SI))