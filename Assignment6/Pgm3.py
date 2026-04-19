# 3.Write a program to calculate the sum of first N natural numbers using a while loop.

num = int(input("Enter a number :"))

sum = 0
i = 1

while i <= num:
    sum = sum + i
    i = i + 1

print("Sum is :", sum)


'''
Enter a number :10
Sum is : 55
'''