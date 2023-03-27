class Square:
    def __init__(self, base,height,length):
        self.base = base
        self.height = height
        self.length = length

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (2*self.length)+self.base

    def report(self):
        print("Base is: %s" % self.base)
        print("Height is: %s" % self.height)
        print("Length is: %s" % self.length)
        print("Area is: %s" % self.area())
        print("Perimeter is: %s" % self.perimeter())



my_square = Square(10,5,20)
print(my_square.report())