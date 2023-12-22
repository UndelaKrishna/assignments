#try-except-finally:
try:
    print("try block")
except:
    print("except block") 
finally:
    print("finally block")   



try:
    print("hiii")
    print(10/0)
    print("hlo")
except:
    print("cannot divided by zero")  
finally:
    print("finally block executed") 




try:
    print("try block")
    print(int("krishna"))
except  ValueError:
    print("except error occured")  
finally:
    print("finally block executed") 
print("outside of the final block")  




try:
    print("tryblock")
except:
    print("except block") 
print("outside of except block") 

finally:
   print("finally block executed")




try:
    print(10+5)
    print("hiii")
    print(10/0)
except ZeroDivisionError:
    print("cannot devided by zero") 
    print("inside the except block")    

finally:
    print("finally block executed")
print("outside of finally block")    






try:
    print("tryblock")
    print(10/0)
print("outside of tryblock")  
except ZeroDivisionError:
print("cannot divided by zero")

print("except block")
finally:
print("finally block execute")  




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
    print("hiii")
    a=10+"hiii"

    print("hello")
except TypeError
    print("cannont add an int and a string")

finally:
    print("finally block executed")
print("hello")    





try:    
    print("hiii")
    print(a+b)

except NameError:
    print("variable names is not define")
finally:
    print("finally block eecuted") 





#try-ecept-else:
try:
    print("try block")
    print(10+7)
except:
    print("except block")    
else:
    print("else block executed")
print("outside of else block")  





try:
    print(10/0)
    print("insideatryblock")
except ZeroDivisionError:
    print("cannot divided by zero")  
    print("inside of exceptblock")
else:
    print("else block executed")
print("outside of elseblock") 





try:
    print("hiiii")
print("outside of tryblock")  
except:
     print("except block")  
else:
   print("else block executed")





try:
    print(float("hii"))
    print("tryblock")
except ValueError:
    print("except block")  
else:
    print("else block executed")
print("outside of else block")




try:
    print("hiiii")
print("outside of tryblock")  
except:
     print("except block")  
print("outside of exceptblock")
 
else:
   print("else block executed")
print("outsideof elseblock")



try:
    print("hii")
    for i in range(1,10):
        if i%2==0:
            print(i,"is even")
except:
    print("except block error occured")  
else:
    print("else block exceuted")
print("outsideof elseblock") 





try:
    print("hii")
    a=[1,2,3,4,5,6,7,8,910]
    for i in x:
        if i%2!=0:
            print(i,"is even")
except NameError:
    print("except block error occured")  
else:
    print("else block exceuted")
print("outsideof elseblock") 




#try-finally:
try:
    print("tryblock")
    print(10/2)
except:
    print("except block")
finally:    
    print("finally block eecuted")



try:
    print("hiii")
    print(1*5)
    print("hello")
finally:
    print("finally block executed")
print("outside of finallyblock") 



try:
    print("inside of try block")
print("outsideof tryblock")  
finally:  
    print("finally block executed")
print("outside of finally block")    



try:
    print("hiii")
    print(10+2)
finally:
    print(10/0)
print("outside of finally block")  


#try-except:
try:
    print("hiii")
    print(10/0)
    print("tryblock")
except ZeroDivisionError:
    print("cannot divided by zero")  
print("outsideof exceptblock")    




try:
    print("hiii")
print("outside of tryblock")
except:
    print("inside a except block")
print("outside of except block")    



try:
    int("hiii")
    print("tryblock")
except ValueError:
    print("value error occured")
print("outside of except block")




try:
    a=10+"hiii"
    print(a)
except TypeError:
    print("cannont add an int and a string") 





try:    
    print("hiii")
    print(a+b)
except NameError:
    print("variable names is not define")




#userdefined Exception

class PassException(Exception):
  def __init__(self,arg):
        self.msg=arg

class FailException(Exception):
    def __init__(self,arg):
        self.msg=arg

try:
    marks=int(input("enter you total marks: "))
    if marks>=50:
     raise PassException("Congrats You have Cleared The Semester")    
    
    elif marks <50:
        raise FailException("sorry better luck next time")
except PassException as pe:
    print(pe.msg)    

except FailException as fe:
    print(fe.msg)    
except ValueError:
    print("Invalid Input")
  





    







    
     


  



    

   

