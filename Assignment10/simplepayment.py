# 3. Simple Payment System
'''
**Concepts Covered:**
Abstraction, Method Overriding

### Problem Statement

In modern applications such as e-commerce platforms, users can pay using multiple payment methods such as **Credit Card, Debit Card, UPI, or Net Banking**.

Create a payment processing system using **Object-Oriented Programming concepts**.

### Requirements

1. Create an **abstract base class** named `Payment`.
2. Define an abstract method called `pay()`.
3. Create multiple child classes such as:

   * `CreditCardPayment`
   * `UPIPayment`
4. Each child class must **override** the `pay()` method and implement its own payment logic.

### Implementation Guidelines

* Use Python’s `abc` module for creating abstract classes.
* Ensure every subclass implements the `pay()` method.
* Demonstrate polymorphism by calling the same method on different objects.

### Expected Outcome

The system should simulate processing payments using different payment methods.

'''

from abc import ABC, abstractmethod

class Payment(ABC):
    
   @abstractmethod
   def pay(self, amount):
      pass

class CreditCardPayment(Payment):

   def pay(self, amount):
      print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):

   def pay(self, amount):
      print(f"Paid {amount} using UPI")

c1 = CreditCardPayment()
u1 = UPIPayment()

c1.pay(5000)
u1.pay(2500)
