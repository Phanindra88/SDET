# Implementing Iterator

class Square:
    def __init__(self,x):
        self.max = x
    def __iter__(self):
        self.ctr = 1
        return self
    def __next__(self):
        if self.ctr <= self.max:
            result = self.ctr * self.ctr
            self.ctr = self.ctr + 1
            return result
        else:
            raise StopIteration

s1 = Square(5)
res = s1.__iter__()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())

s1 = Square(10)
for res in s1:
    print(res)


def display():
    print("Line 1 printed")
    return 1
    print("Line 2 printed")
    return 2
    print("Line 3 printed")
    return 3
    print("Line 4 printed")
    return 4
    print("Line 5 printed")
    return 5

print(display())
print(display())
print(display())
print(display())
print(display())


def display():
    print("Line 1 printed")
    yield 1
    print("Line 2 printed")
    yield 2
    print("Line 3 printed")
    yield 3
    print("Line 4 printed")
    yield 4
    print("Line 5 printed")
    yield 5

d1 = display()
res = iter(d1)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))

d1 = display()
for res in d1:
    print(res)

# Implementing Generators

def display(max):
    ctr = 1
    while ctr <= max:
        res = ctr * ctr
        yield res
        ctr = ctr + 1

d1 = display(5)
res = iter(d1)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))

d1 = display(10)
for res in d1:
    print(res)


# Factorial using Recursion

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

n = int(input("Enter any Number : "))
print("Factorial of Given Number : ",fact(n))


#biggest of 3numbers

def big(x,y,z):
    if x>y and x>z:
        return x
    elif  y>z:
        return y
    else:
        return z
a,b,c=eval(input("enter any 3 numbers:"))
print("biggest of 3 numbers:",big(a,b,c))
