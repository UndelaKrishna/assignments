#write a program to calucate the sum  and average of first 10 numbers  --(10)

n=int(input("Enter Number: "))#input--10
i=0
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
avg=sum/10
print("The sum of first 10 numbers =",sum)    
print("the average of first 10 numbers=",avg)