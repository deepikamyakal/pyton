# 4.Write a program to count the number of digits in a given number using a loop.

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count = count + 1

print("Number of digits:", count)

'''
Enter a number: 65789
Number of digits: 5

'''