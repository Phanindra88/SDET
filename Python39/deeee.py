import math
n=int(input("enter any number:"))
print("number upto given numbers:")
i=1
while i<=n:
    print(i,end="  ")
    i=i+1
    print("\n")
print("squares of numbers upto given numbers are:")
i=1
while i<n:
    print(i*i,end="   ")
    i=i+1
    print("\n")
print("cubes of numbers upto given numbers are:")
i=1
while i<n:
    print(i*i*i,end=" ")
    i=i+1
    print("\n")
i=1
while i<=n:
    print("square root of %d is %f"%(i,math.sqrt(i)))
    i=i+1
    print("\n")
i=1
while i<=n:
    print("factorial of %d is %d"%(i,math.factorial(i)))
    i=i+1
    print("\n")
    


    
