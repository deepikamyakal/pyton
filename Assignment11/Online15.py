'''
15. Mini Project: Online Payment System
**Question:**
Simulate payment system:

* Input card number
* Input amount
* Raise custom exceptions for:

  * Invalid card number (length not 16)
  * Insufficient balance
  * Invalid amount (non-numeric)

Use:

* try
* multiple except
* else
* finally
* custom exceptions

Expected Output Example:
Payment successful.
Transaction completed.
OR
InvalidCardError: Card number must be 16 digits.
Transaction completed.
'''
class InvalidCardError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

balance = 10000

try:
    card_number = input("Enter card number: ")

    if len(card_number) != 16 or not card_number.isdigit():
        raise InvalidCardError("Card number must be 16 digits.")
    
    amount = float(input("Enter amount: "))

    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    
except ValueError:
    print("Invalid amount. Enter numeric value.")

except InvalidCardError as e:
    print("InvalidCardError:",e)

except InsufficientBalanceError as e:
    print("InsufficientBalanceError:", e)

else:
    balance -= amount
    print("Payment successful")
    print("Remaining Balance:", balance)

finally:
    print("Transaction completed.")
    
