'''
SECTION 2: try, except, else, finally

# 3. Number Validation Program

**Question:**
Take input from user and:

* Convert to integer
* Print square of number

Use:

* try
* except
* else
* finally

**Test Case 1:**
Input: 5

Expected Output:
Square: 25
Execution completed.

**Test Case 2:**
Input: abc

Expected Output:
Invalid input.
Execution completed.
'''

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")

else:
    print("Square:", num ** 2)
finally:
    print("Execution completed.")