num=int(input("Enter the Number Of Rows:"))
for i in range(0,num):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()    