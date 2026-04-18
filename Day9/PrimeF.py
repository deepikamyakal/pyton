# First 10 prime numbers program
# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47

num = 2
count = 0
while count < 15:
    i = 1
    factor = 0
    while i <= num:
        if num % i == 0:
            factor += 1
        i += 1
    if factor == 2:
        print(num)
        count += 1
    num += 1