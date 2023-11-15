num=int(input("Number of Rows:"))
k=0
for i in range(num):
    k=k+i
m=num+k
for i in range(num):
    for j in range(i+1):
        print(format(m,"<3"),end=" ")  #"<"--it is used for spaces
        m=m-1
    print()    



 






