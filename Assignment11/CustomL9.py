'''
9. Custom Login Exception

**Question:**
Create custom exception:

```
LoginError
```
Raise if username is incorrect.

Expected Output Example:
LoginError: Invalid username
'''

class LoginError(Exception):
    pass

try:
    username = input("Enter username: ")

    if username != "admin":
        raise LoginError("Invalid username")
    
    print("Login successful")

except LoginError as e:
    print("LoginError:", e)