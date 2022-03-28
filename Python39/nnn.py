# Generating Hotel Bill

bill = []
total_bill = 0.0

while True:
    service = {}
    print("******************************")
    print("   WELCOME TO HOTEL NIRVANA   ")
    print("******************************")
    print("1. Idly Rs. 30.00.")
    print("2. Dosa Rs. 50.00.")
    print("3. Poori Rs. 40.00.")
    print("4. Chapati Rs. 35.00.")
    choice = int(input("Select Your Item : "))
    qty = int(input("Order No. of Plates : "))
    if choice == 1:
        bill_amt = qty * 30.00
        total_bill = total_bill + bill_amt
        service["itemname"] = "Idly"
        service["price"] = 30.00
        service["qty"] = qty
        service["bill_amt"] = bill_amt
        bill.append(service)
    elif choice == 2:
        bill_amt = qty * 50.00
        total_bill = total_bill + bill_amt
        service["itemname"] = "Dosa"
        service["price"] = 50.00
        service["qty"] = qty
        service["bill_amt"] = bill_amt
        bill.append(service)
    elif choice == 3:
        bill_amt = qty * 40.00
        total_bill = total_bill + bill_amt
        service["itemname"] = "Poori"
        service["price"] = 40.00
        service["qty"] = qty
        service["bill_amt"] = bill_amt
        bill.append(service)
    elif choice == 4:
        bill_amt = qty * 35.00
        total_bill = total_bill + bill_amt
        service["itemname"] = "Chapati"
        service["price"] = 35.00
        service["qty"] = qty
        service["bill_amt"] = bill_amt
        bill.append(service)
    else:
        print("Invalid Operion. Please Try Again.")
    ch = input("Want to Order More(Type yes/no) : ")
    if ch == "no":
        break

print("The Bill Details are : ")
sno = 1
print('------------------------------------------------')
print(' S.No   Item Name  Price  Quantity  Bill Amount')
print('------------------------------------------------')
for service in bill:
    print(" %3d    %8s  %.2f       %d       %.2f"%(sno,service["itemname"],service["price"],service["qty"],service["bill_amt"]))
    sno = sno + 1
print('------------------------------------------------')
print('Total Bill amount to be Paid(In Rs.) : %.2f'%total_bill)
gst = total_bill * 18 / 100
total_bill = total_bill + gst
print('------------------------------------------------')
print('       G.S.T(18 percent)   :     %.2f'%total_bill)
print('------------------------------------------------')
print('Final Bill amount to be Paid(In Rs.) : %.2f'%total_bill)
print('------------------------------------------------')

print("\n  *** THANK YOU. VISIT AGAIN. ***")
