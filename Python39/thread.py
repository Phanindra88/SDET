#program to demonstrate threads

from threading import Thread

class A(Thread):
    def run(self):
        print("inside Thread A")
        for i in range(1,11):
            print("thread A executed %d times "%i)

class B(Thread):
    def run(self):
        print("inside Thread b")
        for i in range(1,11):
            print("Thread b executed %d times"%i)

class C(Thread):
    def run(self):
        print("inside Thread c")
        for i in range(1,11):
            print("Thread Cexecuted %d times "%i)

a1=A()
b1=B()
c1=C()
a1.start()
b1.start()
c1.start()
print("inside thread main")
for i in range(1,11):
    print("thread main executed %d times "%i)
