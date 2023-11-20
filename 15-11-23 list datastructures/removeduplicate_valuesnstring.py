   #remove duplicate elements
# #1).
str=(input("Enter The Character: "))

str1=" "
for i in str:
       if i not in str1:
         str1=str1+i
  
print(str1) 

# print("************************************************************")
# #2).
str=(input("Enter The Character: "))  #2
st=[]

for i in str:
       if i not in st:
         
         st.append(i)
print(st)

print("********************************************")
  


#Nexted List

l=[10,20,30,[40,50,60],70,80,90,11]
print(len(l))
 
print(l[0],l[3][0],l[3][1])
print(l[3][0])
print(l[3][1])
print(l[3][2])
print(l[4],l[5])

print(l[0:6])

print(l[0],l[1],l[2],l[3][0],l[3][1],l[3][2])

print(l[0:3])
print(l[0:8])
print(l[1:5])
print(l[1:7])
print(l[1:4])
print(l[0:5])
print(l[2:7])
print(l[3:7])
print(l[3:7:1])

print("**********************************")
print(l[-1:4:-1])
print(l[-1:5:-1])
print(l[-1:1:-1])
print(l[-2:0:-1])
print(l[0:6:1])
print(l[0:7:1])



