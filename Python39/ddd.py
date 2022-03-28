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
