## SECTION 4: filter()
'''
## 8. Filter Even Numbers

**Question:**
Use filter() to extract even numbers from a list.

**Test Case 1:**
Input:
[1,2,3,4,5,6]

Expected Output:
[2,4,6]
'''

num = [1,2,3,4,5,6]
even_no = list(filter(lambda x: x % 2 == 0, num))
print(even_no)