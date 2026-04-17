#Arithmetic Operator
a = 10
print(a%2)  #0
print(a/2)  #5.0
print(a/3)  #3.333333
print(a//3) #3
print(3**2) #9

#Relational Op
x = 100
y = 99
print(x==y)     # F
print(x!=y)     # T  
print(x>y)      # T 
print(x<y)      # F
print(x>=y)     # T
print(x<=y)     # F

#Logical Op
age = 30
print(age > 18 and age <= 30)       # T

age = 36
print(age < 35 or age > 40)         # F

b = True                            # F
print(not b)

#Assignment operator
c = 20
c += 10
c = c + 10
c -= 10
print(c)        # 30