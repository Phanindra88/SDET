a,b=10,20
def fun1():
    print("inside fun1 of module1")
def fun2():
    print("inside fun2 of module1")


c,d=30,40
def fun3():
    print("inside fun3 of module2")
def fun4():
    print("inside fun4 of module2")


#importing the package members using normal import



import main_pack.module1
import main_pack.sub_pack.module2


print("a=",main_pack.module1.a)
print("b=",main_pack.module1.b)
main_pack.module1.fun1()
main_pack.module1.fun2()

print("c=",main_pack.sub_pack.module2.c)
print("d=",main_pack.sub_pack.module2.d)
main_pack.sub_pack.module2.fun3()
main_pack.sub_pack.module2.fun4()



#importing the package members by renaming them
import main_pack.module1 as mm
import main_pack.sub_pack.module2 as msm


print("a=",mm.a)
print("b=",mm.b)
mm.fun1()
mm.fun2()

print("c=",msm.c)
print("d=",msm.d)
msm.fun3()
msm.fun4()


#importing the package members using from  import with *option


from main_pack.module1 import*
from main_pack.sub_pack.module2 import*


print("a=",a)
print("b=",b)
fun1()
fun2()


print("c=",c)
print("d=",d)
fun3()
fun4()



#importing selected package members using from import option

from main_pack.module1 import a,fun1
from main_pack.sub_pack.module2 import d,fun4


print("a=",a)
fun1()
print("d=",d)
fun4()




#writib(storing)data into afile(in write mode)

file_obj=open("sample.txt","w")
data=input("type some text:")
file_obj.write(data)
file_obj.close()
print("file created sucessfully")


#writing(storing) data into a file (in append mode)


file_obj=open("sample.txt","a")
data=input("type some text:")
file_obj.write(data)
file_obj.close()
print("file created sucessfully")


#writing(storing) data into a file(in exclusive mode)


file_obj=open("simple.txt","x")
data=input("type some text:")
file_obj.write(data)
print("file created sucessfully")



#reading (retrieving)data from afile

fil_obj=open("sample.txt")
data=file_obj.read()
file_obj.close()
print("contents of given files are:",data)
print("size of file:",len(data))
print("no.of words in file:",len(data.split()))




#reading (retrieving)data from afile


filename=input("enter the file name to read:")
file_obj=open(filename)
data=file_obj.read()
file_obj.close()
print("contents of given file are:",data)
