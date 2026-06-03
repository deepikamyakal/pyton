'''
### 4. File Reader with finally

**Question:**
Write a program to:

* Open a file
* Read contents
* Handle FileNotFoundError
* Ensure file is closed using finally
'''

file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File closed.")