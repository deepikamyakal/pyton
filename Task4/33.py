# 33. Program to Count Words in a Sentence
'''
**Problem Statement:** Write a program to count the number of words in a sentence.

**Test Cases:**
• Test Case 1:
Input: sentence = hello world
Expected Output: 2
'''

sentence = input("Enter sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)