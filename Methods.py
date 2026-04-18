# 1. Case Conversion Methods
# capitalize() ---> Makes first letter uppercase, rest lowercase
s = "hello WORLd"
print(s.capitalize())          # Hello world

# casefold() ---> Converts string to lowercase (more powerful than lower)
a = "HELLO World"
print(a.casefold())             #hello world

# lower() ---> Converts all characters to lowercase
print("HELLO".lower())          # hello

# upper() ---> Converts all characters to uppercase
print("hello".upper())          # HELLO

# swapcase() ---> Changes lowercase → uppercase and vice versa
print("HeLlO".swapcase())       # hElLo

# title() ---> Makes first letter of each word uppercase
print("hello world".title())     # Hello World


# 2. Alignment Methods 
# center --->  Places string in center
print("hii".center(10,"-"))             # ---hii----
print("Deepika".center(18,"*"))         # *****Deepika******

# ljust(width, char) ---> Aligns left
print("Hii".ljust(10,"+"))              # Hii+++++++
print("Deepika".ljust(18,"_"))         # Deepika___________

# rjust(width, char) ---> Aligns right
print("Hii".rjust(10,"+"))              # +++++++Hii
print("Deepika".rjust(18,"_"))          # ___________Deepika


#  3.Searching Methods
# find() ---> Returns index position, -1 if not found
print("star".find("r"))                 # 3
print("hello".find("r"))                # -1

# index() --->  Same as find but gives error if not found
print("hello".index("o"))                # 4

# rfind() --->  Finds from right side
print("Hello".rfind("h"))               # -1
print("Hello".rfind("e"))               # 1

# rindex() ---> Same as rfind but gives error if not found
print("hello".rindex("l"))              # 3


# 4. Checking Methods (True/False)
# isalnum() ---> Checks letters + numbers only
print("abc123".isalnum())               # True
print("abc123@".isalnum())              # False

# isalpha() ---> Only alphabets
print("abc".isalpha())                  # True
print("98abc".isalpha())                # False

# isdigit() ---> only digits
print("123".isdigit())                  # True
print("123ab".isdigit())                # False

# isdecimal() / isnumeric() ---> Checks numeric values
print("12.2".isdecimal())               # F
print("1234".isdecimal())               # T

# islower() ---> All letters lowercase
print("HELLO".islower())                # F
print("hello".islower())                # T

# isupper() ---> All letters uppercase
print("HELLO".isupper())                # T
print("hello".isupper())                # F

# isspace() ---> Only spaces
print(" ".isspace())                    # T
print("".isspace())                     # F

# istitle() ---> Checks title format
print("Hello World".istitle())          # T
print("hello World".istitle())          # F

# isascii() ---> Checks ASCII characters
print("abc".isascii())                  # T
print("@$%".isascii())                  # T
print("123@a".isascii())                # T

# isidentifier() ---> Valid variable name or not
print("var1".isidentifier())            # T
print("var@".isidentifier())            # F

# isprintable() ---> No hidden characters
print("ghhh".isprintable())             # T


# 5.Replace & Count
# replace(old, new) ---> Replaces text
print("hello".replace("l","L"))         # heLLo

# count(value) ---> Counts occurrences
print("hello".count("l"))               # 2
print("hello".count("5"))               # 0
print("hello".count("o"))               # 1


# 6. Split & Join
# split() ---> Converts string → list
print("A,b,c".split(","))               # ['A', 'b', 'c']

# rsplit() ---> Split from right

# splitlines() ---> Splits by new line

# join() ---> Joins list → string
print("=".join(["a","b","c"]))          # a=b=c


# 7. Strip Methods
# strip() ---> Removes spaces from both sides
print(" hii ".strip())                   # hii

# lstrip() / rstrip() ---> Removes left / right spaces


# 8. Start & End Check
# startswith() ---> checks starting text
print("hello".startswith("he"))         # T
print("hello".startswith("ol"))         # F

# endswith() ----> Checks ending text
print("hello".endswith("lo"))           # T
print("hello".endswith("ge"))           # F


# 9. Partition Methods
# partition() ---> Splits into 3 parts
print("hello-world".partition("-"))         # ('hello', '-', 'world')

# rpartition() ---> Same but from right
print("heelo*world".rpartition("-"))         # ('', '', 'heelo*world')


# 10. Formatting
# format() ---> Inserts values
print("My name is {}".format("Deepika"))     # My name is Deepika

# format_map() ---> Uses dictionary
person = {'name': 'Deepika','age':24}
result = "Name: {name}, Age: {age}".format_map(person)
print(result)       # Name: Deepika, Age: 24


# 11. Other Methods
# expandtabs() ---> Controls tab space
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))
'''
H       e       l       l       o
H       e       l       l       o
H e l l o
H   e   l   l   o
H         e         l         l         o

'''

# encode() ---> Converts to bytes
text = "Hello"
encoded_data = text.encode()
print(encoded_data)             # b'Hello'

# maketrans() + translate() ---> Replace characters using table
txt = "Hello Deep!"
mytable = str.maketrans("D", "P")
print(txt.translate(mytable))           # Peep

# zfill() ---> Adds zeros in front
print("5".zfill(5))         # 00005


