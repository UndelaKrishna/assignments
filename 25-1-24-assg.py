


#1.Create a Class with instance attributes
class Car:
    def __init__(self,cname,ccolor,cprice,cmodel):
        self .cname=cname
        self.ccolor=ccolor
        self.cprice=cprice
        self.cmodel=cmodel
 #2. Create a Vehicle class without any variables and methods       
class Vehicle:
    pass
#3.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class  Bus(Vehicle):
    pass

c1=Car("toyata camry","black",70000,2022)
c2=Car("volvo","red",80000,2021)


print("*********Car1Details*********************")
print("cname=",c1.cname)
print("ccolor=",c1.ccolor)
print("cprice=",c1.cprice)
print("cmodel=",c1.cmodel)


print("*********Car2Details*********************")
print("cname=",c2.cname)
print("ccolor=",c2.ccolor)
print("cprice=",c2.cprice)
print("cmodel=",c2.cmodel)

b=Bus()






   