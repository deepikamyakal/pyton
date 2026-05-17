# Python Assignment Set – Intermediate Programming Concepts
'''
## 1. Password Checker

**Concepts Covered:**
Functions, Loops, Conditional Statements

### Problem Statement

Create a Python program that checks whether a given password is **strong or weak** based on predefined security rules. Password validation is a common requirement in modern applications such as banking systems, social media platforms, and enterprise software.

### Requirements

The program should perform the following validations:
1. The password must be **at least 8 characters long**.
2. It must contain **at least one uppercase letter**.
3. It must contain **at least one lowercase letter**.
4. It must contain **at least one numeric digit (0-9)**.
5. It must contain **at least one special character** (such as `@`, `#`, `$`, `%`, `!`, etc.).

### Implementation Guidelines
* Create a **function** named `password_checker()`.
* Accept the password as input from the user.
* Use a **loop** to iterate through each character in the password.
* Use **conditional statements** to check the required conditions.
* Return whether the password is **Strong** or **Weak**.

### Expected Outcome
The program should display a message indicating whether the password satisfies all security requirements.
'''

def password_cheker():
    password = input("Enter your Password :")

    # Conditions
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "@#$%!&"

    # check password length
    if len(password) < 8 :
        print("Weak Password")
        return
    
    # Loop through each character
    for char in password:
        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True
        
        elif char.isdigit():
            has_digit = True

        elif char in special_chars:
            has_special = True

    # Final vaildation
    if has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    else:
        print("Weak Password")

# function call
password_cheker()
