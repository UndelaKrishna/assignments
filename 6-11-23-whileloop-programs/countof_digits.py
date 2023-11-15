#count number of digits in an integer using while loop     ---(16) input(1234)-o/p(4)
num=int(input("Enter number: "))
count=0
while num!=0:
    num=num//10
    count+=1
print("Number of digit in given number is: ",count)    