# 6. Program to Find Largest of Three Numbers
'''
**Problem Statement:** Write a program to find the largest among three numbers.

**Test Cases:**
• Test Case 1:
Input: a = 10, b = 20, c = 30
Expected Output: 30
'''

a = int(input("Enter your first no:"))
b = int(input("Enter your second no:"))
c = int(input("Enter your third no:"))

if a >= b and b >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest no :", largest)


# Built-in function using

num1 = 10
num2 = 20
num3 = 30

print("Large no is:", max(num1,num2,num3))