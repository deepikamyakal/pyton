# 4.Write a program to display the multiplication table of a given number using a for loop.

num = int(input("Enter a number:"))

for i in range(1,11):
    print(num,"x",i,"=",num * i)
    #print(num * i)

'''
print(num,"x",i,"=",num * i)
Enter a number:3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30


#print(num * i)
4
8
12
16
20
24
28
32
36
40
'''