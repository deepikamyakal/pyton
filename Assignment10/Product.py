# 6. Product Price Calculator
'''
**Concepts Covered:**
Functions, Default Arguments, Keyword Arguments

### Problem Statement

E-commerce platforms often calculate product prices by applying taxes and discounts.

Create a price calculator that determines the final product price after applying tax and discount.

### Requirements

1. Create a function named `calculate_price()`.
2. Accept the following parameters:

   * Product price
   * Tax percentage (default value)
   * Discount amount (optional)
3. Allow users to pass arguments using **keyword arguments**.

### Implementation Guidelines

* Use default parameters for tax and discount.
* Compute the final price using arithmetic operations.

### Expected Outcome

The function should return the **final price after tax and discount calculations**.
'''

def calculate_price(price, tax=18, discount=0):
   
   tax_amount = (price * tax) / 100

   final_price = price + tax_amount - discount

   return final_price

result = calculate_price(
   price=1000,
   tax=18,
   discount=100
)

print("Final Price :", result)
