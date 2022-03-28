n=int(input("Enter n no. ofstudents"))
m1,m2,m3,m4,m5,m6=eval(input("Enter marks of 5 subjects:"))
print("upto to given numbers")
total=m1+m2+m3+m4+m5+m6
avg=total/6
attend_count=0
pass_count=0
fail_count=0
print("total marks=",total)
print("avg marks=",avg)
if m1>=35 and m2>=35 and m3>35 and m4>=35 and m5>=35 and m6>=35:
    print("congrats!your are passed")
    print("number of students passed=",pass_count)
else:
    print("sorry!your are failed")
    print("number of students failed=",fail_count)

