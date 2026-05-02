# 8. Program to Convert Minutes to Hours and Minutes
'''
**Problem Statement:** Write a program to convert total minutes into hours and remaining minutes.

**Test Cases:**
• Test Case 1:
Input: minutes = 130
Expected Output: 2 hours 10 minutes
'''

minutes = int(input("Enter total minutes :"))

hours = minutes // 60
remaining_min = minutes % 60

print(hours,"hours", remaining_min,"minutes")