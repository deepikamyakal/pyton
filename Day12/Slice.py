# SLICING IN STRINGS
# Syntax
# string[start : end : step]

# Ex 1: Basic Slicing
word = "Python"
print(word[1:5])        # ytho

print()
# Ex 2 : Omit Start / End
print(word[:4])         # Pyth
print(word[3:])         # hon

print()
# Ex 3 : Negative Slicing
print(word[-5:-1])      # ytho

print()
# Ex 4 : Step Value
print(word[::3])        # Ph

print()
# Ex 5 : Reverse String
print(word[::-1])       # nohtyP

print()
# Ex : Mask Account Number
acc = "123456789012"
print("***********" + acc[-4:])        # ***********9012


