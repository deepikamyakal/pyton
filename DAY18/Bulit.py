# Built in higher order function

# map() ---> applies function to each and every element in the group of data 

num = [1,2,3,4,5,6]
l = []
for i in num:
    square = i ** 2
    l.append(square)
print(l)                # [1, 4, 9, 16, 25, 36]


num = [1,2,3,4,5,6]

result = list(map(lambda a: a ** 2,num))
print(result)                                   # [1, 4, 9, 16, 25, 36]


# filter()
# reduce()
