# 36. Program to Remove Duplicates from a List
'''
**Problem Statement:** Write a program to remove duplicate elements from a list.

**Test Cases:**
• Test Case 1:
Input: list = [1, 1, 2, 2]
Expected Output: [1, 2]
'''

lst = [1, 1, 2, 2]
result = list(set(lst))
print(result) 