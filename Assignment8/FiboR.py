'''
11. Fibonacci Using Recursion

**Question:**
Print first N Fibonacci numbers.

**Test Case 1:**
Input:
n = 5

Expected Output:
0 1 1 2 3
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibo(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

fibo(5)