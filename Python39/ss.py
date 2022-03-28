ls1 = [10,20,30,40,50]
ls2 = [10,20,30,40,50]
ls3 = [60,70,80]
ls1.append(ls3)
ls2.extend(ls3)
print("Appended List : ",ls1)
print("Extended List : ",ls2)
ls1 = [10,20,30,40,50]
ls2 = [10,20,30,40,50]
ls3 = [60,70,80]
ls1.append(ls3)
print("Appended List : ",ls1)
for list_item in ls3:
    ls2.append(list_item)
print("Extended List : ",ls2)
