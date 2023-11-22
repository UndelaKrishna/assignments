#extend()

a=[10,20,30,"krishna","python",11.2,44,55,66]
b=[1,2,3,4,5,6]
b.extend(a)
print(b)
print(a)

n=[10,22,33,44,55,66,77,88,90]
m=["krishna","python","java","sql"]
n.extend("hloo")
print(n)
m.extend("hll")
print(m)

l=[10,20,30,40,50,60]
l1=["krishna",22,33,44,5,78]
l1.extend("java")
print(l1)
l.extend(["python"])
print(l)

l=[1,2,3,3,"krishna","java","sql"]
l2=[10,2,30,40]
l.extend(l2)
print(l2)
print(l)

l1=[1,2,3,3,4,44,55,6,66,77]
l2=[10,2,30,40]
l1.extend(l1)
print(l2)
print(l1)




#remove()
l=[10,20,20,30,40,50]
l.remove(20)
l.remove(20)
l.remove(20)#ValueError: list.remove(x): x not in list
print(l)

l1=[10,20,30,40,50,60]
l1.remove(40)
print(l1)

l2=["krishna","java","python",12,13]
l2.remove("krishna")
print(l2)

l3=["krishna","python","True","False",11,11.2,12]
l3.remove("krishna")
print(l3)

l4=[10,20,30,40,50,60]
l4.remove(10)
print(l4)
l4.remove(100) #ValueError: list.remove(x): x not in list
print(l4)

l5=[10,20,30,40,50]#to perform remove action there is no reurn valuews it is-- (None)
print(l5.remove(30))




#pop()
l=[10,20,30,40,50,60,70]
l.pop(1) #to remove by using indexing
print(l)

l1=[1,2,3,4,"krishna","python",11.9,10]
l1.pop()#to delete last occurence of the elemnts
print(l1)


l2=[10,20,30,40,45,69,90]
print(l2.pop(5))   #return the element output should be(45)

l3=[10,11,22,33,44,55,66,77,88]
print(l3.pop())
l3.pop(1)
print(l3)


l4=[11,22,33,"python","java",10.3,15,20]
l4.pop(4)
print(l4)
print(l4.pop())





#reverse()
l1=[10,20,30,40,50,60]
l1.reverse()
print(l1)
 
l2=["krishna","python","java","sql",10,22]
l2.reverse()
print(l2)

l3=["python","java"]
l3.reverse()
print(l3)

l4=["python"] #multiple elemnts you have to take
l4.reverse()
print(l4)

l5=[10,20,30,40]
print(l5.reverse())  #to perform reverse action there is no reurn valuews it is-- (None)

l=[10,20,30,40,50]
l.reverse()
print(l)





#sort()
a=[10,20,30,40,50,60,1,2,3,4]
a.sort()
print(a)


b=["krishna","python","Java","Sql","ram"]
b.sort()
print(b)


c=[10,20,30,"krish","python","java"]#TypeError: '<' not supported between instances of 'str' and 'int'
c.sort() #cannot compare to int to string
print(c)

d=["krishnareddy","ram","Pawan","Java","KOhli"]
d.sort()
print(d)

e=[1,2,13,45,67,90,77]
e.sort()
print(e)