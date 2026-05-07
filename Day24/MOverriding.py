# Method Overriding :- subclass methods overrided by parent class methods 

class parent:
    def method1(self,name):
        print(name)
        print("This is parent class")

    def display(self):
        print("This is child1 class")

class child(parent):
    def method1(self,salary):
        print(salary)
        print("This is child2 class")

c = child()
c.method1("deepika")
c.method1(50000)
c.display()