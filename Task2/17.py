# 17. Program to Calculate Electricity Bill
'''
**Problem Statement:** Write a program to calculate electricity bill based on units consumed.
(Example logic: <100 Low, 100–200 Medium, >200 High)

**Test Cases:**
• Test Case 1:
Input: units = 50
Expected Output: Low Bill
'''
 
units = int(input("Enter the Units :"))
if units < 100:
    print("Low Bill")
elif units <= 200:
    print("Medium Bill")
else:
    print("High Bill")