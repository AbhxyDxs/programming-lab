#from graphics import circle
#from graphics import rectangle
#from graphics.threeD_graphics import sphere
#from graphics.threeD_graphics import cuboid

from graphics import *
from graphics.threeD_graphics import *

r=int(input("Enter Radius of Circle : "))

l=int(input("Enter Length of Rectangle : ")) 
b=int(input("Enter Breadth of Rectangle : "))

p=int(input("Enter Length of Cuboid : "))
q=int(input("Enter Breadth of Cuboid : "))
r=int(input("Enter Height of Cuboid : "))

x=int(input("Enter Radius of Sphere : "))


circle.cArea(r)
circle.cPerim(r)
rectangle.rArea(l,b)
rectangle.rPerim(l,b)

cuboid.cubArea(p,q,r)
cuboid.cubPerim(p,q,r)
sphere.sArea(x)
sphere.sPerim(x)

