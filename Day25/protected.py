# protected access specifiers : put (_)underscore before data and method to declare it as protected access sepcifiers  
# they can be access only by the superclass and subclass (subclass which is derived from the superclass) 

class Parent:   # super class
    _protecteddata = "Deepika"
    def protectedmethod(self):
        print(self._protecteddata)

class Child(Parent):   # subclass 0r derived class
    def method(self):
        print(self._protecteddata)


class Sample(Child):   # normal 
    def display(self):
        print()
        print(self._protecteddata)

obj=Parent()
print(obj._protecteddata)
obj.protectedmethod()

obj1=Child()
obj1.method()
print(obj1._protecteddata)

obj2=Sample()
obj2.display()
print(obj2._protecteddata)
obj2.method()    #
