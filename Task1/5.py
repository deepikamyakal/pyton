# 5. Program to Swap Two Numbers
'''
**Problem Statement:** Write a program to swap two numbers entered by the user.

**Test Cases:**
• Test Case 1:
Input: a = 5, b = 10
Expected Output: a = 10, b = 5
'''

a = int(input("Enter your first no:"))
b = int(input("Enter your second no:"))

temp = a
a = b
b = temp

print("After Swapping:")
print("a =", a)
print("b =", b)