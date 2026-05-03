# 40. Program to Create Calculator using Functions
'''
**Problem Statement:** Write a program using functions to perform basic arithmetic operations (addition, subtraction, multiplication, division).

**Test Cases:**
• Test Case 1:
Input: add(2, 3)
Expected Output: 5
'''

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def divide(a,b):
    return a/b
 
print("Addition:", add(2, 3))
print("Subtraction:", sub(5, 2))
print("Multiplication:", mul(2, 3))
print("Division:", divide(10, 2))