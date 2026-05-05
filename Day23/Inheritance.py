# Inheritance :- ability to use methods and attributes fron one class to another class.

class A:
    def sample(self):
        print("Class A")

class B(A):
    def demo(self):
        print("Class B")

obj = B()
obj.demo()      # class B
obj.sample()    # class A

o = A()
o.sample()
#o.demo() ---> cannot access