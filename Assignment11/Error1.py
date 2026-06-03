'''
# EXCEPTION HANDLING  ASSIGNMENT
ERRORS VS EXCEPTIONS

# 1. Identify Error Type

**Question:**
Write a program that intentionally produces:

* A Syntax Error
* A ZeroDivisionError
* A NameError

Explain which are errors and which are exceptions.

**Task:**
Handle only the runtime exceptions properly using try-except.
'''

try:
    # zeroDivisionError
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero.")

try:
    # NameError
    print(x)
except NameError:
    print("Variable is not defined.")


# Explanation:

# Syntax Error → Error (occurs before execution)
# ZeroDivisionError → Exception (runtime)
# NameError → Exception (runtime)