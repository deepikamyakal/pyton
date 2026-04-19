# 7.Write a python program to print a complete diamond shape using stars (*) with nested loops.

n = int(input("Enter a number :"))

# Upper part
for i in range(1, n+1):
    print(" "*(n-i) + "*" *(2*i-1))

# Lower part
for i in range(n-1,0,-1):
    print(" "*(n-i) + "*" *(2*i-1))


'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''