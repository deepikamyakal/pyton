# Decorators 
# Decorators : is a func which modifies another function without changing the original code 

# decorator means wrapper 

# gift --> watch --> box --> wrapper / giftcover 

def outer():

    def inner():
        return "inner function"
    return inner()

print(outer())


def wrapper(yy):
    def sample():
        print("before function")
        yy()
        print("aFTER FUNCTION ")
    return sample

@wrapper
def demoyy():
    print("this is demoyy function")
demoyy()


def wrapper(yy):
    def sample(args):
        print("before function")
        yy(args)
        print("aFTER FUNCTION ")
    return sample

@wrapper
def demoyy(args):
    print("this is demoyy function")
    print("msg : ",args)

demoyy("this is a very big headache")



# want to create multiple decorators ??? if yes --> how ?? demonstrate 

# if no --> the y ???? explaination 

