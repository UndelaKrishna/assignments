num=int(input("Enter The No Of Rows: "))

# for i in range(num):
#     a=65
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print() 

for i in range(num):
    for j in range(num-i,-1):
        print(chr(65+j),end=" ")

    print()    

