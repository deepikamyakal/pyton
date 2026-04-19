# 2.Write a program to count the number of vowels in a given string using string methods.
# Without loop
text = input("Enter a string :")
text = text.lower()
vowel_count = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
print("Number of vowels:",vowel_count)

'''
# With loop
text = input("Enter a string :")
count = 0

for ch in text.lower() :
    if ch in "aeiou":
        count += 1
print("Number of Vowels:",count)
'''



'''
Output : 
Enter a string : HELLO HASH
Number of Vowels: 3
'''