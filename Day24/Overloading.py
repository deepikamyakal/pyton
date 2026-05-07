# Operator Overloading :  one operator behaving differently for different datatypes 

# "+"
print(100+99)       # addition operator
print("Deepika"+" is a good girl")  # concatenate 

k = [1,2,3,4,5,6]
l = [98,99,77]
print(k+l)  # joins

#  " * "
print(10*3)
print("Sai " * 5)

# *args ---> multiple parameters (packing and unpacking arguments)

# if a function handles more than one datatype or different parameter size, then it is also called as ploymorphism 

def sample(*a):
    print(a)

sample(10,20,30,40)


class A:
    def demo(self):
        print("Class A method")

class B:
    def demo(self):
        print("Class B method")

class C:
    def demo(self):
        print("Class C method")

def poly(obj):
    obj.demo()

obj1 = A()
obj2 = B()
obj3 = C()

poly(obj1)
poly(obj2)
