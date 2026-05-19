# Recursion : A function which calls itself, recursive function.
# instead of sloving the whole problem at a time , 
# it sloves a small part and calls itself for the remaining part
 
def sample():
    name = "rocky"
    print(name)

sample()
sample()


# Factorial --> 5! ---> 5*4*3*2*1 = 120

n=8
res=1
for i in range(1,n+1): # 8*7*6*5*4*3*2*1
   res = res*i

print(8*7*6*5*4*3*2*1)

'''
def functionName():
    if base condition :  # when this recursion should stop 
        return result
    else:
        return functionName(small part of problem)

'''

def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n-1)

print(Factorial(5))
print(Factorial(8))




