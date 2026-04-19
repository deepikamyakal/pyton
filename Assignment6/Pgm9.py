# 9.Write a program to demonstrate the use of break and continue statements with a loop.

# break → stops the loop
for i in range(1,11):
    if i == 5:
        break
    print(i)

'''
Output :
1
2
3
4
'''

# continue → skips one iteration
for i in range(1,11):
    if i == 6:
        continue
    print(i)

'''
1
2
3
4
5
7
8
9
10
'''