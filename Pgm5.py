# 5.Write a program to find the length of a string without using the len() function
# (Hint: use a string method).

text = input("Enter a string: ")

length = 0
for ch in text:
    length += text.count(ch) // text.count(ch)

print("Length of string:", length)

'''
Output
Enter a String:hello world
Length of a string : 11
'''