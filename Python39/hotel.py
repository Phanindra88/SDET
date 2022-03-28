total_bill=0.0
while True:
    print("***************************")
    print("   WELCOME TO HOTEL RAJ   ")
    print("***************************")
    print("1.Docdhum biriyani Rs.300.00")
    print("2.mutton biriyani Rs.450.00")
    print("3.prawns biriyani Rs.500.00")
    print("4.tandhoori RS.500.00")
    print("5.ulavacharu biriyani Rs.550.00")
    choice=int(input("select your item:"))
    qty=int(input("order quantity:"))
    if choice==1:
        bill_amt=qty*300.00
        total_bill=total_bill+bill_amt
    elif choice==2:
        bill_amt=qty*450.00
        total_bill=total_bill+bill_amt
     
    elif choice==3:
        bill_amt=qty*500.00
        total_bill=total_bill+bill_amt
    
    elif choice==4:
        bill_amt=qty*500.00
        total_bill=total_bill+bill_amt
     
    elif choice==5:
        bill_amt=qty*550.00
        total_bill=total_bill+bill_amt
    else:
        print("sorry sir!items not available")
    ch = input("Want to Order More(Type yes/no) : ")
    if ch == "no":
        break

print("Your Bill Amount is Rs.",total_bill)
gst = total_bill * 18 / 100
total_bill = total_bill + gst
print("G.S.T(18%) : Rs.",gst)
print("Final Bill amount to be Paid : Rs.",total_bill)
print("***THANK YOU .VISIT AGAIN.***")   
   
