n=int(input("enter n number of students:"))
n=int(input("enter roll number"))

n = int(input("Enter how many subjects : "))
total=0
result="pass"

for i in range(n):
    sub_name=input("enter subject name:")
    sub_marks=int(input("enter subject marks:"))
    marks[sub_name]=sub_marks
    total += sub_marks
    if sub_marks < 35:
        result = "Fail"
avg = total / n

print("Marks Obtained by Student : ")
print('------------------------------------------------------------------')
print('rollno     name    telugu    maths    english   hindi    social   total  average  percent ')
print('------------------------------------------------------------------')
for subjects in marks:
    print('%d    %s       %d        %d          %d          %d         %d '%(rollno and name and telugu and maths and english and hindi and socia))
print('-------------------------------------------------------------------')
print("Total Marks = ",total)
print("Average Marks = ",avg)
if result == "Fail":
    print("Sorry! You are Failed")
else:
    print("Congrats! You are Passed")
    
