# return 


def is_even():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

print(is_even())    # ----> none


def is_even():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even())        # Even


# Prime no
# a number which is only divisible by 1 and itself ----> every number is prime number ??
# 99 --> 99 = 1 --> only 2 factors

