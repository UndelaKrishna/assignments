a=(10,20,30,40,77)#valid
a=10, #valid
a=10 #invalid
a=(11,)#invalid
a=(10,)#valid
a=()
print(type(a))


t=(10,20,30,40,50,60,10)
t[1]=120
print(t)
t.append(99)
print(t)

t.remove()
print(t)

t1=(10,20,30,40,50,60,70)
print(t1*3)

t1=(10,20,30,40,50,60,70,80)
t2=(10,20,30,50,60)
print(t1*2)
print(t2*2)
