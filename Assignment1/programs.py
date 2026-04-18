# Assignment1

# 1. Program to Calculate the Area of a Circle

radius = float(input("Enter radius: "))
pi = 3.14
area = pi * radius * radius
print("Area of the circle =", round(area, 2))

'''
o/p :-Enter radius: 7
Area of the circle = 153.86
'''
print()
# 2. Program to calculate total cost after discount

price = float(input("Enter original price: "))
discount = float(input("Enter discount %: "))
final_price = price - (price * discount / 100)
print("Final Price =", final_price)

'''
o/p :- Enter original price: 1000
Enter discount %: 20
Final Price = 800.0
'''

print()
# 3. Program to calculate simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", round(simple_interest, 2))

'''
o/p :- Enter principal amount: 1000
Enter rate of interest: 5
Enter time (in years): 2
Simple Interest = 100.0
'''
print()
# 4. Program to Calculate Total Salary

basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

total = basic + hra + da
print("Total Salary =", total)

'''
o/p :- Enter basic salary: 25000
       Enter HRA: 5000
       Enter DA: 3000
       Total Salary = 33000.0
'''

print()
# 5.  Program to Calculate Distance Traveled

speed = float(input("Enter speed: "))
time = float(input("Enter time: "))

distance = speed * time
print("Distance =", distance)

'''
o/p : - Enter speed: 60
Enter time: 2
Distance = 120.0
''' 

print()
# 6. Program to Convert Temperature from Celsius to Fahrenheit

c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)

'''
o/p :- Enter Celsius: 25
Fahrenheit = 77.0
'''
print()
#7 .Program to Find the Maximum of Two Numbers Using Ternary Operator

a = int(input("Enter a: "))
b = int(input("Enter b: "))

max_val = a if a > b else b
print("Maximum =", max_val)

'''
o/p :- Enter a: 10
Enter b: 20
Maximum = 20
'''
print()
# 8. Swap Two Numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a
print("a =", a, "b =", b)

'''
o/p :- Enter a: 5
Enter b: 10
a = 10 b = 5
'''

print()
# 9. Next Multiple of 100

n = int(input("Enter number: "))

next_multiple = ((n // 100) + 1) * 100
print("Next multiple of 100 =", next_multiple)

'''
o/p :- Enter number: 250
Next multiple of 100 = 300
'''

print()
# 10. Splitting into the Teams

people = int(input("Enter number of people: "))

teams = people // 2
left = people % 2

print("Teams =", teams, "Leftover =", left)

'''
o/p :- Enter number of people: 5
Teams = 2 Leftover = 1
'''
