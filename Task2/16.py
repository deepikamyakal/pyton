# 16. Program to Identify Vowel or Consonant
'''
Problem Statement:** Write a program to check whether a character is a vowel or consonant.

**Test Cases:**
• Test Case 1:
Input: char = a
Expected Output: Vowel
'''

char = input("Enter your character :")

char = char.lower()

if char in ['a','e','i','o','u']:
    print("Vowel")
else:
    print("Consonent")


# 
ch = input("Enter char: ").lower()
print("Vowel" if ch in "aeiou" else "Consonant")