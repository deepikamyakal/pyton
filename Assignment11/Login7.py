'''
7. Login System with Limited Attempts

**Question:**
Create login system:

* Correct password = "admin123"
* Allow only 3 attempts
* Raise exception after 3 failed attempts

Expected Output:
Access denied after 3 failed attempts.
'''
correct_password = "admin123"
attempts = 0

while attempts < 3:
    password = input("Enter password:")

    if password == correct_password:
        print("Login successful.")
        break

    attempts += 1

if attempts == 3:
    raise Exception("Access denied after 3 failed attempts.")