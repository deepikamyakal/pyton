# 8.Write a program to check whether a given number is a prime number using loops.

num = int(input("Enter a number :"))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print("It is prime no") 
else:
    print("It is not prime no")

'''
Enter a number :4
It is not prime no

Enter a number :13
It is prime no
'''