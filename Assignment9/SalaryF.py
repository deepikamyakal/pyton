# 13. Filter High Salary Employees
'''
*Question:**
Given a list of salaries, filter salaries above 50,000.

**Test Case 1:**
Input:
[30000, 60000, 45000, 80000]

Expected Output:
[60000, 80000]
'''
salaries = [30000, 60000, 45000, 80000]
high_sal = list(filter(lambda x: x >= 50000, salaries))
print(high_sal)
