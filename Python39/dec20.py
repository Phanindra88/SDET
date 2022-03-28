#handling nested exceptions

try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    try:
        c=a/b
        print("division=",c)
    except(ZeroDivisionError):
        print("inside inner try_except block")
        print("division by zero error")
    c=a+b
    print("sum=",c)
    c=a-b
    print("difference=",c)
    c=a*b
    print("product=",c)
except(ValueError):
    print("inside outer try_except block")
    print("input must be an integer")
=============================================
#implementing finally block

try:
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    c=a/b
    print("division=",c)
except:
    print("input must be a non-zero integer")
finally:
    print("inside finally block")
===============================================
#implementing user-defined exceptions

class InvalidReadingException(Exception):
    """this is a user-defined exception class"""

pres=int(input("enter present reading:"))
prev=int(input("enter previous reading:"))
try:
    if pres<=prev:
        raise InvalidReadingException
    no_units=pres-prev
    if no_units<100:
        unit_price=2.15
    elif no_units<200:
        unit_price=2.65
    else:
       unit_price=3.25
    bill_amt=no_units*unit_price
    print("no.of units consumed:",unit_price)
    print("price(per u it):",unit_price)
    print("bill amount to be paid:",bill_amt)
except(InvalidReadingException):
       print("exception raised")
       print("present reading must be greater than previous")
=========================================================
