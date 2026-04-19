# 5.Write a program to count the number of digits in a given number using a loop.

num = int(input("Enter a number :"))

count = 0

while num != 0:
    num = num // 10
    count = count + 1

print("Number of Digits", count)


'''
Enter a number :123456
Number of Digits 6
'''