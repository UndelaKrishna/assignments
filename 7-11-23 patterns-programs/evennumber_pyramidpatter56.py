
num=int(input("Enter The No Of Rows: "))
lastEvennumber=2*num
evenNumber=lastEvennumber
for i in range(1,num+1):
    evenNumber=lastEvennumber
    for j in range(i):
        print(evenNumber,end=" ")
        evenNumber -=2
    print()
