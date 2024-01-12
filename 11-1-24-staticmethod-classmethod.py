
class  Employee:
    enam="krshna"
    def __init__(self) :
        Employee.eid=307
        self.a=33
    def details(self):
        Employee.esal=15000
        Employee.edomain="python" 
        self.b=99
    @classmethod    
    def employeeDetails(cls):
        Employee.cname="marolix"
        cls.eas=4.0
    @staticmethod    
    def display():  
        Employee.eexp=1

print(Employee.__dict__)
e=Employee()
e.details()
Employee.employeeDetails()
Employee.display()
Employee.c=100
print(Employee.__dict__)

e.employeeDetails()
e.display()
print(e.__dict__)







class Student:
    smarks=500
    def __init__(self,snm,sper,sid,sphn):
        self.snm=snm
        self.sper=sper
        self.sid=sid
        self.sphn=sphn

        print(self.smarks)
        print(Student.smarks)
    def s(self):    
        print(self.smarks)
        print(self.sid)
        print(self.snm)
        print(Student.smarks)
    @classmethod
    def s1(cls):
        print(cls.smarks)  
        print(Student.smarks)
 
    @staticmethod
    def s2():
      print(Student.smarks) 
      print(Student.smarks)
print(Student.__dict__)        

s=Student("krishna",70,12,9888,)
print(s.smarks)
s.s()
s.s1()
s.s2()
print(s.smarks)
print(s.__dict__)










class Test:
    a=30
    def __init__(self) :
        pass
    def a(self):
        print("instance method")
    @classmethod
    def a1(cls):
        print("class method") 
    @staticmethod
    def a2():
        print("static method")

print(Test.__dict__)         
t=Test()
t.a()
t.a1()
t.a2()
print(t.__dict__)
print(Test.__dict__)


       
