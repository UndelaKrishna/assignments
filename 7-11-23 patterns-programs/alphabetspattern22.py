rows = int(input("Enter the no of rows:"))
ascii_number=65
for i in range(0,rows):
    for j in range(0,i+1):
        character = chr(ascii_number)
        print(character,end=" ")
        ascii_number+=1
    print()   






