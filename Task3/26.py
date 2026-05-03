# 26. Program to Check Prime Number
'''
**Problem Statement:** Write a program to check whether a given number is prime.

**Test Cases:**
• Test Case 1:
Input: number = 7
Expected Output: Prime
'''
num = int(input("Enter any no :"))
count = 0
for i in range (1,num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print("prime no")
else:
    print(" not prime no")