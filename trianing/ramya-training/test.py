class Rectangle:
    type = "Polygon"

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return f"perimeter of the rectangle is {2 * (self.length + self.breadth)}cm."

    @property
    def area(self):
        return f"area of the rectangle is {self.length * self.breadth}sqcm"


r = Rectangle(10, 5)

print(r.perimeter)  # address of perimeter function
print(r.perimeter())


# decorated with property decorator --> # FuncName = returned value
# its not holding the address anymore, so cannot call

print(r.area())  # str not callable
print(r.area)


# print(r.length)  # 10
# print(r.type)