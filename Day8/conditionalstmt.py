# conditional statements ??
# if , else , elif , nested if 

# if statement ?? decision making 
# syntax 

'''
if condition :
    statement
    statements
    statment  

statements 

if condition 
{

}
else
{

}
'''
age = 19
if age >= 18:
    print("Eligible to vote")
    print("He is a major")
    print("He is a superman")
    print("He is a Batsman")

else:
    print("He is wonder women")
password = input("Enter your password:")
if len(password) >= 8:
    print("Pass accepted")
else:
    print("Pass must be more that 8 characters")
print("if else completed")

username = input("Enter your name:")
if username == "Ram":
    print("Login success")
elif username == "ram":
    print("login success")
elif username == "Remo":
    print("login success")
else:
     print("login failed")


# elif
signal = input("Enter the color:")
if signal == "red":
    print("stop")
elif signal == "orange":
    print("get ready")
elif signal == "white":
    print("close your eyes")
elif signal == "blue":
    print("open your eyes")
else:
    print("go")


# Nested if : if inside a fit condition
username="laxman" 
password="ram123"

if username=="laxman" :
    if password=="ram123" : 
        print("permited")
