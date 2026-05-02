# 2. Program to Calculate Employee Salary with Bonus
'''
Problem Statement: Write a program to calculate the final salary of an employee 
by adding a 10% bonus to the base salary.

**Test Cases:**
• Test Case 1:
Input: salary = 10000
Expected Output: 11000
'''

sal = int(input("Enter your Salary:"))

bonus = sal * 0.10

final_sal = sal + bonus

print("Final Salary :", int(final_sal))