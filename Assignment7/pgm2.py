# 2.Write a program to find the sum of all even numbers between 1 and N using a loop.

n = int(input("Enter a no :"))
sum = 0

for i in range(2,n+1,2):
    sum = sum + i
print("Sum of even nos:", sum)


'''
Enter a no :12
Sum of even nos: 42
'''











