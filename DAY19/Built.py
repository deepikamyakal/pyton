# fliter() ---> filters the output according to the logic
# find the even nos

num = [1, 4, 9, 16, 25, 36, 58, 89, 99, 100]
even_number = list(filter(lambda a: a % 2==0,num))
print(even_number)          # [4, 16, 36, 58, 100]



# reduce() ---> takes collection data as input and gives a single output
# sum of number
from functools import reduce

numbers = [10,30,44,87,96,56,78,100]
result = reduce(lambda a,b : a+b,num)
print(result)       # 437
