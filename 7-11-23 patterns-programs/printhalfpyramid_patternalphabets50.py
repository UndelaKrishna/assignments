num=int(input("Enter The No Of Rows: "))
for i in range(1,num+1):
    a=65
    for j in range(num,i-1,-1):
        character=chr(a)
        print(character,end=" ")
        a=a+1
    a=a-1
    print()    









