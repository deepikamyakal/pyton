# 10.Write a program to check whether a string contains only digits using string methods.

s = input("Enter a String :")

if s.isdigit():
    print("Only digits")
else:
    print("Not Only digits")


'''
Enter a String :1234
Only digits

Enter a String :svf45
Not Only digits
'''