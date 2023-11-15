#wap to calculate the sum of numbers from m to n   --(12)

m=int(input("enter the value of m: "))
n=int(input("Enter the value of n: "))
sum=0
while (m<=n):
    sum=sum+m
    m=m+1
print("Sum =",sum)    