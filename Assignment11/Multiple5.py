'''
5. Multiple Exception Handling

**Question:**
Write a program that:

* Takes index input from user
* Prints element from list
* Handles IndexError and ValueError

**Test Case 1:**
List: [10, 20, 30]
Input: 1

Output:
Element: 20

**Test Case 2:**
Input: 5

Output:
Error: Index out of range.

**Test Case 3:**
Input: abc

Output:
Error: Invalid index input.
'''

numbers = [10,20,30]

try:
    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index out of range.")

except ValueError:
    print("Error: Invalid index input.")
    