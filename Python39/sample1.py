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
