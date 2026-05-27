# Advance python

# iterator
# generator
# Decorators

# used in 
# data science 
# API's
# Backend systems 
# frameworks 
# memory optimization 

# Iterators : 

# __iter__()  ---> return iterator  
# __next__() ---> it will fetch next element / value

l = ["deepika","sairam","sumit","sai"]
it = iter(l)
for i in l:
    print(next(it))

# Generators : it is a special function that returns the values one by one using yield keyword 

def gene():
    for i in range(10):
        yield i

res = gene()
for value in range(10):
    print(next(res)) 

#
def numbers():
    yield "sai"
    yield 1
    yield 2
    yield 3
    yield 4

for i in numbers():
    print(i)