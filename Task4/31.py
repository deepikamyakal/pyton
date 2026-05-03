# 31. Program to Check Palindrome String
'''
**Problem Statement:** Write a program to check whether a given string is a palindrome (same forward and backward).

**Test Cases:**
• Test Case 1:
Input: string = madam
Expected Output: Palindrome
'''

string = input("Enter string :")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")