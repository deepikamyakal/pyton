num = int(input("enter any no :"))
count = 0
i = 1
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print(num,"is a prime no")
else:
    print(num,"is not a prime")
    