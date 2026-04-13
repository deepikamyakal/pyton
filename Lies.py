# 4.Write a program to check whether a number lies between 10 and 50 using logical operators.

num = int(input("Enter number :"))

if num >= 10 and num <= 50:
    print("Number lies between 10 and 50")
else:
    print("Not in range")