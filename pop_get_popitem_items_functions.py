
#get()
a=dict(((10,"krishna"),(20,"ramu"),(30,"raja"),(40,"cherry")))
print(a)

print(len(a))
print(a.get(10))

#2
b={100:"a",200:"b",300:"c",400:"d",500:"e"}
print(b)

c=b.get(300)
print(c)

#3
d={100: 'a', 200: 'b', 300: 'c', 400: 'd', 500: 'e',600:"krishna",700:"ramu",800:"python"}
print(len(a))
print(d.get(100,100))

#4

f={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}
print(f.get(600,"cherry"))
print(f.get(700,"teja"))

#5
f={10: 'krishna', 200: 'teja', 30: 'cherry', 40: 'patel',600:"ram"}
print(f.get(1000))


#pop()
#1
a={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}
print(a.pop(30))

#2
b={10:"teja",20:"krishna",30:"cherry",40:"ram",50:"raja"}
b.pop(20)
print(b)

# #3
c=dict(((10,"krishna"),(20,"ramu"),(30,"rama"),(40,"raju")))
print(c.pop(1000))

#4
d=dict([(10,"krishna"),(20,"ramu"),(30,"rama"),(40,"raju")])
print(d.pop())

#5
e=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})

a=e.pop(109)
print(a)


#popitem()
#1
a={10:"a",20:"b",30:"c",40:"d",50:"e"}
print(a.popitem())


#2
b=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})
for x in a.popitem():
    print(x)
#3
c={10: 'krishna', 200: 'teja', 30: 'cherry', 40: 'patel',600:"ram"}
c.popitem()
print(c)

#4
d=dict(((10,"krishna"),(20,"ramu"),(30,"raja"),(40,"cherry")))
print(d.popitem(10))

#5
d=dict([(100,"krishna"),(20,"ramu"),(300,"rama"),(400,"raju")])
c=d.popitem()
print(c)


#items()
#1
a=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})
print(a.items())

#2
d=dict([(100,"krishna"),(20,"ramu"),(300,"rama"),(400,"raju")])
for i in d.items():
    print(i,end=" ")

#3
l=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})
l.items()
print(l)

#4
e={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}
f=e.items()
print(f)

for x in f:
    print(x)

#5
l1={10:"teja",20:"krishna",30:"cherry",40:"ram",50:"raja"}
print(l1.popitem())
print(l1)

l2=l1.items()
print(l2)


#key()
a={10:"krishna",20:"rama","raja":300,"teja":3000,"rakesh":4000}
print(len(a))

a.keys()
print(a)

b={20:"krishna",30:"rama",40:"raja",50:"cherry"}
print(b)

for x,y in b.keys():
    print(x,y)


#values()
#1
a={10:"a",20:"b",30:"c",40:"d",50:"e"}
print(a)
for x in a.values():
    print(x)


#2
b=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})
print(len(b))

c=b.values()
print(b)
    













