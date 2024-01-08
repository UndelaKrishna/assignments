class Employee:
    def __init__(self,eno,ename,esal) :
        self.eno=eno
        self.ename=ename
        self.esal=esal
        
    def employeeDetails(self):
        print("eno=",self.eno)
        print("ename=",self.ename)
        print("esal=",self.esal)


Employee(11,"krishna",3444).employeeDetails()

e=Employee(22,"kkk",87777)
e.__init__
e.employeeDetails()



#constructor overloading
class Demo:
    def __init__(self):
        print("this is first constructor method....")
    def __init__(self):
        print("this is second constructor method....")    
    def __init__(self):
        print("this is third constructor method")   
    def __init__(self):
        print("this is fourth constructor method")    
d=Demo()       





class Student:
    def __init__(self,sname,srno,sage,sper,sclg):
        self.sname=sname
        self.srno=srno
        self.sage=sage
        self.sper=sper
        self.sclg=sclg

    def StudentDetails(self):
        print("sname=",self.sname)    
        print("srno=",self.srno)
        print("sage=",self.sage) 
        print("sper=",self.sper)
        print("sclg=",self.sclg)

s=Student("krishna",22,24,77,"vikas")
s.StudentDetails()

Student=[Student("krishna",29,25,68,"nri")]
for i in Student:
    i.StudentDetails()

#1).instance variables(object level variable)
    
#1).inside the constructor you can declare  the variable
#2).inside the instance  method using self variables
#3).outside the class by using object refercence variable

class Employee:
    def __init__(self):  #1
        self.ename="krishna"
        self.esal=10000
        self.eid=307
    def employeeDetails(self):#2
              self.phno=9770
              self.edomain="python"

e=Employee() 
print(e.__dict__)

e.employeeDetails()
print(e.__dict__)
#outside the class by using object refercence variable
e.ecnm="marolix"#3
print(e.__dict__)

print(e.ecnm)
print(e.phno)
print(e.edomain)





class Student:
    def __init__(self):
        self.sname="ramu"
        self.srno=18
        self.sage=22
        self.sper=77
        self.sclg="dbs"
    def details(self):
        self.sbranch="ece"
s=Student()
s1=Student()
s.details()
s1.details()
s1.d=900

print(s.__dict__)       
print(s1.__dict__)  
print(s.sname)  
print(s1.sbranch)





class Test:
    def __init__(self) :
        self.a=100
    def a1(self):
        self.b=666
        self.c=9000
t=Test()
t.a1()
t.b=8888
t.c=7654
print(t.__dict__) 






#2).static variable(class level variable)

#how to acces static variable
# #should be acced either by classname or by object reference
class Employee:

    enm="krishna"#static variable

    def __init__(self):#instance variable
        self.eid=123
        self.esal=2222 
    def display(self):
        print("eid=",self.eid)
        print("esal=",self.esal)    
e=Employee()
print(e.enm) 
print(e.__dict__)

print(Employee.enm)
e.display() 

print(e.eid)
print(e.esal)






class Employee:

    enm="raju"#static variable

    def __init__(self):#instance variable
        self.eid=123
print("*****")
e=Employee()
e.eid=22

Employee.enm="krishna"
e1=Employee()
print(e.enm,e.eid)
print(e1.enm,e1.eid)


      



              


      