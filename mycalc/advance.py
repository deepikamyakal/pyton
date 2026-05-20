class Sample:
    x= int(input("enter your number : "))
    
    def cube(self,x):
        res=x*x*x
        return res
    
    def factorial(self,x):
        num = 1
        while x>0:
            num = num * x
            x=x-1
        return num