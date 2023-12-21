# #case-1
try:
    print("hiii")
    print(10/3)
    print("hloo")
except:
    print("statement4")
    print("statement5")
finally:
    print("statement-6")
print("statement-7")  


try:

    print("hiikrishna")
except ZeroDivisionError:
    print("statement-4")
    print("statement5")
finally:
    print("statement-6")
    print("statement-7") 


try:
    x=10
    print(x)
except:
    print("somthing went wrong")
finally:
    print("finally block is executed")  



#case-2
try:    
    print("hiii")
    print(a+b)

except NameError:
    print("variable names is not define")
finally:
    print("finally block eecuted") 


try:
    a=10+"hiii"
    print(a)
except TypeError:
    print("cannont add an int and a string")   
finally:
    print("finally block executed") 


try:
     a=10
     print(a.b)
except AttributeError:
    print("attribute error occured")
finally:
    print("finally block executed..")   



try:
    print("hii krishna")
    int("abc",99)
except ValueError as e:
    print("value error occcured..")  
finally:
    print("finally block exxecuted..")  



try:
     print("hiii")
     l=[i for i in range(1000000000000000000000000000000000)]
     print(l)
except MemoryError:
    print("memory error occured..")  
finally:
    print("finally block excecuted...")       



# case-3
try:
    print("hiii")
    print(10/0)
    print("hello")
except SystemError:
    print("cannot divided by zero")
    print("hlooo")
finally:
    print("finally block executed")
print("hello") 



try:
    print("hiii")
    a=10+"hiii"

    print("hello")
except ValueError:
    print("cannont add an int and a string")

finally:
    print("finally block executed")
print("hello")    



# case-4
try:
    print("hiiikrishna")
    print(22/0)
    print("hello")
except ZeroDivisionError:
    print(10/0)
    print("cannont add an int and a string")

finally:
    print("finally block executed")
print("hii")  



try:
    print(1*90)
    print(10/0)
    print("hello")
except ZeroDivisionError as m:
    print(10/0,"message")
    print("hlooo")
finally:
    print("finall block eecuted")

#case-5
try:
    print(1*90)
    print(1+5)
    print("hello")
except ZeroDivisionError:
    print(10/0,"message")
    print("hlooo")
finally:
    print(10/0)
print("finally block executed")   




try:
    print(1*90)
    print(1+5)
    print("hello")
except ZeroDivisionError:
    print(10/0,"message",m)
    print("hlooo")
finally:
    print(10/0)
print("finally block executed") 



# #case1--exception raised at outer try
try:
    print(float("abc"))
    try:
        print("inner try block")
        print("inner try block2")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except ValueError:
    print("outer except block")
    print("outer except block2")
finally:
    print("outer finally block")
print("outside the all block")



#case-2 exception raised at outer try stm-2
try:

    print("outer try block ")
    try:
        print("inside try block")
        print(10/0)

    except ZeroDivisionError:
        print("print inner except block")
    finally:
        print("fianlly block") 
except ValueError:
    print("outer of except block")  
finally:
    print("outer finally block")
print("outer all finally block ")   





#case-3 exception raised at inner try stm-2
try:

    print("outer try block ")
 
    try:
        a=10+"hiii"
        print(a)
        print("inside try block")
        
    except TypeError:
        print("print inner except block")
    finally:
        print("fianlly block")
       
except :
    print("outer of except block")
finally:
    print("outer finally block")
print("outer all finally block ") 




# case-4 exception raised at inner ecept stm-3
try:
    print("hiii")
    try:
        print("inner try block")

    except ZeroDivisionError:
        print("inner except block")
        print(10/0)
    finally:
        print("inner finally block")
    print("outside the inner block")
except SyntaxError:
    print("outer except block")

finally:
    print("outer finally block")
print("outside the all block")




# case-5 exception raised at outer try and inner except stm-1,3
try:
    print(50/0)
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print(10/0)
        print("inner except block")
    finally:
        print("inner finally block")
    print("outside the inner block")
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")
print("outside the all block")





# case-6 exception raised at outer try and finally block  stm-1,4
try:
    print(50/0)
    print("outer try block")
    try:
        print("inner try block")
    except ZeroDivisionError:
        print("inner except block")
    finally:
        print(10/0)
    print("outside the inner block")
except :
    print("outer except block")
finally:
    print("outer finally block")
print("outside the all block")


















 

     
    






        

   
    






