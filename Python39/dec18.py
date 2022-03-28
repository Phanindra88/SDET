a=int(input("enter first number:"))
b=int(input("enter first number:"))
try:
    c=a/b
    print("division=",c)
except(ZeroDivisionError):
    print("exception raised")
    print("division by zero error")
c=a+b
print("sum=",c)
c=a-b
print("difference=",c)
c=a*b
print("product=",c)
=====================================
ls=[10,20,30,40,50]
index=int(input("enter the index of element to print:"))
try:
    print("element at given index:",ls[index])
except(IndexError):
    print("invalid index.try again.")
    print("end of program")
=======================================
filename=input("enter the file name to read:")
try:
    file_obj=open(filename)
    print("contents of given files are:",file_obj.read())
    file_obj.close()
except(FileNotFoundError):
    print("invalid file name or path")
    print("end of program")
=========================================


