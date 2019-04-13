class Cylinder():
    pi= 3.14
    def __init__(self, radius, height):
         self.radius= radius
         self.height= height

    def volume(self):
        V= self.pi*self.radius**2*self.height
        return V

    def surface_area(self):
        SA= (2*self.pi*self.radius*self.height)+(2*self.pi*self.radius**2)
        return SA

cylinder1= Cylinder(2,1)
print(cylinder1.volume())
print(cylinder1.surface_area())


class Line():

    def __init__(self,co_ord1,co_ord2):
        self.co_ord1= co_ord1
        self.co_ord2= co_ord2

    def distance(self):
        #tuple unpacking
        x1,y1= self.co_ord1
        x2,y2= self.co_ord2
        return ((x2-x1)**2+(y2-y1)**2)*0.5

    def slope(self):
        x1, y1 = self.co_ord1
        x2, y2 = self.co_ord2
        return (y2-y1)/(x2-x1)

line1= Line((3,1),(5,4))
print(line1.distance())
print(line1.slope())

