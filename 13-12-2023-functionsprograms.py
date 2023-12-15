#lambda
#1
a=lambda n:n*n
print(a(5))
#2
a=lambda a,b :a if a<b else b
print(a(5,10))

#3
l1=lambda a :a+10
print(l1(10))

#4
str1 = 'pythonisdynamiclanguage'
upper = lambda string: string.upper()
print(upper(str1))

#5
ages = [13, 90, 17, 59, 21, 60, 5]
l1= list(filter(lambda age: age > 18, ages)) 
print(l1)

#filter
#1
def even(x):
    if x%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,10]
a=filter(even,l)
print(a)

#2
def even(x):
    if x%2==0:
        return  True
    else:
        return False
l1=[1,20,30,40,22,13,12,44,55,18]  
a=list(filter(even,l1))
print(a)

#3
def fact(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    print(fa)  
fact(5)
l2=[1,2,3,4,5,6]
b=filter(fact,l2)
print(b)
for i in b:
    print(i)


#4
list=[1,22,33,2,44,14,19,50,22]    
b=filter(lambda a:a%2==0,list)
print(b)
for i in b:
    print(i)


#5
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
l1=[10,20,30,40,1,2,3,4,8,9,55]
a=filter(myFunc,l1)
print(a)
for i in a:
   print(i,end=" ")

#6
def div(x):
   sum=0
   for i in range(1,x+1):
      sum=sum+i
   print(sum) 
l1=[1,2,3,4,5,6,7,8,9,10]  
a=filter(div,l1) 
print(a)
for i in a:
   print(i)  


#map
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a,b:a*b,l1,l2)
print(a)
for i in a:
   print(i)

#2
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a,b:a+b,l1,l2)
print(a)
for i in a:
   print(i)
 
#3
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a,b:a/b,l1,l2)
print(a)
for i in a:
   print(i) 
#4
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a,b:a**b,l1,l2)
print(a)
for i in a:
   print(i)
 
#5
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a,b:a//b,l1,l2)
print(a)
for i in a:
   print(i)
 
#6
l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a:a%2==0,l2)
print(a)
for i in a:
   print(i) 

 #recursive fun
def fac(x):
    if x==1:
        result=1
    else:
        result=x*fac(x-1)
    return result
print(fac(6))

def fac(x):
    if x==1:
        result=8
    else:
        result=x*fac(x-1)
    return result
print(fac(8))

def fac(x):
    if x==1:
        result=0
    else:
        result=x*fac(x-1)
    return result
print(fac(6))

def fac(x):
    if x==1:
        result=5
    else:
        result=x*fac(x-1)
    return result
print(fac(10))

def fac(x):
    if x==1:
        result=10
    else:
        result=x*fac(x-1)
    return result
print(fac(10)) 

#arguments
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4) 
f(3,5)
f(10,20,30,40)
f(11,6,arg4=1000)
f(arg4=6,arg1=7,arg2=9)
f(arg3=90,arg4=80,10,50)    
f(6,8,arg2=89)  
f(4,5,arg3=7,arg5=78)  
f()  

#reduce
t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a+b-a*b+a*a,t))

from functools import reduce
value = reduce(lambda a, b: a + b, [1,2,3,4,5])
print(value)

l=[1,4.5,36,38,6,2]
print(reduce(lambda a,b:a<b,t))

t=(1,4.5,36,38,6,2)
print(reduce(lambda a,b:a%2!=0,t))

a=[2,6,18,9,83,72,90]
print(reduce(lambda x,y:y==2,a))





      



















   
