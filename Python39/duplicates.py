ls1 = [10,20,30,10,40,10,20,50,30,60]
ls2 = []
print("Elements Before removing duplicates : ",ls1)
for list_item in ls1:
    if list_item not in ls2:
        ls2.append(list_item)
print("Elements after removing duplicates : ",ls2)



ls1 = [10,20,30,40,50,60]
ls2 = [5,10,15,20,25,30]

print("Elements of List-1 : ",ls1)
print("Elements of List-2 : ",ls2)
print("Common Elements of List-1 and List-2 : ",end=" ")
for list_item in ls1:
    if list_item in ls2:
        print(list_item,end="  ")
