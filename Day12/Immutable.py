#  STRING IMMUTABILITY
s = "Python"
print(id(s))        # 2158367412064
print()

s = s + "3"
print(id(s))        # 2158367714224
print()

a = "Deepika"
print(a)            # Deepika
a = a+" Heroine "   # Deepika Heroine
print(a)
print()

msg = "Welcome to Python"
print(len(msg))         # 17
print()

text = "PythoN"
print(text.upper())     # PYTHON
print(text.lower())     # python
print()

sentence = "python programming language"
print(sentence.capitalize())            # Python programming language
print(sentence.title())                 # Python Programming Language
print()

fruits = "apple banana mango deepika"
print(fruits.split(" "))                # ['apple', 'banana', 'mango', 'deepika']

# reverse of a string 
name = "DjTillu"        
rev = " "
for char in name:
    rev = char + rev
print(rev)                  # ulliTjD

username = "Deepika Myakal"
for i in username:
    print(username[-1])         # l continuously print 14 times

print()
# Ex : Iterate Using Index
text = "Python"
for i in range(len(text)):
    print(text[i])

print()
name = "Deepika"
age = 24
print("My name is {} and age is {}".format(name, age))  # My name is Deepika and age is 24

