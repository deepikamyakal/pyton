# 21. Program to Calculate Factorial of a Number
'''
*Problem Statement:** Write a program to calculate the factorial of a given number using a loop.

**Test Cases:**
• Test Case 1:
Input: number = 5
Expected Output: 120
'''

num = int(input("Enter your no :"))

fact = 1

for i in range(1,num+1):
    fact *= i
    
print("Factorial no:", fact)