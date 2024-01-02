#decorators
def dec(f):
    def inner(name):
        if name=="red":
            print("good color")
        else:f(name)
    return inner 

@dec
def color(name):
    print("i want",name)
color("red")    
color("green")


def dec(func):
    def inner(a):
       x=func(a)
       return x*x
    return inner 
def mul(func):
    def inner(a):
       x=func(a)
       return 2*x
    return inner 
@mul
@dec
def num(a):
    return a
print(num(10))


def dec1(func):
    def inner(name):
        print("this is 1 st decoratotr executiing")
        func(name)
    return inner    
def dec2(func):
    def krishna(name):
       x=func(name)
       print("this is 2 st decoratotr executiing")
       func(name)
    return krishna 
@dec2
@dec1
def hello(name):
    print("hii",hello,"goodmorning")
hello("krishnareddy")




