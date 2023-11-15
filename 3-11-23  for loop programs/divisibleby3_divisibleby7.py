num=int(input("Enter Number: "))                #---(7)
for i in range(num): #(num+1)- adding one value
    if i%3==0:
        print("divisible by three ",i)
    elif i%7==0:
        print("divisible by seven ",i) 
    else:
        print("divisible by null ",i)       