

#using forloop to iterate through elements in sequeance executing a set of statements for each item
#output statemnts are essential for displaying results
#program to check the credentials for an user

num=int(input("Enter Number: "))   #--(3)
count=0
for i in range(num):
    if i%2==0:
        print(i,"even number")
        count+=1
        # print("total count of even numbers =",count)    
print("total count of even numbers =",count)  