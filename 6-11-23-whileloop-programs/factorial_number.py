#wap to calucate factorial of given input n by using while loop   --(15)
num=int(input("Enter a number: "))
fact=1
while(num>0):
    fact =fact*num
    num=num-1
print("factorial number is: ",fact)    