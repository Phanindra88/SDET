pur_amt=float(input("enter purcgase amount"))
discount=pur_amt * 20/100
gst=pur_amt *18/100
bill_amt=pur_amt-discount+gst


print("you purchased for Rs.%.2f"%pur_amt)
print("your discount isRs.%.2f"%discount)
print("you gst is Rs.%.2f"%gst)
print("you have tonpay Rs.%.2f"%bill_amt)
