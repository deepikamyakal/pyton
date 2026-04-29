# OOPs ---> Object Oriented Programming System

class Employee:
    name = "Deepika"
    salary = 50000

obj = Employee()
print(obj.name)         # Deepika
print(obj.salary)       # 50000

obj1 = Employee()
print(obj1.name)         # Deepika
print(obj1.salary) 

obj2 = Employee()
obj2.name = "Pavan"
print(obj2.name)         # Pavan
print(obj2.salary)


print()

class Student:
    name = "Deepu"
    roll_no = 29
    marks = 84

    def function():
        name = "Deepu"
        roll_no = 29
        marks = 84
        print("Congratualtions", name)
    function()

st = Student()
print(st.name)
print(st.roll_no)