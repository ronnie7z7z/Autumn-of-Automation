class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def display(self):
        print(str(self.r)+' '+str(self.i)+'i')

    def conjugate(self):
        self.i=-self.i
        return self
    
    def modulus(self):
        return (self.r*self.r+self.i*self.i)**0.5

    def inverse(self):
        self.r=self.r/(self.r*self.r+self.i*self.i)
        self.i=-self.i/(self.r*self.r+self.i*self.i)
        return self

    def add(self, other):
        self.r += other.r
        self.i += other.i
        return self

    def sub(self, other):
        self.r -= other.r
        self.i -= other.i
        return self
    
    def multiply(self, other):
        self.r = self.r*other.r - self.i*other.i
        self.i = self.r*other.i + self.i*other.r
        return self


a = Complex(1,2)
a.display()
b = Complex(2,-3)
c = b.add(a)
c.display()
c.conjugate().display()
a.multiply(c).display()
print(c.modulus())
b.inverse().display()
c.sub(a).display()


    