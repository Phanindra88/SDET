total_bill=0.0
while True:
    print("******************************")
    print("   WELCOME TO HOTEL TAJ MAHAL   ")
    print("******************************")
    print("1. dum biriyani Rs. 250.00")
    print("2. mutton biriyani Rs. 300.00")
    print("3. prawns biriyanai Rs. 400.00")
    print("4. ulavacharu biriyaniRs. 500.00")
    choice = int(input("Select Your Item : "))
    qty = int(input("Order Quentity : "))
    if choice == 1:
        bill_amt = qty * 250.00
        total_bill = total_bill + bill_amt
    elif choice == 2:
        bill_amt = qty * 300.00
        total_bill = total_bill + bill_amt
    elif choice == 3:
        bill_amt = qty * 400.00
        total_bill = total_bill + bill_amt
    elif choice == 4:
        bill_amt = qty * 500.00
        total_bill = total_bill + bill_amt
    else:
        print("Sorry Sir! Item not Available")
    ch = input("Want to Order More(Type yes/no) : ")
    if ch == "no":
        break
print("Hotel Bill:")
print("-------------------------------------------")
print("S.No ItemName price  no_plates  bill_amt")
print("-------------------------------------------")

print("Your Bill Amount is Rs.",total_bill)
gst = total_bill * 18 / 100
total_bill = total_bill + gst
print("G.S.T(18%) : Rs.",gst)
print("Final Bill amount to be Paid : Rs.",total_bill)
print("*** THANK YOU. VISIT AGAIN. ***")

