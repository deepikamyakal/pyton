# 6.Write a program to check whether a given value exists in a list using membership operators.

list = [10,30,50,70]
num = int(input("Enter number :"))

if num in list:
    print("Exists in list")
else:
    print("Not in list")