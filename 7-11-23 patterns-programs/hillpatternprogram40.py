num=int(input(" Enter the Number Of Rows: "))
for i in range(num):
    p=65
    for j in range(i,num):
        print('',end=" ")
    for j in range(i):
        character=chr(p)
        print(character,end=" ")
        p=p+1

    for j in range(i+1):
        character=chr(p)
        print(character,end=" ")
        p=p-1
    print()  












