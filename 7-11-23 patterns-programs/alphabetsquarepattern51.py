num=int(input("Enter The Number Of Rows: "))
count=0
for i in range(num):
    for j in range(num):
        print(chr(65+count),end=" ")
        count=count+1
    print()   







