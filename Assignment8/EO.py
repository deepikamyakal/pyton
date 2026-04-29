'''
8) Even & Odd Counter

**Question:**
Write a function that returns count of even and odd numbers.

**Test Case 1:**
Input:
[1,2,3,4,5]

Expected Output:
Even count: 2
Odd count: 3
'''

def count_even_odd(num):
    even = 0
    odd = 0

    for n in num:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even,odd

num = [1,2,3,4,5]

even_count, odd_count = count_even_odd(num)

print("Even Count :", even_count)
print("Odd Count ", odd_count)