# Implementing Method Overriding. Implementing super() function

class A:
    def fun1(self):
        print("Inside fun1 of A")
    def fun2(self):
        print("Inside fun2 of A")

class B(A):
    def fun1(self):
        super().fun1()
        print("Inside fun1 of B")
    def fun2(self):
        super().fun2()
        print("Inside fun2 of B")

class C(B):
    def fun1(self):
        super().fun1()
        print("Inside fun1 of C")
    def fun2(self):
        super().fun2()
        print("Inside fun2 of C")

c1 = C()
c1.fun1()
c1.fun2()
print(C.mro())
================================================
# Program-1 on Multiple Inheritance

class A:
    def fun1(self):
        print("Inside fun1 of A")

class B:
    def fun2(self):
        print("Inside fun2 of B")

class C(A,B):
    def fun3(self):
        print("Inside fun3 of C")

c1 = C()
c1.fun1()
c1.fun2()
c1.fun3()
==================================================
# Program-2 on Multiple Inheritance

class A:
    def fun1(self):
        print("Inside fun1 of A")

class B:
    def fun1(self):
        print("Inside fun1 of B")

class C(A,B):
    def fun1(self):
        print("Inside fun1 of C")

c1 = C()
c1.fun1()
===================================================
#program-3 on multiple inheritance

class a:
    def fun1(self):
        print("inside fun1 of a")
class b:
    def fun1(self):
        print("inside fun1 of b")
class c(a,b):
    def fun2(self):
        print("inside fun2 of c")
c1=c()
c1.fun1()
c1.fun2()
print(c.mro())
==================================================
# Implementing Dynamic or Run-Time Polymorphism

class A:
    def fun1(self):
        print("Inside fun1 of A")
    def fun2(self):
        print("Inside fun2 of A")

class B(A):
    def fun1(self):
        print("Inside fun1 of B")
    def fun2(self):
        print("Inside fun2 of B")

class C(B):
    def fun1(self):
        print("Inside fun1 of C")
    def fun2(self):
        print("Inside fun2 of C")

ref = None
n = int(input("Enter any Number : "))
if n < 10:
    ref = A()
elif n < 20:
    ref = B()
else:
    ref = C()
ref.fun1()
ref.fun2()
