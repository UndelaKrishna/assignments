#write a program to print sum 1 st 10 numbers    ---(11)
num=int(input("Enter Number: "))
s=0
i=0
while i<=num:
    s=s+i
    i=i+1
average=s/10
print("Average=",average)    