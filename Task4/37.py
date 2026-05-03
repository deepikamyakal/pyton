# 37. Program to Find Second Largest Number in a List
'''
**Problem Statement:** Write a program to find the second largest number in a list.

**Test Cases:**
• Test Case 1:
Input: list = [1, 2, 3]
Expected Output: 2
'''

lst = list(map(int, input("Enter numbers: ").split()))

unique = list(set(lst))  

if len(unique) < 2:
    print("No second largest element")
else:
    unique.sort()
    print("Second largest:", unique[-2])
