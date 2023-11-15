num =int(input("Enter the no of Rows:"))
value=65
for i in range(num):
    for j in range(0,i+1):
        ch=chr(value)
        print(ch,end=" ")
    value=value+1
    print() 



      