#implementing destructor

class sample:
    def __init__(self):
        print("inside constructor")
    def display(self):
        print("inside display")
    def __del__(self):
        print("inside destructor")



s1=sample()
s1.display()
print("s1=",s1)

s1=sample()
s1.display()
print("s1=",s1)
=================================================
#dyanmically adding and removing attributes of a class

class sample:
    a=100
    def __init__(self):
        self.b=200


s1=sample()
print("static data member a=",sample.a)
print("non_static data member b=",s1.b)

sample.c=300
s1.d=400
print("static data member c=",sample.c)
print("non-static data member d=",s1.d)
===================================================
#implementing single inheritance

class a:
    def fun1(self):
        print("inside fun1 of a")
    def fun2(self):
       print("inside fun2 of a")


class b(a):
   def fun3(self):
       print("inside fun3 of b")
   def fun4(self):
       print("inside fun4 of b")


b1=b()
b1.fun1()
b1.fun2()
b1.fun3()
b1.fun4()
=================================================
#implementing multi-level inheritance

class a:
    def fun1(self):
        print("inside fun1 of a")
    def fun2(self):
        print("inside fun2 of a")

class b(a):
    def fun3(self):
        print("inside fun3 of b")
    def fun4(self):
        print("inside fun4 of b")

class c(b):
    def fun5(self):
        print("inside fun5 of c")
    def fun6(self):
        print("inside fun6 of c")

c1=c()
c1.fun1()
c1.fun2()
c1.fun3()
c1.fun4()
c1.fun5()
c1.fun6()
==============================================
