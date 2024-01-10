

#by using  @classmethod
class Student:

    def __init__(self,sname,smarks) :
        self.sname=sname
        self.smarks=smarks

    def message(self):
        print(self.sname,"percentage is=",self.smarks,"%") 
        
    @classmethod
    def display(cls,sname,smarks):
        return cls(sname,str((int(smarks)/400)*100))
    

s2=Student.display("krishna","90")  
s2.message()

s3=Student.display("ramu","80")
s3.message()




class MyClass:
    def __init__(self,fname,lname) :
        self.fname=fname
        self.lname=lname
    def msg(self):
        print("fname=",self.fname,"lname=",self.lname) 
    @classmethod    
    def getSalary(cls,salary):
        cls.salary=salary

    def s(self):
        print("total salary is=",self.salary)   
       

m=MyClass("krishna","teja")
m.getSalary(12000)
m.msg()
m.s()





class Student:
    count=0
    def __init__(self,sname,smarks) :
        self.sname=sname
        self.smarks=smarks
        Student.count=Student.count+1

    def message(self):
        print(self.sname,"______",self.smarks)  
    @classmethod    
    def total_count(cls):
        return cls.count
    
s1=Student("krishna",80)  
s2=Student("ramu",88)
print("total count is=",Student.total_count()) 
# print("total count is=",s1.total_count())
# print("total count is=",s2.total_count())






#without using @classmethod 

class Employee:
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
        print(self.ename)
        print(self.eid)
    def details(string):
        print(string)    


e=Employee.details("krishna,99")




class Employee:
    def __init__(self,eid):
        
        self.eid=eid
     
    def details(self):
        a,b=map(int,self.eid.split(","))
        self.a=a
        self.b=b

    def d(self):   
        print(self.a)
        print(self.b)

e=Employee("1200,99")
e.details()
e.d()





class Student:
    def __init__(self,srno,sphno):
        
        self.srno=srno
        self.sphno=sphno
     
    def details(self):
      a,b=map(int,[self.srno,self.sphno])
      self.a=a
      self.b=b

    def d(self):   
        print("Roll No is=",self.a)
        print("Mobile NO is=",self.b)


e=Student("29","9032022837")
e.details()
e.d()




