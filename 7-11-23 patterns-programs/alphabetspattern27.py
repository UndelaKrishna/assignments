num=int(input("Enter the no of Rows:"))
ascii_value=65
for i in range(1,num):
    for j in range(1,i+1):
        character=chr(ascii_value)
        print(character,end=" ")
        ascii_value+=1
    print()    















