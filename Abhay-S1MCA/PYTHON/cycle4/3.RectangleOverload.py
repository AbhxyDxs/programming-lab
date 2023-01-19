class Rectangle:
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    

    def __lt__(self, other):
        area1 = self.__length*self.__width
        area2 = other.__length * other.__width
        if area2 < area1 :
            print("Rectangle 1 is Large")
        elif area1 < area2:
            print("Rectangle 2 is Large")
        else:
            print("Both Rectangle have Equal Area")

length1 = int(input("Enter The Length of Rectangle 1  : "))
width1 = int(input("Enter The Breadth of Rectangle 1 : "))

length2 = int(input("Enter The Length of Rectangle 2  : "))
width2 = int(input("Enter The Breadth of Rectangle 2 : "))

rect1 = Rectangle(length1, width1)
rect2 = Rectangle(length2, width2)

rect1 < rect2
