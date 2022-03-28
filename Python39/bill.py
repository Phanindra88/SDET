total_bill = 0.0
while True:
    print("******************************")
    print("   WELCOME TO HOTEL NIRVANA   ")
    print("******************************")
    print("1. Idly Rs. 30.00")
    print("2. Dosa Rs. 50.00")
    print("3. Poori Rs. 40.00")
    print("4. Coffee Rs. 20.00")
    choice = int(input("Select Your Item : "))
    qty = int(input("Order Quentity : "))
    if choice == 1:
        bill_amt = qty * 30.00
        total_bill = total_bill + bill_amt
    elif choice == 2:
        bill_amt = qty * 50.00
        total_bill = total_bill + bill_amt
    elif choice == 3:
        bill_amt = qty * 40.00
        total_bill = total_bill + bill_amt
    elif choice == 4:
        bill_amt = qty * 20.00
        total_bill = total_bill + bill_amt
    else:
        print("Sorry Sir! Item not Available")
    ch = input("Want to Order More(Type yes/no) : ")
    if ch == "no":
        break

print("Your Bill Amount is Rs.",total_bill)
gst = total_bill * 18 / 100
total_bill = total_bill + gst
print("G.S.T(18%) : Rs.",gst)
print("Final Bill amount to be Paid : Rs.",total_bill)
print("*** THANK YOU. VISIT AGAIN. ***")
