def add(x=100,y=200):#100,200=>deafault arguments
    print("x=",x)
    print("y=",y)
    print("sum=",x+y)


add(10,20)
add(10)
add()


def add(x,y):
    print("x=",x)
    print("y=",y)
    print("sum=",x+y)

add(10,20) #Non-keyword argumens
add(x=10,y=20)#keyword arguments
add(y=10,x=20)#key word arguments
add(10,y=20)
#add(10,x=20)


def add(*x):
    total=0
    for item in x:
        total=total+item
        print("sum of given numbers:",total)


add(10,20,30)
add(10,20,30,40,50)
add(10,20,30,40,50,60,70,80,90,100)


def fact(x):
    if x==1:
        return 1
    else:
        return x * fact(x-1)

n = int(input("Enter any Number : "))
print("Factorial of given number : ",fact(n))


def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

n=int(input("enter any number:"))
for i in range(1,n+1):
    print("factorial of %dis %d"%(i,fact(i)))


a=100#global variable


def fun1():
    global a
    a=a+100
    print("value of a in fun1=",a)
def fun2():
    global a
    a=a*4
    print("value of ain fun2=",a)


def fun3():
    global a
    a=a/10
    print("value of ain fun3=",a)


print("value of a before calling functions:",a)
fun1()
fun2()
fun3()
print("value of after calling functions:",a)    
