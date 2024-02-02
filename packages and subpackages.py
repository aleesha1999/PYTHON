import graphics.circle
import graphics.rectangle
import graphics.graphics3d.cuboid
import graphics.graphics3d.sphere
r=int(input("Enter the radius of circle-"))
r1=int(input("Enter the radius of sphere_"))
leng=int(input("Enter the lenght of rectangle_"))
bread=int(input("Enter the  breadth of rectangle_"))
lenght=int(input("Enter the lenght of cuboid"))
height=int(input("Enter the height of  cuboid"))
width=int(input("Enter the width of cuboid"))
print("Area of circle is:",graphics.circle.area(r))
print("perimeter of rectangle is:",graphics.rectangle.perimeter(leng,bread))
print("Area of rectangle is:",graphics.rectangle.area(leng,bread))
print("Perimeter of rectangle is:", graphics.rectangle.perimeter(leng,bread))
print("Area of cuboid is :", graphics.graphic3d.cuboid.area(lenght,width, height))
print("perimeter of cuboid  is: ", graphics.graphics3d.cuboid.perimetr(lenght, width,height))
Print("Area of sphere is:",graphics3d.sphere.area(r1))
print("perimeter of sphere is:",graphics.graphics3d.sphere.perimeter(r1))
def area(leg,bread):
    return (leg*bread)
    def perimeter(leg,bread):
        return  2*(leng+bread)
    import math
    def area(r):
        return math.pi*r*r
        def perimeter(r):
            return 2*math.pi*r
        import math
        def area(r):
            return4* math .pi*r
            def perimetr(r):
                return 2*math.pi*r

            def area(lenght, width,height):
                return 2*(lenght*width)+(lenght*height)+(width*height)
            return 4*(lenght+ width+height)
    


                 
