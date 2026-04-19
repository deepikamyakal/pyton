# 6.Write a program to print a square pattern of stars of size N:
'''
****
****       
****
****
'''
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# ************************************
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


'''
* * * *
* * * *       
* * * *
* * * *
'''

