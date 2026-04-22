# *args argument

def total(*args):
    return sum(args)

print(total(20,60,96,10))       # 186


def employee(name, *rating):
    return f"{name} : {max(rating)}"

print(employee("Deepika",8,9,7,63))     # Deepika : 63
print(employee("Pavan",80,9,7,63))      # Pavan : 80


def student(rollno, *marks):
    return f"{rollno} : {max(marks)}"

print(student("11",98,89,78))       # 11 : 98 
