ls =[10,20,30,40,50,60,70,80,90]
num=int(input("enter an element to search:"))
found=False


for list_item in ls:
    if list_item==num:
        found=True
        break
if found==True:
    print("searching element found in the list:")
else:
    print("searching element not found in list:")
print ("to display the index when found the value:")
