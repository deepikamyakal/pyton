'''
2. Division Calculator with Exception Handling

**Question:**
Write a program that:

* Takes two numbers from user
* Performs division
* Handles ZeroDivisionError and ValueError

**Test Case 1:**
Input:
10
2

Expected Output:
Result: 5.0

**Test Case 2:**
Input:
10
0

Expected Output:
Error: Cannot divide by zero.

**Test Case 3:**
Input:
10
abc

Expected Output:
Error: Invalid input. Please enter numbers only.
'''

try:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

    result = num1/num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")