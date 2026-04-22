# Types of Arguments

# 1) Positional arguments

def add(a,b):
    return a+b

print(add(10,20))


def add(a,b):
    print(a)
    print(b)
    return a+b

print(add(10,20))


def login(username,password):
    if username == "admin":
        if password == "1234":
            return "Login success"
        else:
            return "wrong password"
    else:
        return "Invalid credentials"

print(login("admin","1234"))        # Login success

print(login("admin","123"))         # wrong password

print(login("admin","rocky"))     # wrong password

print(login("adm","1234"))      # Invalid credentials



def checksign(a):
    if a > 0:
        return "Postive"
    elif a < 0 :
        return "Negative"
    else :
        return "Zero"
    
print(checksign(a=10))
print(checksign(a= -9))
print(checksign(a=0))     



