a,b,c,d,e = eval(input("Enter any 5 numbers:"))
if a>b and a>c and a>d and a>e:
    print(a,"is big")
elif b>c and b>d and b>e:
    print(b,"is big")
elif c>d and c>e:
    print(c,"is big")
elif d>e:
    print(d,"is big")
else:
    print(e,"is big")
    
