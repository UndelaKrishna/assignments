

# #copy()
a=[10,20,30,40,50,60]
b=a.copy()
print(b)




# #reverse sort()
list=[10,22,30,40,57,60]
list.sort(reverse=True)
print(list)



#comparaing list objects
l1=["krishna","python","java","sql","twsting"]
l2=["krishna","python","java","sql","twsting"]
print(l1 is l2) 
print(l1 is not l2)

print(l1==l2)
print(l1!=l2)
print(id(l1))
print(id(l2))




# #matri function
a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
print("totl length is=",len(a))
for i in a:
    for j in i:
        print(j,end=" ") 
    print()    













