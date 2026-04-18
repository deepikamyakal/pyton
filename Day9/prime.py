num = int(input("Enter any no :"))
count = 0
for i in range (1,num+1):
    if num % i == 0:
        count += 1

if count == 2:
    print(num,"is a prime no")
else:
    print(num,"is not a prime no")