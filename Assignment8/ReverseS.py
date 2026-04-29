'''
13.Reverse String (Recursion)

**Question:**
Reverse string using recursion.

**Test Case 1:**
Input:
"python"

Expected Output:
"nohtyp"
'''

def rev_str(s):
    if len(s) == 0:
        return s
    return s[-1] + rev_str(s[:-1])

print(rev_str("python"))