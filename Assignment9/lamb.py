# 2. Lambda with Multiple Arguments
'''
**Question:**
Create a lambda function to calculate the total price (price × quantity).

**Test Case 1:**
Input:
total = lambda price, qty: price * qty
total(100, 3)

Expected Output:
300
'''
total = lambda price, qty: price * qty
print(total(100, 3))