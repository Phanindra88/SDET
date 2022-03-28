#creating a class with multiple methods
class sample:
    def add(self):
        self.a=100
        self.b=40
        print("sum=",self.a+self.b)
    def sub(self):
        print("difference=",self.a-self.b)
    def mul(self):
        print("product=",self.a*self.b)
    def div(self):
        print("division=",self.a/self.b)

s1=sample()
s1.add()
s1.sub()
s1.mul()
s1.div()
        
