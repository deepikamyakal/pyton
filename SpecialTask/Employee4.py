# 4. Program to Create an Employee Salary System
'''
**Problem Statement:**
Create an `Employee` class. The constructor should initialize employee name and basic salary. 
Add a method to calculate salary after adding bonus (10%).

**Task Requirements:**

* Constructor initialization
* Method to calculate updated salary
* Display final salary

**Test Cases:**
• Test Case 1:
Input: name = Sairam, salary = 10000
Expected Output: Final Salary = 11000
'''

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_final_sal(self):
        bonus = self.salary * 0.10
        return self.salary + bonus
         
    def display(self):
        final_salary = self.calculate_final_sal()
        print(f"Name: {self.name} ")
        print(f"final Salary = {int(final_salary)}")

E = Employee("Sairam", 10000)
E.display()

E1 = Employee("Ravi", 20000)
E1.display()

E2 = Employee("Anu", 5000)
E2.display()
        