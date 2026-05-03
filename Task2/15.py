## 15. Program to Check Palindrome Number
'''
Problem Statement:** Write a program to check whether a number is a palindrome.

**Test Cases:**
• Test Case 1:
Input: number = 121
Expected Output: Palindrome
'''
num = input("Enter your number :")

if num == num[::-1]: 
    print("Palindrome no")
else:
    print("Not Palindrome no")