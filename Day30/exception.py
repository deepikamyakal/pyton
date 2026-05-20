# Exception handling in python 

# Errors ---> which are made by programmer

# logical errors 
# syntax errors 
# complietime errors 

# Runtime errors ---> mistakes

age = int(input("Enter a number:"))
after10 = age + 10
print(after10)

a = 10
b = 5
try:
    res = a/b
    print(res)

except Exception as e:
    print("zero division error",e)

print("End of the program")

# try block  ---> logic where there is a chance of getting an error 
# except block ---> leave it as an exception 
'''
a = int(input("Enter a value :"))
b = int(input("Enter B value :"))
res = a/b
print(res)
'''

try:
    a = int(input("Enter a value :"))
    b = int(input("Enter B value :"))
    res = a/b
    print(res)

except ZeroDivisionError as zde:
    print(zde)

except ValueError as ve:
    print(ve)

except Exception as y:
    print("Unexpected error",y)

finally:
    print("End of the program")
