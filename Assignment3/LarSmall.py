# 2)Write a program to find the largest and smallest elements in a list without using built-in functions.

numbers = [29,31,89,65,74]   # define list first

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)