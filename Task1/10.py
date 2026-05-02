## 10. Program to Implement Grade System
'''
**Problem Statement:** Write a program to assign grades based on marks.

**Test Cases:**
• Test Case 1:
Input: marks = 95
Expected Output: A
'''

marks = int(input("Enter your marks:"))

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 50:
    grade = 'D'
else:
    grade = 'Fail'

print("Grade:", grade)


