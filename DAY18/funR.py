# Function returning another function

def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
print(square(5))        # 25



def discount(rate):
    def demo(price):
        return price - price * rate
    return demo

ten_percent = discount(0.1)
print(ten_percent(2000))        # 1800.0

