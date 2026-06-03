'''
14. Custom Exception with finally Block

**Question:**
Create custom exception:

```
PasswordLengthError
```
If password length < 6 → raise exception
Ensure finally block always prints:
"Validation process completed."
'''
class PasswordLengthError(Exception):
    pass

try:
    password = input("Enter password: ")

    if len(password) < 6:
        raise PasswordLengthError("Password must be at least 6 characters.")
    
    print("Password accepted.")

except PasswordLengthError as e:
    print("PasswordLengthError:",e)

finally:
    print("Validation process completed.")