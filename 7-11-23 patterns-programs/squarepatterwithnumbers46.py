
n=int(input("Enter the No of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()     






