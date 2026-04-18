# 3.Write a program to check whether a given string starts with a specific word using a string method.

text = input("Enter a String:")
word  = input("Enter the word to check:")

if text.startswith(word):
    print("The string starts with the given word")
else :
    print("The string does NOT start with the given word")



'''
Output :
Enter a String:Hello World
Enter the word to check:Hello
The string starts with the given word
'''