#lambda
# syntax:-lambda input:expression
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


str1 = 'GeeksforGeeks'
 
upper = lambda string: string.upper()
print(upper(str1))


#5


ages = [13, 90, 17, 59, 21, 60, 5]
l1= list(filter(lambda age: age > 18, ages))
 
print(l1)
#filter

#syntax:-filter(function,sequence)
def even(x):
    if x%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,10]
a=filter(even,l)
print(a)
# for i in a:
#     print(i)
# b=filter(even,l)
# print(b)



#filter
#1
def even(x):
    if x%2==0:
        return  True
    else:
        return False
l1=[1,20,30,40,22,13,12,44,55,18]  
a=list(filter(even,l1))
print(a)

print("_________-")
#2
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


#3
list=[1,22,33,2,44,14,19,50,22]    
b=filter(lambda a:a%2==0,list)
print(b)
for i in b:
    print(i)
print("_______")
#4
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

#5
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

# filter function in oneline
# l=[1,2,3,4,5,6,7,8]
# a=filter(lambda a:a%2==0,l)
# print(list(a))


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
#6l1=[1,2,33,44,66,77]
l2=[10,22,39,44,55,67,9,96]
a=map(lambda a:a%2==0,l2)
print(a)
for i in a:
   print(i)                  
      



















   