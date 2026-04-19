# 6.Write a program to reverse a number using a while loop.

# input from user (example: 1234)
num = int(input("Enter a number :"))

# This variable will store the reversed number
rev = 0

#Loop runs until the number becomes 0
while num != 0:
    digit = num % 10          # % 10 gives last digit Example: 1234 % 10 = 4
    rev = rev * 10 + digit    # Multiply rev by 10 and add digit
                              # Example: rev = 0 → (0*10 + 4) = 4,  next: (4*10 + 3) = 43
    num = num // 10           # Removes last digit, Example: 1234 → 123

print("Reversed number:", rev)  


'''
Enter a number :1234
Reversed number: 4321

Step	num	    digit	rev
1	    1234	4	    4
2	    123	    3	    43
3	    12	    2	    432
4	    1	    1	    4321

Loop ends when num = 0
'''