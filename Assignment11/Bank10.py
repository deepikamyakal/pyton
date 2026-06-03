'''
 10. Bank Minimum Balance Exception

**Question:**
Create custom exception:

```
MinimumBalanceError
```
If withdrawal makes balance < 1000 → raise exception.
'''
class MinimumBalanceError(Exception):
    pass
balance = 5000
try:
    amount = int(input("Enter withdrawal amount: "))

    if balance - amount < 1000:
        raise MinimumBalanceError("Minimum balance of 1000 must be maintained.")
    
    balance -= amount
    print("Remaining Balance:", balance)

except MinimumBalanceError as e:
    print("MinimumBalanceError:", e)

