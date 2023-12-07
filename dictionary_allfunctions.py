#del()
#1
a=dict([(10,"krishna"),(20,"ramu"),(30,"rama"),(40,"raju")])
print(a)
del a[30]
print(a)

#2
b=dict({(109,"krishna"),(200,"python"),(30,"java"),(400,"raju")})
print(b)

del b[400]
print(b)

#3
c=dict(((10,"krishna"),(20,"ramu"),(30,"rama"),(40,"raju")))
print(c)

del c[10]
print(c)

#4
d=dict([(100,"krishna"),(20,"ramu"),(300,"rama"),(400,"raju")])

del a[10]
print(d)

# del a
# print(a)

#5
e={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}

del e[200]
print(e)

# del e
# print(e)

#clear()
#1
f={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}
print(f.clear())

#2
g={10: 'krishna', 200: "raju"}
g.clear()
print(g)

#3
h={10: 'krishna', 200: 'testing', 200: 'java', 40: 'python',400:"sql"}
h.clear()
print(h)

#4
i={10: 'krishna', 200: 'testing', 30: 'raja', 40: 'rama',600:"sql"}
print(len(i))

b=i.clear()
print(b)

#5
l={10: 'krishna', 200: 'testing', 30: 'java', 40: 'python',600:"sql"}

print(l.clear())







