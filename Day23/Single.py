# Single Inheritance :

class Parent:
    def method(self):
        print("This is parent class")

    def display(self):
        print("This is parent display class")

class Child(Parent):
    def demo(self):
        print("This is child class")

c = Child()
c.method()          # This is parent class
c.display()         # This is parent display class
c.demo()            # This is child class

