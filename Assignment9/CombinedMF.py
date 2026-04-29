## 15. Combined Example (map + filter)
'''
**Question:**
Given a list of numbers:

* First filter even numbers
* Then square them using map()

**Test Case 1:**
Input:
[1,2,3,4,5,6]

Expected Output:
[4,16,36]
'''

num = [1,2,3,4,5,6]

result = list(map(lambda x: x * x , filter(lambda x : x % 2 == 0, num)))

print(result)