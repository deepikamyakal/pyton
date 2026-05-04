# 5. Program to Create a Car Information System
'''
**Problem Statement:**
Create a `Car` class. The constructor should initialize brand, model, and price. 
Create a method to display car details and apply a discount (5%).

**Task Requirements:**

* Use constructor
* Create method to apply discount
* Display updated price

**Test Cases:**
• Test Case 1:
Input: brand = Toyota, model = Innova, price = 2000000
Expected Output: Discounted Price = 1900000
'''

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self):
        discount = self.price * 0.05
        return self.price - discount
    
    def display(self):
        discounted_price = self.apply_discount()
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Original price: {self.price}")
        print(f"Discounted_price = {int(discounted_price)}")

        
C1 = Car("Toyota", "Innova", 2000000)    
C1.display()

C2 = Car("Hyundai", "i20", 800000)    
C2.display()

C3 = Car("Tata", "Nexon", 1000000)    
C3.display()
