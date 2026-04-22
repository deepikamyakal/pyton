# 3) Default arguments

def login(password,username="admin"):
    if username == "admin":
        if password == "1234":
            return "Login success"
        else:
            return "wrong password"
    else:
        return "Invalid credentials"

print(login(username="deepika",password="1234"))        # Invalid credentials