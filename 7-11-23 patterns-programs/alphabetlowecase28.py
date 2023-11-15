num=int(input("Enter the no of Rowws:"))
ascii_number=97
for i in range(1,num):
    for j in range(1,i+1):
        character=chr(ascii_number)
        print(character,end=" ")
        ascii_number=ascii_number+1
    print()    








