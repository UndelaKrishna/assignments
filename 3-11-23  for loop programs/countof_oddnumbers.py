num=int(input("Enter Number:"))    #--(6)
count=0
for i in range(num):
    if i%2==1:
        print(i,"Odd Number")
        count+=1
print("total count of odd numbers=",count)        