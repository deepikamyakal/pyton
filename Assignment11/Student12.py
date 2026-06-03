'''
12. Student Marks Validation

**Question:**
Create custom exception:

```
InvalidMarksError
```
Marks should be between 0 and 100.

**Test Case 1:**
Input: 85
Output: Valid marks.

**Test Case 2:**
Input: 120
Output: InvalidMarksError: Marks must be between 0 and 100.
'''

class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")
    
    print("Valid marks.")

except InvalidMarksError as e:
    print("InvalidMarksError:", e)