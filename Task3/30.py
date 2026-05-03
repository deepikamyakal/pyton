# 30. Program to Reverse a String using Loop
'''
**Problem Statement:** Write a program to reverse a given string without using built-in reverse functions.

**Test Cases:**
• Test Case 1:
Input: string = hello
Expected Output: olleh
'''

string = input("Enter string :")

rev = "" 

for ch in string:
    rev = ch + rev

print("Reversed string :", rev)