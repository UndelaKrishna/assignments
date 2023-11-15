



num=int(input("Enter a Number: ")) 

for i in range(1,num): 
    n=1
    for j in range(num,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print(n,end=" ")
            n=n+1  
    print() 