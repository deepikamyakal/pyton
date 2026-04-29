# SECTION 6: PRACTICAL REAL-TIME EXAMPLES
## 12. Apply 10% Discount Using map()
'''
**Question:**
Given a list of prices, apply 10% discount to each price.

**Test Case 1:**
Input:
[100, 200, 300]

Expected Output:
[90.0, 180.0, 270.0]
'''

price = [100,200,300]
discount = list(map(lambda x: x * 0.9, price))
print(discount)