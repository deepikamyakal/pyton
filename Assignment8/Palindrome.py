'''
9) Palindrome Checker

**Question:**
Create function is_palindrome(word).
Return True if palindrome else False.

**Test Case 1:**
Input:
is_palindrome("madam")

Expected Output:
True
'''

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))
