# 32. Program to Count Vowels in a String
'''
**Problem Statement:** Write a program to count the number of vowels in a given string.

**Test Cases:**
• Test Case 1:
Input: string = hello
Expected Output: 2
'''
string = input("Enter string :")

count = 0
vowels  = "aeiouAEIOU"

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels :", count)