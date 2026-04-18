# STRING FORMATTING (**)
## Method 1: `format()`

# Ex 1 : 
name = "Deepika"
age = 25            # My name is Deepika and age is 25
print("My name is {} and age is {}".format(name,age))

print()
# Ex 2 : Positional Formatting
print("Name: {0}, Age: {1}".format(name,age))   # Name: Deepika, Age: 25

print()
# Ex 3 : Named Formatting
print("Name: {n}, Age: {a}".format(n=name,a=age))    # Name: Deepika, Age: 25

print()
## Method 2: f-Strings (MOST USED)

# Ex 4 : Simple f-String
print(f"My name is {name} and age is {age}")     # My name is Deepika and age is 25

print()
# Ex 5 :  Real-Time Invoice
item = "Laptop"
price = 55000
qty = 2
print(f"Item: {item}")
print(f"Total Amount: {price * qty}")
# Output 
#Item: Laptop
#Total Amount: 110000