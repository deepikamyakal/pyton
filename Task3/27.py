# 27. Program to Print Prime Numbers in a Range
'''
**Problem Statement:** Write a program to print all prime numbers between two given numbers.

**Test Cases:**
• Test Case 1:
Input: start = 1, end = 10
Expected Output: 2 3 5 7
'''

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")