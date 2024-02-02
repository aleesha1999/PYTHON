from  graphics import circle
from  graphics  import rectangle
from  graphics.graphics3d import cuboid
from  graphics.graphics3d import sphere
r=int(input("Enter the radius of circle-"))
r1=int(input("Enter the radius of sphere_"))
leng=int(input("Enter the lenght of rectangle_"))
bread=int(input("Enter the  breadth of rectangle_"))
length=int(input("Enter the lenght of cuboid_"))
height=int(input("Enter the height of  cuboid_"))
width=int(input("Enter the width of cuboid_"))
print("Area of circle is:",circle.area(r))
print("perimeter of circle is:",circle.perimeter(r))
print("Area of rectangle is:",rectangle.area(leng,bread))
print("Perimeter of rectangle is:",rectangle.perimeter(leng,bread))
print("Area of cuboid is :", cuboid.area(length,width, height))
print("perimeter of cuboid  is: ", cuboid.perimeter(length, width,height))
print("Area of sphere is:",sphere.area(r1))
print("perimeter of sphere is:",sphere.perimeter(r1))

    

         
