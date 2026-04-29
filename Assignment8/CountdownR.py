'''
14.Countdown Using Recursion

**Question:**
Print countdown using recursion.

**Test Case 1:**
Input:
countdown(3)

Expected Output:
3
2
1
Done!
'''

def coutdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    coutdown(n-1)

coutdown(3)
