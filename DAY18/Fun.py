# Higher order function ---> It takes another function as an argument and return another function as a result.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def calculate(func,x,y):
    return func(x,y)

print(calculate(add,100,200))       # 300
print(calculate(sub,30,15))         # 15
print(calculate(mul,10,20))         # 200


#2) example

def hello(name):
    return "hii " + name

def message(func,name):
    return func(name)

print(message(hello,"Rocky bhai"))      # hii Rocky bhai

