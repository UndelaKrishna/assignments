import pickle
class Student:
    def __init__(self,sname,srno,sstream,spercentage):
        self.sname=sname
        self.srno=srno
        self.sstream=sstream
        self.spercentage=spercentage
    def studentRecords(self):
        print(self.sname,"/t",self.srno,"/t",self.sstream,"/t",self.spercentage)    


s=Student("krishna",17,"civil",68.0)
s1=Student("ramu",18,"mech",80)
s.studentRecords()
# print(s.sname)
# print(s.srno)
# print(s.sstream)
# print(s.spercentage)
# print(s)
#pickiling
with open("student.data","wb") as f:
    pickle.dump(s,f)
    pickle.dump(s1,f)
    print("pickle of student object is done")


#unpickle
with open("student.data","rb") as f:
    up=pickle.load(f)
    print("student info after the unpickiling") 
    up.studentRecords()  
    

