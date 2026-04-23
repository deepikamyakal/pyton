# Lambda function ??

# Anonymous function which is defined by lambda keyword 
# single line function 
# which is used for smaller functions 

def add(a,b):
    c = a+b
    return c
print(add(10,20))

print((lambda a,b : a+b)(30,40))    # single    70


# Syntax : 

# lambda parameters : expression  ----> declaration 

# how to call ?? 

# (lambda parameters : expression)(arguments) ---> declaration + calling 

(lambda num : print("even") if num % 2 == 0 else print("odd"))(29)      # odd

def is_even(num):
    if num % 2 == 0:
        print("Even no")
    else:
        print("Odd no")

is_even(31)     # Odd no

# # write a lambda function for multiple conditions (elif) grade system ()

def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 65:
        return "C"
    elif m >= 50:
        return "D"
    else:
        return "F"

print(grade(95))    # A
print(grade(80))    # B
print(grade(70))    # C
print(grade(60))    # D
print(grade(45))    # F