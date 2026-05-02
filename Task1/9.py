# 9. Program to Check Voting Eligibility
'''
*Problem Statement:** Write a program to check whether a person is eligible to vote based on age.

**Test Cases:**
• Test Case 1:
Input: age = 17
Expected Output: Not Eligible
'''

age = int(input("Enter your age:"))

if age >= 18:
    print("Eligible vote")
else:
    print("Not Eligible")

