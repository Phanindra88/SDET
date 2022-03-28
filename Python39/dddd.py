#implementing dynamic or run-time polymorphism

class a:
    def fum1(self):
        print("inside fun1 of a")
    def fun2(self):
        print("inside fun2 of a")
class b(a):
    def fun1(self):
        print("inside fun1 of b")
    def fun2(self):
        print("inside fun2 of b")
class c(b):
    def fun1(self):
        print("inside fun1 of c")
    def fun2(self):
        print("inside fun2 of c")
ref=None
n=int(input("enter any number:"))
if n<10:
    ref =a()
elif n<20:
    ref =b()
else:
    ref=c()
ref.fun1()
ref.fun2()
