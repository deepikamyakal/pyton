# 3. Program to Build a Product Billing System
'''
**Problem Statement:**
Create a `Product` class where the constructor takes product name, price, and quantity. 
Create a method to calculate total cost and display bill details.

**Task Requirements:**

* Use constructor to initialize attributes
* Create method to calculate total price
* Display formatted output

**Test Cases:**
• Test Case 1:
Input: name = Laptop, price = 50000, qty = 1
Expected Output: Total = 50000
'''
 
class Product:
    
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total(self):
        return self.price * self.qty
    
    def display_bill(self):
        total = self.calculate_total()
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.qty}")
        print(f"Total =  {total}")

P1 = Product("Laptop",50000,1)
P1.display_bill()
        
P2 = Product("Mobile",20000,2)
P2.display_bill()

P3 = Product("Pen",10,5)
P3.display_bill()