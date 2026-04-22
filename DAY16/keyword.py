# 2) Keyword arguments

def login(password,username):
    if username == "admin":
        if password == "1234":
            return "Login success"
        else:
            return "wrong password"
    else:
        return "Invalid credentials"

print(login(username="admin",password="1234"))    # Login success
