# private access specifiers : data can be accessed by only the superclass 
# (__) double underscore 
#if you want to access private data then you can only access through methods of super class  
# we can not access the private data through objects 


class Parent:   # super class
    __privatedata = "Deepika"
    def privatemethod(self):
        print(self.__privatedata)

class Child(Parent):   # subclass 0r derived class
    def method(self):
        print(self.__privatedata)


obj=Parent()
obj.privatemethod()
# print(obj.__privatedata)

obj1=Child()
obj1.method()