## SECTION 3: map()
'''
6. Square All Numbers Using map()

**Question:**
Given a list of numbers, use map() to return a list of squares.

**Test Case 1:**
Input:
[1, 2, 3, 4]

Expected Output:
[1, 4, 9, 16]
'''
n = [1,2,3,4]
squares = list(map(lambda x: x *x,n))
print(squares)
