class Employee:
      name="krishna" 
      def __init__(self,ename,esal,eid,epack,edomain,name):
            name="krishna"
            self.ename=ename
            self.esal=esal
            self.eid=eid
            self.epack=epack
            self.edomain=edomain
            self.name=name
      def employeeDetails(self) :
            print("Employee Details:")   
            print(self.name,"***********",self.ename,"********",self.esal,"********",self.eid,"********",self.epack,"********",self.edomain) 
  
e=Employee("krishnareddy",20000,307,3.8,"python","raju")
e.employeeDetails()
print(e.name)
print(Employee.name)
  
e=Employee("ram",200,30,3.58,"java","ramam")
e.employeeDetails()
print(e.name)
print(Employee.name)


class student:
  def __init__(a,x,y,z,r) :
    a.snm=x
    a.srno=y
    a.sper=z 
    a.sclg=r

  def display(a):
      print("display method....")
      print(a.snm)
      print(a.srno)
      print(a.sper)
      print(a.sclg)
s=student("krishna",123,77,"vikas")
s.display()


class Employee:
    def __init__(emp) :
        emp.ename="krishna"
        emp.esal=20000
        emp.eid=307
        emp.epack=4.0
    def employeeDetails(emp):   
        print("Employee Details:") 
        print(emp.ename)
        print(emp.esal)
        print(emp.eid) 
        print(emp.epack)
Employee().employeeDetails() 

# #by using method
class Student:
    def studentRecords(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
s=Student()
s.studentRecords("krishna",44,99)     



# #by  using constructor

class Student:
    def __init__(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
s=Student("krishna",44,99)

# #by using constructor and method
class Student:
    def __init__(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
    
    def studentRecords(self,sname,srno,sper):
        self.sname=sname
        self.srno=srno
        self.sper=sper
        print("student records")
Student("krishna",88,77)  .studentRecords("krishna",88,77) 
# s=student("krishna",88,77)  
# s.studentRecords("krishna",88,77) 










     


    

 
