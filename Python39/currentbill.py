pres=int(input("enter present reading:"))
prev=int(input("enter previous  reading:"))
no_units=pres-prev
unit_price=4
bill_amnt=no_units * unit_price
print("no.of units consumed:",no_units)
print("price(per unit):",unit_price)
print("bill amount to be paid:",bill_amnt)
