'''
SECTION 4: INTERMEDIATE LOGIC-BASED EXCEPTION HANDLING

13. Nested Try-Except Block

**Question:**
Create program:

* Take number input
* Divide 100 by number
* Inside that, convert another input to integer
* Use nested try-except

Handle:

* ZeroDivisionError
* ValueError
'''
try:
    num = int(input("Enter number:"))
    result = 100 / num
    print("Result:",result)

    try:
        value = int(input("Enter another number: "))
        print("You entered:", value)

    except ValueError:
        print("Inner Exception: Invalid input.")

except ZeroDivisionError:
    print("Outer Exception: Cannot divide by zero.")

except ValueError:
    print("Outer Exception: Invalid number.")
    