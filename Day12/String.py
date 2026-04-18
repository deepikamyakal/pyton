# Strings
## What is a String?
# A "string" is an immutable sequence of Unicode characters.

name = "Deepika"
city = "Solapur"

# **Immutable** → once created, it cannot be changed.

## Real-Time Uses

# User names
# Emails
# Passwords
# File paths
# API responses
# Messages & logs

# Ex 1 : User Name Storage
username = "Deepika"        # Deepika
print(username)

print()
# Ex 2 : Multiline String
address = """ Solapur
Maharashtra
India """
print(address)

print()
# Ex 3 : Length of String
msg = "Welcome To Python"       # 17
print(len(msg))

print()
# Ex 4 : Accessing a Character
language = "Python is my Favourite language."
print(language[0])          # P
print(language[-1])         # .

print()
# Ex 5 : Immutability Proof
s = "Hello"
s = s + " World "
print(s)                    # Hello World
