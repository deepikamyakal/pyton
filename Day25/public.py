# Access specifiers 
# 1) public access specifiers  : 

class Parent:
    publicdata = "deepika"
    def publicmethod(self):
        print(self.publicdata)

class Child(Parent):
    def method(self):
        print(self.publicdata)

obj = Parent()
print(obj.publicdata)
obj.publicmethod()

obj1 = Child()
obj1.method()
print(obj1.publicdata)