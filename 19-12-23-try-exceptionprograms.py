

#case-1
try:
    print("hiii")
    print(10/3)
    print("hloo")
except:
    print("statement4")
print("statement5")



#2
try:
    print("hiikrishna")
    print(10/0)
    print("divison")
except ZeroDivisionError:
    print("zero cannot  be divided")    
    print("hii") 



#3
try:
    print(1*5)
    print(10/2)
    print("substraction")
except ZeroDivisionError as m:
    print("zero cannot  be divided",m)    
    print("hii") 



 #4
try:
    print(5+10)
    print(10/0)
    print("divison")
except ZeroDivisionError as m:
    print(10/2,"message",m)    
    print("hii")


#5
try:
    print("hiikrishna")
    print(10/0)
    print("divison")
except ZeroDivisionError as m:
    print(10/0,"message",m)    
    print("hii") 



#case-2:
try:
    print("hii")
    print(10/0)
    print("hello")
except ZeroDivisionError:
    print("zero cannot  be divided by zero")
    print("hlooo")  


#2
try:
    print(10%1)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
    print(10/0,"message")
    print("hlooo")
    
    
#3
try:
    print(5%10)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
    print(10/2,"message")
    print("hlooo")  


#4
try:
    print(5%10)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
    print("zero cannot be divided",m)
print("hlooo")    



#case-3
#1
try:
    print(10%1)
    print(10/0)
    print("hello")
except SystemError:
    print(10/0,"message")
print("hlooo")   


 #2
try:
    print(5%10)
    print(10/0)
    print("hello")
except ValueError:
    print("hiiii")
print("statement5")


# #3
try:
    print(5%10)
    print(10/0)
    print("hello")
except SystemError as m:
    print(10/2,"message",m)
print("hlooo")  

#case-4:
try:
    print(100-90)
    print(10/0)
    print("hello")
except ZeroDivisionError:
    print(10/0)
print("hlooo")


#2
try:
    print(1*90)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
    print(10/0,"message")
print("hlooo")  


#3
try:
    print(100+50)
    print(10/0)
    print("hello")
except ZeroDivisionError:
   print("hiii")
print(10/0,"hlooo")  



#4
try:
    print(100+50)
    print(10/0)
    print("hello")
except ZeroDivisionError:
   print(10/2,"hiii")
print(10/0,"hlooo")  



#5
try:
    print(100-50)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
   print(10/2,"hiii",m)
print(10/0,"hlooo")  




try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divided by zero") 



try:
    a=int(input("enter the first number"))
    for i in range(0,10):
       if i%2==0:
           
           print(i,"is even")
       elif i%2!=0:

           print(i,"is odd numbers")
except :
    print("invalid")
    

try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot division of number") 
except ValueError:
    print("please provide a value not string")    



try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except (ZeroDivisionError,ValueError )as m:
    print(m) 


    
    

    
    

             
        
    
    
    
          

