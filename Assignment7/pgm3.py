# 3.Write a program to reverse a given number using a loop.
# Example: Input → 1234, Output → 4321

num = int(input("Enter a number: "))

rev = 0

while num != 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number:", rev)