# Multi Level Inheritance ---> Grandfather --> father --> child

class GrandFather:
    def method1(self):
        print("This is parent class")

    def display(self):
        print("This is GrandFather display class")

class Father(GrandFather):
    def method2(self):
        print("This is parent class")

    def display(self):
        print("This is father display class")

class Child(Father):
    def demo(self):
        print("This is child class")

c = Child()
c.method1()     # This is parent class
c.display()     # This is father display class

c.method2()     # This is parent class

c.demo()        # This is child class
