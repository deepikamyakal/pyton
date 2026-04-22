# Function

print("Hello") # ------> calling function

def is_even():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even()

'''
def add():  # add --> parameter, (a,b) is ---> Arguments
    a=10
    b=20
    c=a+b
    print(c)
add()
'''

def add(a,b):   # parameters
    c=a+b
    print(c)

add(20,30)      # arguments
add(666,96) 
add(222,32) 


def login(user_name,password):
    if user_name == "admin":
        if password == "1234":
            print("login successfull")
        else:
            print("Passord is incorrect")
    else:
        print("User name not matched")

login("admin","1234")