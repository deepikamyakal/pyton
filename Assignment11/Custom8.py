'''
# SECTION 3: CUSTOM EXCEPTIONS

### 8. Custom Age Validation Exception

**Question:**
Create custom exception:

```
InvalidAgeError
```

If age < 18 → raise exception.

**Test Case 1:**
Input: 20
Output: Access granted.

**Test Case 2:**
Input: 15
Output: InvalidAgeError: Age must be 18 or above.
'''
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age:"))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Access granted.")

except InvalidAgeError as e:
    print("InvalidAgeError:",e)
