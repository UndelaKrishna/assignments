#Tuple()
# 1
a=[10,2,3,4,5,6,7,8,9]
print(a.sort())
b=a.sort()
print(b)
print(sorted(a))

#2
b=(10,20,40,30,50,60,70)
a=list(b)
print(a)

print(a.sort())
print(sorted(a))
a.sort()
print(a)

#3
c=[10,20,40,30,50,70,80]
print(c.sort())
print(sorted(c))


#4
d=[10,20,30,40,50,90,70]
print(sorted(d))
print(tuple(sorted(d)))

#how to convert tuple
a=tuple(sorted(d))
print(a)


#5
e=[10,30,40,50,20,70,90]
print(e.sort())
print(tuple(sorted(e)))
print(sorted(e))

#6
l1=(10,20,30,40,50,60,90,55)
# l1.sort()
# print(l1)
print(sorted(l1))
#how to convert tuple
a=tuple(sorted(l1))
print(a)


#imp functions on tuple

#index()
#1
t=(10,20,30,40,50)
print(t.index(20))


#2

t1=(10,20,30,40,50,60)
print(t1.index(50))
print(t1)


#3
t2=(10,20,30,40)
print(t2.index(100))#tuple.index(x): x not in tuple

#4
t3=(10,20,30,"python","java","krishna")
print(t3.index("krishna"))

#5

t4=(True,False,"python","java",10,10.2)
print(t4.index(False))



#count()

#1
l1=(10,20,30,40,50)
print(l1.count(10))

#2
l2=(10,20,10,40,50)
print(l2.count(10))

#3

l3=(10,20,True,44,True,11,False)
print(l3.count(True))

#4

l4=("python","java","sql","java","python",True,False)
print(l4.count("python"))

#5

l5=("python","java","sql","java","python",True,False,True,True,False,10,20,10,False,10.2,10.1,102)
print(l5.count(False))





# #set()

#1)add()
s={10,20,30,40,50,60,80}
s.add(200)
print(s)

#2)
l1={10,20,30,40,50}
l1.add(10)
print(l1)

#3).
l2={10,20,30,"python","java","sql","testing",True}
l2.add(11.2)
print(l2)

#4).
l3={10,20,30,40,50,60,90}
l3.add("python")
print(l3)

#5).
l4={10,20,30,40,50,60,90}
l4.add(True)
print(l4)

#update()


t={10,20,30,40,50,60,70}
# t.update(10,20,30,40)#--- it completly individuval  integers
# print(t)
a={10,22,33,44,55,66} #-- it is a seaquence 
t.update(a)
print(t)

#2).
t1={10,20,30,40,50,60}
t1.update((70,80,90))
print(t1)

#3).
t2={110,20,30,"python","java",11.2,"testing",77,88}
t2.update([10,22,"krishna"])
print(t2)

#4).
t3={10,20,30,40,80,60,66}
t3.update("krishna")
print(t3)

#5
t4={10,20,30,40,50}
t4.update([True])
print(t4)

t4.update(range(20),"python")
print(t4)

#copy()

#1
s={10,20,30,40}
b=s.copy()
print(b) 

#2
s1={10,20,30,40,50,60}
s1.copy()
print(s1)

#3
s2={10,20,30,40,50,60}
a=list(s2)
a.copy()
print(a)
#4
s3={10,20,30,40,50}
c=s3.copy()
print(c)
print(id(s3))
print(id(c))

#5
s4={10,20,30,40,50,60,70}
d=s4.copy()
print(s4)

e=list(s4)
e.copy()
print(e)



#pop()

#2
t={10,20,30,40,50,60}
print(t.pop())
print(t.pop())

t.pop()
print(t)

#2
t1={10,20,30,40,50,60}
t1.pop(1)
print(t2)

#3
t2={10,20,30,40,60,"python","java"}
print(t2.pop())

#4

t3={10,20,10,60,80,90,11.2}
print(t3.pop())
t3.pop()
print(t3)

#5

t3={10,20,10,60,80,"python","hii","java",True,90,11.2}
print(t3.pop())

t3.pop(3)
print(t3)

#remove()
#1
l1={10,20,30,40,50,60,70}
l1.remove(30)
print(l1)

#2
l2={10,20,30,"python","java","sql",True,11.2}
l2.remove(True)
print(l2)

#3

l3={10,20,30,40,50,90,100,200,10.3}
# l3.remove(3000)
# print(l3)

l3.remove(10.3)
print(l3)

#4
#duplicate values are not allowed
l4={10,20,30,40,50,60,70,20,10}
l4.remove(10)
print(l4)

#5
l5={10,20,30,40,50,"python","java","java",True,False,True,10.3,10.2,10.3}
l5.remove(True)
print(l5)


#discard()
#1
s1={10,20,30,40,50,60}
s1.discard(200)
print(s1)

#2

s2={10,20,30,40,50,60,70,80}
s2.discard(90)
print(s2)

#3

s3={10,20,30,40,"python","java","sql",True}
s3.discard(True)
print(s3)

#4

s4={10,20,30,40,"python","java","sql",True,10,"python","sql","java"}
s4.discard("sql")
print(s4)

#5

s5={10,20,30,40,"python","java","sql",True,11.2,False,10.3,11.2,10}
s5.discard(10000)
print(s5)








