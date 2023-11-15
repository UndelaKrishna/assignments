num=int(input("Enter Number :"))   #---(12)
sum=0
for i in range(num):
    if i%2==0:
        sum+=i
print("summation even numbers=",sum)