# Patterns Program
# *
# * *
# * * *
# * * * * Left triangle

for i in range(1,5):
    print("*" * i) #without space

for i in range(1,5):
    print(" * " * i) # with space

# Nested for loop
for i in range(1,5):
    for j in range(i):
        print("*", end=" ")
    print()

print()
# Reverse left Triangle
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
for i in range(5,0,-1):
    print(" * " * i)

print()

# Right Triangle
#      *
#     **
#    ***
#   ****

for i in range(1,5):
    print(" " * (4-i) + "*" *i)

print()

# Pyramid 
#    *
#   ***
#  *****
# *******
for i in range(1,5):
    print(" " * (4-i) + "*" * (2*i-1))

print()


# *
# ***
# ******
# **********
for i in range(1,5):
    for j in range(1, i+1):
        print("*" * j, end="")
    print()

print()

# ****
# ****
# ****
# ****
for i in range(4):
    for j in range(4):
        print("*", end="")
    print()

print("Out of the loop")
print()




