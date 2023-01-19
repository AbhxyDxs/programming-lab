class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        return area
    
    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        return perimeter

    
length1 = int(input("Enter Length-Rectangle 1  : "))
breadth1 = int(input("Enter Breadth-Rectangle 1 : "))

length2 = int(input("Enter Length-Rectangle 2  : "))
breadth2 = int(input("Enter Breadth-Rectangle 2 : "))

ob1 = Rectangle(length1, breadth1)
ob2 = Rectangle(length2, breadth2)

area1 = ob1.area()
perimeter1 = ob1.perimeter()

area2 = ob2.area()
perimeter2 = ob2.perimeter()

print("\nArea-Rectangle 1 : ", area1)
print("Perimeter-Rectangle 1 : ", perimeter1)

print("Area-Rectangle 2 : ", area2)
print("Perimeter-Rectangle 2 : ", perimeter2)

if area1 == area2:
    print("\nRectangle Areas are Equal ")
else:
    if area1 < area2:
        print("\nArea of Rectangle 2 is Greater")
    else:
        print("\nArea of Rectangle 1 is Greater ")



