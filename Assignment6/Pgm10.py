# 10.Write a program to find the factorial of a given number using a loop.

num = int(input("Enter a no:"))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial is:", fact)

'''
Enter a no:5
Factorial is: 120

Factorial means:
5! = 5 × 4 × 3 × 2 × 1 = 120
Loop multiplies numbers from 1 to num

0! = 1 (factorial of 0 is 1)

'''