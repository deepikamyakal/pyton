  # Hierarical Inheritance
'''
        Father
         /  \
        /    \
       /      \
    child 1   child 2
       
'''

class parent:
    def method1(self):
        print("This is parent class")

class child1(parent):
    def method1(self):
        print("This is child1 class")

class child2(parent):
    def method1(self):
        print("This is child2 class")



# Hybrid Inheritance --- > combination of more that one type of inheritance....gg