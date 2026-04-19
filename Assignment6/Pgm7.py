#  7.Write a program to print the following pattern using nested loops:
'''
*
* *
* * *
* * * *
* * * * *
'''

for i in range(1,6):
    for j in range(i):
        print("*", end =" ")
    print()
print()