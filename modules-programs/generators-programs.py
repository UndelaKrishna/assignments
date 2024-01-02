#generators
l=(x*x for x in range(100000000000000000000000000000))
print(l)

l=[x*x for x in range(100000000000000000000000000000)]
print(l)
for i in l:
    print(i)
print(next(l))   
print(next(l)) 
print(next(l)) 
print(next(l)) 
