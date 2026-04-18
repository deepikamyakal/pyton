# 9.Write a program to remove leading and trailing spaces from a string.

s = input("Enter a String :")

result = s.strip()          # strip() removes spaces from start and end only
print("After removing spaces :", result)


'''
Enter a String :      hello world
After removing spaces : hello world
'''