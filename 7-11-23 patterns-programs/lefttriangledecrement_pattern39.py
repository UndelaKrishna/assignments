num=int(input("Enter The Number Of Rows: "))
a=69
for i in range(num):
    p=a
    for j in range(i):
        print('',end="")
    for j in range(i,num):
         print(chr(p),end=" ")
         p-=1
    a-=1
    print() 
    
       



