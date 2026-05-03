# 12. Program to Validate Login Credentials
'''
Problem Statement:** Write a program to validate a username and password entered by the user. Assume correct credentials are username = "admin" and password = "1234".

**Test Cases:**
• Test Case 1:
Input: username = admin, password = 1234
Expected Output: Login Successful
'''
correct_username = "admin"
correct_password = "1234"

username = input("Enter your username :")
password = input("Enter your password :")

if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")

