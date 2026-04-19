# 6.Write a program to check whether a given string is a palindrome using string methods.

s = input("Enter a String :")

if s == s[::-1]: # [::-1] means reverse the string
    print("Palindrome")
else:
    print("Not a Palindrome")


'''
Enter a String :hello
Not a Palindrome

Enter a String :madam
Palindrome
'''