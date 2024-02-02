


class Employee:
    def __init__(self,enmae,esal,eid,edomain) :
        self.ename=enmae
        self.esal=esal
        self.eid=eid
        self.edomain=edomain
    def displayEmployeeDetails(self):
        print("ename=",self.ename)
        print("esal=",self.esal)
        print("eid=",self.eid)
        print("edomain=",self.edomain) 
        self.salaryDetails(12000)

    def salaryDetails(self,amount):
        if amount>0:
            self.esal+=amount 
            print(self.ename,"salary has been incresead=",self.esal)
        else:
            print("amount should be greter than zero for salary raise..")


e=Employee("krishna",10000,302,"python")
e.displayEmployeeDetails()   
# e.salaryDetails(12000) 

e1=Employee("ram",12000,123,"java")
e1.displayEmployeeDetails()
# e1.salaryDetails(5000)     





class Employee:
    enm="krishna"
    def display(self):
        print("the employee name is",self.enm)
        # print("the employee name is",Employee.enm)

# print(Employee.enm)
e=Employee()
# print(e.enm)
e.display()  






class Student:
    sclgnm="vikas"
    def __init__(self,sname,srno,sage):
        self.sname=sname
        self.srno=srno
        self.sage=sage

        self.display()
    def display(self):
        print("clgnm is",self.sclgnm,"sname is ",self.sname,"srno is",self.srno,"sage is",self.sage) 
s=Student("krishna",12,24)
# s.display()        







class Test:
    z=10
    def m1(self):
        self.a=100
        a=200
        print(a)
    def m2(self):
        self.b=100
        b=133
        a=444
        print(b) 
        print(a)  
        print(self.a)
t=Test()
t.m1()
t.m2()  








class Test:
    z=10
    def m1(self):
        self.a=100
        a=200
        print(a)
    def m2(self):
        self.b=100
        b=133
        a=444
        print(b) 
        print(a)  
        print(self.a)
t=Test()
t.m1()
t.m2()  

print(t.z)  
print(Test.z)    








class  Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=800
        a=199
        print(b) 
        print(a) 
t=Test()
t.m1()
t.m2()          


       






        
