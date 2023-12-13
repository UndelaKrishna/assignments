

# #pro to print sum if given number in var len arg

def add(*a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)
add(10,20,30,40,50)
add(1,2,3,4,5,6,7,8,9,10)   


#types of arguments
#1).positional argument
def func(a,b):
    return a+b
print(func(10,20))

#2
def add(a,b):
    print(a-b)
    return a-b
add(200,100)
#3
def add(x):
    print("the square root of {}is{}".format(x,x*x))
add(10)

#4
def add(x):
    print("the cube of {} is{}".format(x,x*x*x))
add(22)
#5
def funcn(a,b):
    c=a*b
    return c
print(funcn(10,5))


#keywod argument
def  f(name,rollno):
    print("hi",name,rollno)
    return name,rollno
f(name="krishna",rollno=123)

#2
def f1(name,percentage):
    print("hii",name,percentage) 
    return name, percentage
f1(88.9,"krishnna")
#3
def add(a,b):
    print("addition",a+b)
    return a,b
add(a=10,b=5)
#4
def mul(b,c):
    print("multiplication of",b*c)
    return b,c
mul(b=10,c=5)

#5
def div(a,c):
    print("division of",a/c)
    return a,c
div(a=10,c=5)



#3).default  arguments
#1
def f(name,id):
    print("my name is",name + " and my id is",id)
f(name="srinu",id = 25)
#2
def f(name="krish",roll=545):
    print("hi my name is",name)
f(name="srinivas",roll=112)
#3
def add(age,name="krishna",rollno=29):
    print("my name is",name,"and my rollno is",rollno,"my age is",age)
add(10)  

#4
def func(name,age,percentage,color="white"):
    print("my name is",name,"my age is",age,"my percentage is",percentage,"my color is",color)
func("krishna",24,66.7,"green") 
func(24,"krishna","gray",77.9)

#5
def func(name,age,percentage,color="white"):
    print("my name is",name,"my age is",age,"my percentage is",percentage,"my color is",color)
func(name="krishna",age=33,percentage=88.8,color="blue") 

#6
def f2(roll,add,phn,name="raja"):
    print("hi",phn,add,roll,name)
f2(899,"krish",1213)


#variable length argument
def add(*a):
    print(a)
    for i in a:
        print(i)
add(10,20)
add(1,2,3,4,5,6)


#2
def sum1(*b):
    sum=0
    for i in b:
        sum=sum+i
    print("total sum is=",sum)  
sum1(10,20,30,40,50,60)
sum1(1,2,3,4,5) 


#4
def fun1(item_name,quantity,item_list="none"):
    if item_list =="none":
        item_list={}
        item_list[item_name]=quantity
        return item_list
print(fun1("notebook",4)) 
print(fun1("pencil",5))   
print(fun1("eraser",2))


#4
def fun(item_name,item_list="none"): 
    if item_list=="none":
        item_list=[]
        item_list.append(item_name)
        return item_list
print(fun("Notebook ")) 
print(fun("Pencil"))  
print(fun("ereaser"))


#global variable

name="krishna"
def f():
    global name
    print("name of the person",name)
f()


a=10
b=32
def sum():
    global a,b
    c=45
    print("sum",a+b)
sum()
    
    
def dif():
    d=78
    print("diff",a-b)
dif()


def mul():
    global dif
    d=78
    print("mul",a*b)
mul()



#local variable
name="python"
def f():
    name="ram"
    print("name of the person",name)
f()


a=10
b=32
def sum():
    c=45
    print("sum",a+b)
sum()
    
    
def dif():
    d=78
    print("diff",a-b)
dif()






            




