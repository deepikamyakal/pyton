## 7. Convert Strings to Uppercase Using map()
'''
**Question:**
Convert a list of names to uppercase using map().

**Test Case 1:**
Input:
["sairam", "anjali", "rahul"]

Expected Output:
["SAIRAM", "ANJALI", "RAHUL"]
'''

name = ["sairam", "anjali", "rahul"]

uppercase_names = list(map(lambda x: x.upper(), name))

print(uppercase_names)