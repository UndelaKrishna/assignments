n=int(input("Enter Number: "))         #---(14)
sum=0
for i in range(n):
    if i%2==1:
        sum+=i
print("total summation is =",sum)        