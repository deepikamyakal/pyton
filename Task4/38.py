# 38. Program to Merge Two Lists
'''
**Problem Statement:** Write a program to merge two lists into one list.

**Test Cases:**
• Test Case 1:
Input: list1 = [1, 2], list2 = [3, 4]
Expected Output: [1, 2, 3, 4]
'''


list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

merged_list = list1 + list2

print("Merged List:", merged_list)