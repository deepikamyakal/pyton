# 5.Create a dictionary with employee details (id, name, salary).
# Perform:
# a)Add a new key
# b)Update salary
# c)Delete a key


emp = {"id":101, "name" :"Deepika", "salary":25000}

emp["department"] = "IT"

emp["salary"] = 30000

del emp["id"]

print(emp)