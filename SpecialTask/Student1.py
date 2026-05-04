# 1. Program to Create a Student Management System
'''
**Problem Statement:**
Write a program to create a `Student` class. The constructor should initialize student name, roll number, and marks. Create methods to display student details and calculate grade based on marks.

**Task Requirements:**

* Use constructor to initialize values
* Create at least 2 methods
* Create multiple student objects

**Test Cases:**
• Test Case 1:
Input: name = Sairam, roll = 101, marks = 85
Expected Output:
Name: Sairam, Roll: 101, Grade: B
'''

class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
    def Calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 50:
            return 'C'
        else:
            return 'Fail'
        
    def display(self):
        grade = self.Calculate_grade()
        print(f"Name:{self.name}, Roll:{self.roll}, Grade:{grade}")

s1 = Student("Sairam", 101, 85)
s2 = Student("Ravi", 102, 95)
s3 = Student("Anu", 103, 40)

s1.display()
s2.display()
s3.display()