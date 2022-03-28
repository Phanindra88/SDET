m1=int(input("Enter the marks of telugu :"))
m2=int(input("Enter the marks of hindi :"))
m3=int(input("Enter the marks of english :"))
m4=int(input("Enter the marks of maths :"))
m5=int(input("Enter the marks of science :"))
m6=int(input("Enter the marks of social :"))
total=m1+m2+m3+m4+m5+m6
avg=total/6
percentage=total/600*100
if m1>=35 and m2>=35 and m3>=35 and m4>=35 and m5>=35 and m6>=35:
       print('you have passed')
else:
       print('you have failed')

print(" the total marks is:",total,"/600")
print(" average marks is :",avg)
print("percentage is:",percentage)
