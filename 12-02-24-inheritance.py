
# #single level inheritance-->inheriting properities from one class to another class
class P:
    def m1(self):
        print("this is parent class")

class C(P):
    def m2(self):
        print("this is child class")

c=C()
c.m2()
c.m1()




class P:
    snm="pawan"
    def m1(self):
        print(self.snm)
     
        print("this is parent class")

class C(P):
    def m2(self):
        print("this is child class")

c=C()
c.m2()
c.m1()
print(P.snm)





class Employee:
    def __init__(self,eno,eid,esal,ecnm) :
        self.eno=eno
        self.eid=eid
        self.esal=esal
        self.ecnm=ecnm

    def display(self):
        print("eno=",self.eno)
        print("eid=",self.eid)
        print("esal=",self.esal)
        print("ecnm=",self.ecnm)  
      

class A(Employee):
    def __init__(self, eno, eid, esal, ecnm,edomain):
        self.eno=eno
        self.eid=eid
        self.esal=esal
        self.ecnm=ecnm
        self.edomain=edomain     
    def b(self):
        Employee.display(self)
        print("edomain=",self.edomain)

a=A(121,1230,123645,"hp1","java")  
# a.display()
a.b()






#multilevel-inheritances-->

class A:
    def m1(self):
        print("this is parent class")
class B(A):
    def m3(self):
        print("this is Intermedaite class")
class c(B):
    def m2(self):
        print("this is child class")

c=c()   
c.m1()
c.m2()  
               
            



class A:
    a=100
    def m1(self):
        print(self.a)
        print("this is parent class")
class B(A):
    a=77
    def m3(self):
        print("this is Intermedaite class")
class c(B):
    def m2(self):
        print("this is child class")

c=c()   
c.m1()
c.m2()
c.m3()
print(A.a)
c.a=900
print(c.a)
print(c.__dict__)





class A:
    id=103
    def m1(self,a,b):
        self.a=a
        self.b=b
        print(self.id)

    def display(self):
        print(self.a)
        print(self.b)    
        print("this is parent class")
class B(A):
    def m3(self):
        print("this is Intermedaite class")
class c(B):
    def m2(self):
        print("this is child class")

c=c()   
c.m1(100,900)
c.display()
c.m3()
c.m2()
print(c.__dict__) 




# #multiple-inheritance-->f parent class is multiple but one child class
class p1:
    def m1(self):
        print("parent 1")

class p2:
    def m2(self):
        print("parent 2")

class c(p1,p2):
    def m3(self):
        print("child") 


c=c()
c.m1()
c.m2()
c.m3()
 



class p1:
    def m1(self):
        self.nm="krishna"
        self.id=122
        self.phno=9890

    def d(self):
        print("name=",self.nm)
        print("id=",self.id)
        print("phno=",self.phno)    
        print("parent 1")

class p2:
    def m2(self):
        print("parent 2")

class c(p1,p2):
    def m3(self):
        print("child") 


c=c()
c.m1()
c.d()
c.m2()
c.m3()
print(c.__dict__)
 

 


class p1:
    no=999
    def m1(self):
        self.nm="krishna"
        self.id=122
        self.phno=9890

    def d(self):
        print("no =",p1.no,"----","nm=",self.nm,"---","id=",self.id,"------","phno=",self.phno)   
        print("parent 1")

class p2:
    def m2(self):
        print("parent 2")

class c(p1,p2):
    def m3(self):
        print("child") 


c=c()
c.m1()
c.d()
c.m2()
c.m3()
print(c.__dict__)





# #hierarchical ->single parent but mutiple childs
class p:
    def m1(self):
        print("parent")

class c1(p):
    def m2(self):
        print("child 1")

class c2(p):
    def m3(self):
        print("child 2")

c1=c1()
c1.m2()
c1.m1()


c2=c2()
c2.m1()
c2.m3()






class p:
    def m1(self,a,b):
        self.a=a
        self.b=b
        print("parent")

    def display(self):
        print(self.a)
        print(self.b)     

class c1(p):
    def m2(self):
        print("child 1")

class c2(p):
    def m3(self):
        print("child 2")

c1=c1()
c1.m2()
c1.m1(122,455)
c1.display()


c2=c2()
c2.m1(400,900)
c2.display()
c2.m3()






class p:
    name="ram"
    def m1(self,a,b):
        self.a=a
        self.b=b
        print(self.name)
        print("parent")

    def display(self):
        print(self.a)
        print(self.b)     

class c1(p):
    def m2(self):
        print("child 1")

class c2(p):
    def m3(self):
        print("child 2")

c1=c1()
c1.m2()
c1.m1(122,455)
c1.display()


c2=c2()
c2.m1(400,900)
c2.display()
c2.m3()
print(c2.name)
print(p.name)
print(c2.__dict__)

c2.name="krishna"
print(c2.name)
print(c2.__dict__)



 

 




