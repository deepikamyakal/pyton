# STRING METHODS
## Case Conversion Methods

# Ex 1 : 'upper()' and 'lower()'
text = "Python"
print(text.upper())         # PYTHON
print(text.lower())         # python

print()
# Ex 2 : `capitalize()` and `title()`
sentence = "Python is Programming language"
print(sentence.capitalize())        # # first word first letter will beconme capital (upper)
print(sentence.title())

print()
# Whitespace & Replace Methods
# Ex 3 : 'strip()'
email = "admin@gmail.com"       
print(email.strip())            # admin@gmail.com

print()
# Ex 4 : 'replace()'
msg = "I love Ruby"
print(msg.replace("Ruby","Python"))     # I love Python

print()
# Ex 5 : `find()` and `count()`
data = "Python is easy"
print(data.find("is"))          # 7
print(data.count("o"))          # 1

print()
# Ex 6 : 'split()'
fruits = "apple,banana,mango"
print(fruits.split(","))        # ['apple', 'banana', 'mango']

print()
## Real-Time Example: Email Validation
email1 = "test@gmail.com"

if "@" in email1 and "." in email1:
    print("Valid Email")
else:                                   # Valid Email
    print("Invalid Email")

print()
# INDEXING IN STRINGS
# What is Indexing?
# Accessing characters using **position numbers**.
# Index starts from **0**

# Ex 1 : Positive Indexing
word = "Python"
print(word[0])      # P
print(word[4])      # o

print()
# Ex 2 : Negative Indexing
print(word[-1])     # n
print(word[-4])     # t

print()
# Ex 3 : First and Last Character
name = "Deepika"
print(name[0])      # D
print(name[-2])     # k

print()
# Ex 4 : Iterate Using Index
text1 = "Python"
for i in range(len(text1)):
    print(text1[i])               
    #print(text1[i], end = " ")      # P y t h o n
    #print(text1[i], end = "")       # Python

print()
# Ex 5 : Character Validation
password = "Admin123"
print(password[0].isupper())        # True

print()
# Ex 