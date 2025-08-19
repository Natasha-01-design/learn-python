class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
         print(f"this shape is called {self.name}")
    # def formulas(self,r):
    #     self.r=r
    #     if self.name == "circle":
    #         calculate=(22/7)*r*r
    #         return calculate
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__("rectangle")
        self.length=length
        self.width=width
    def area(self):
        a=self.width*self.length
        print("area is",a)
        return a
        

        
shape1=Shape(name="circle")
shape1.describe()
shape3=Rectangle(10,15)
shape3.area()
