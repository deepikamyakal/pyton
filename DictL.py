# 6.Write a program to iterate through a dictionary and print: Keys, Values ,Key-value pairs.

emp = {"id":101, "name" :"Deepika", "salary":25000}

for k in emp.keys():
    print(k)

for v in emp.values():
    print(v)

for k,v in emp.items():
    print(k,":",v)