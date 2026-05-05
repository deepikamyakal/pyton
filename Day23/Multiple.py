# Multiple Inheritance --> a child class inheriting the properties of two or more parent classes.

class Father:
    def method1(self):
        print("This is parent class")

    def display(self):
        print("This is Father display class")

class Mother:
    def method2(self):
        print("This is parent class")

    def display(self):
        print("This is Mother display class")

class Child(Father, Mother):
    def demo(self):
        print("This is child class")

c = Child()
c.method1()      # This is parent class
c.display()     # This is Father display class
c.demo()        # This is child class
c.method2()     # This is parent class