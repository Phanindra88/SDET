#creating a class with multiple methods

class sample:
    def __init__(self):
        print("inside constructor")
        self.a=100
        self.b=50
    def add(self):
       print("sum=",self.a+self.b)
    def sub(self):
       print("difference=",self.a-self.b)
    def mul(self):
        print("product=",self.a*self.b)
    def div(self):
        print("division=",self.a/self.b)


s1=sample()
s1.add()
s1.sub()
s1.mul()
s1.div()
================================================
#implementing a non-parameterized constructor


class account:
    def __init__(self):
        self.accno=201
        self.balance=10000.00
    def showbalance(self):
        print("balance in %d is:%.2f"%(self.accno,self.balance))

a1=account()
a1.showbalance()
====================================================
#implementing a  non-parameterized constructor

class account:
    def __init__(self):
        self.accno=int(input("enter account number:"))
        self.balance=float(input("enter starting balance:"))
    def showbalance(self):
        print("balance in%dis :%.2f"%(self.accno,self.balance))

a1=account()
a2=account()
a3=account()
a1.showbalance()
a2.showbalance()
a3.showbalance()
======================================================
#implementing a parameterised constructor


class account:
    def __init__(self,x,y):
        self.accno=x
        self.balance=y
    def showbalance(self):
        print("balance in %d is :%.2f"%(self.accno,self.balance))
    
a1=account(201,1000000.00)
a2=account(202,3000000.00)
a3=account(203,4500000.00)
a1.showbalance()
a2.showbalance()
a3.showbalance()
======================================================
# implementing a parameterized constructor


class account:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
    def showbalance(self):
        print("balance in %d is:%.2f"%(self.accno,self.balance))

a1=account(201,1000000.00)
a2=account(202,1000000.00)
a3=account(203,3450000.00)
a1.showbalance()
a2.showbalance()
a3.showbalance()
=====================================================
# Implementing method overloading

class Sample:
    def display(self):
        print("Inside display with 0 parameters")
    def display(self,x):
        print("Inside display with 1 parameters")
    def display(self,x,y):
        print("Inside display with 2 parameters")

s1 = Sample()
s1.display(10,20)
s1.display(10,40)
========================================================

        
