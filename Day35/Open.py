#open("filename", "mode of operation")
'''
try:
    f = open("demo.txt", "x")
    f.close()
except Exception as e:
    print(e)

d = open("demo.txt", "r")
data = d.read()     # reads all the lines in the file 
print(data)
d.close()


d = open("demo.txt", "w")  # write mode will override the old data 
d.write("Hello Deepika")
d.close()



d = open("memo.txt", "w") # write mode will override the old data and if file not exists then create a new file 
d.write("Data is changed")
d.close()


d = open("memo.txt", "a") # write mode will override the old data and if file not exists then create a new file 
d.write("\nnew data is added from the end the file.")
d.close()

with open("memo.txt", "r") as f:
    print(f.tell())\
    
    print(f.seek(17))
    print(f.read())          # read all the lines 

    print(f.tell())

    print(f.readline())     # reads only one line

    print(f.tell())

    print(f.readlines())       # returns all lines as a list  

    print(f.tell())

'''
with open("memo.txt", "r") as f:
    for i in range(6):
        print(f.tell())
        print(f.readline())

    print(f.tell())

# write Multiple lines

with open("demo.txt","w") as f:
    f.write("This is python training\n")
    f.write("no one is singing song\nwhy this kolavari di\n")
    f.write("why this kolavari di")


# using loop

with open("demo.txt","a") as f:
    name = input("Enter your name :")
    f.write(" " + name + " ")


# copy data from one file to another file ??

a = open("demo.txt" , "r")
b = open("memo.txt" , "w")

data = a.read()
b.write(data)

a.close()
b.close()



a = open("demo.txt" , "a")


print(a.name)
print(a.closed)
print(a.flush)
a.write("\ndata is appended after flushing")

a.close()


a = open("demo.txt" , "r")
print(a.read().split())
a.close()

