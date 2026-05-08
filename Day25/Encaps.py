# Encapsulation in python : wrapping up data(variables) and methods in a single unit called class and restricting direct access 
# means Data Hiding --> we protect some important from direct modification 

# why ?? 
# data security 
# controlled access : allows access only through methods 
# prevent accidental changes : others can not modify important data directly 


class Sample:
    name = "Deepika"
    def demo(self):
        print("This encapsulation")

class A():
    def method(self):
        print("Cannot access directly")

obj = A()
obj.demo()