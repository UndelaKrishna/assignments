negitive=0
positive=0
zeroes=0
print("Enter -1 to exit...")
while(1):
    num=int(input("Enter any number:"))
    if(num==-1):
        break
    if(num==0):
        zeroes=zeroes+1
    elif(num>0):
        positive=positive+1
    else:
        negitive=negitive+1
print("Enter positive Number entered :",positive)
print("Enter Negitive Number entered :",negitive) 
print("Count of zeroes entered: ",zeroes)              