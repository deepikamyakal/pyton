# 9. Filter Students with Passing Marks
'''
**Question:**
Given a list of marks, filter students who scored 50 or above.

**Test Case 1:**
Input:
[45, 67, 80, 30, 55]

Expected Output:
[67, 80, 55]
'''
marks = [45,67,80,30,55]

passed = list(filter(lambda x: x >= 50, marks))

print(passed)