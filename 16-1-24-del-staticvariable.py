
# delete of static variable


class student:
    a=10
    @classmethod
    def m2(cls):
        del cls.a

student.m2()
print(student.__dict__)




class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=60
        
t=Test()
t.m1()
t.m3()
print(Test.__dict__)




class Test:
    a=10
    def __init__(self):
        Test.b=20
        del Test.a
    def m1(self):
        Test.c=30
        del Test.b
    @classmethod
    def m2(cls):
        cls.d=677
        del Test.c
    @staticmethod
    def m3():
        Test.r=60
    
t=Test()
t.m1()
t.m2()
t.m3()
print(Test.__dict__)









class Bank_Account:
    def __init__(self) :
        self.balance=0
        print("Helloo!!! welcome to the Deposit & withdraw Machine")
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance+=amount
        print("\n You Deposited:",amount) 
    def withdraw(self):
        amount=float(input("Enter amount to be withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdraw:",amount)
        else:
            print("\n Insufficent Balance")      
    def display(self):
        print("\n Net AVailable Balance=",self.balance)  

b=Bank_Account()
b.deposit()
b.withdraw()
b.display()
               


 
    