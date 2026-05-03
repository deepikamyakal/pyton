# 19. Program to Print Numbers from 1 to N
'''
**Problem Statement:** Write a program to print numbers from 1 to N using a loop.

**Test Cases:**
• Test Case 1:
Input: n = 5
Expected Output: 1 2 3 4 5
'''
n = int(input("Enter number :"))
for i in range(1,n+1):
    print(i, end=" ")

print()

# while loop
num = int(input("Enter a number: "))
i = 1

while i <= num:
    print(i, end=" ")
    i += 1