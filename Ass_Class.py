# Assignment 1
class BankAccount:
    def __init__(self,name,number,balance):
        self.a=name
        self.b=number
        self.c=balance
    def deposit (self,amount):
        if amount > 0:
            self.c += amount
            print(f"New Deposit has enter {self.a}'s account, balance is {self.c}")
    def withdrawl (self,amount):
        if amount >0:
            self.c -= amount
            return f"withdrawl has been succussful, {self.a}'s account balance is {self.c}"
    def checkbalance(self):
        print(f"Recent account balance is {self.c}")
        return self.c
Acct1=BankAccount(name="Aliu_Kehinde", number=9043201906,balance=10000)
Acct2=BankAccount(name="Ojo_Taiye", number='0325147700',balance=5000)
print(Acct1.deposit(1000))
print(Acct1.withdrawl(2000))
print(Acct1.checkbalance())
print(Acct2.deposit(500))
print(Acct2.withdrawl(1000))
print(Acct2.checkbalance())

# Assignment 2
class person:
    def __init__(self,name,level, department,address):
        self.a=name
        self.b=level
        self.c=department
        self.d=address
    def describe(self):
        print(f"My name is {self.a}, a {self.b} student, from the {self.c}, I live at {self.d} ")
class student(person):
    def information (self,faculty):
        self.e=faculty
        print(f" My name is {self.a}, a {self.b} student, from the {self.c}, {self.e},I live at {self.d} ")
class lecturer(person):
    def lecturer_detail(self,position):
        self.f=position
        print(f"This is Mrs {self.a}, she is a {self.f} in the {self.c}")
a1= person(name='Tayo_Oyebisi',level='400level',department='Statistics',address= 'Tanke')
a2=student(name='Lawal_Muiz',level='300level',department='Chemistry',address= 'Oke_odo')
a3= lecturer(name="Adeniyi", position= 'lecturer')
a1.describe() 

                    