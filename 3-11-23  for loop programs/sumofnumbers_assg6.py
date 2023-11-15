
num =  input("Enter Number :")
values = num.split(',')
sum=0
for i in values:
    sum+=int(i)   #converted integer values into sum ex:sum+=int(i)
print("Total suum is=",sum)