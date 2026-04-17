# Identity Op
l = [1,2,3,4]
p = [1,2]
print(p is l)       # F

l = [1,2,3,4]
p = [1,2]
print(p is not l)   # T

# Membership Op
names = ["Deepika","Anu","Ashu","Aish"]
print("Anu" in names)           # T
print("Saee" not in names)      # T
print("xyz" in names)           # F

for i in range(0,5):
    print(i)            # 0 1 2 3 4


# Bitwise Op
a = 10
print(~ a)      # -11
print(a>>1)     # 5
print(bin(a))   # 0b1010

a = 5
print(a<<1)     # 10
print(bin(a))   # 0b101

b = 3
print(bin(b))   # 0b11
print(a^b)      # 6

a & b
a|b
print(a & b)     # 1
print(a|b)       # 7

# Operator Precedence
print((9+3)-(9+3))      # 0
print(10+5*3)           # 25
print(100 + ~3)         # 96
print(100 + 5 * 3)      # 115
print(100 - 5 * 3)      # 85
print(8 >> 4 - 2)       # 2
print(6 & 2 + 1)        # 2
print(6 ^ 2 + 1)        # 5
print(6 | 2 + 1)        # 7
print(5 == 4 + 1)       # True
print(not 5 == 5)       # False
print(1 or 2 and 3)     # 1
print(4 or 5 + 10 or 8) # 4



