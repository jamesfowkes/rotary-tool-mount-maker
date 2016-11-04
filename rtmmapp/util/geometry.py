from collections import namedtuple

import math

class Point(namedtuple("Point", ["x", "y"])):

    __slots__ = ()
    
    def __str__(self):
        return str(self.x) + "," + str(self.y) 
    
    def svg(self, units="mm", mirror = 0):
        
        if mirror != 0:
            y = (2 * mirror) - self.y
        else:
            y = self.y
        
        return ("{}{}".format(self.x, units), "{}{}".format(y, units))

    def rotate(self, origin, degrees=None, radians=None):

        if degrees is None and radians is None:
            return self

        angle = radians or math.radians(degrees)

        ox, oy = origin.x, origin.y
        px, py = self.x, self.y

        qx = ox + math.cos(angle, ) * (px - ox) - math.sin(angle, ) * (py - oy)
        qy = oy + math.sin(angle, ) * (px - ox) + math.cos(angle, ) * (py - oy)
        return Point(qx, qy)
    
class Dimension(namedtuple("Dimension", ["w", "h"])):
    __slots__ = ()
    def __str__(self):
        return str(self.w) + " x " + str(self.h)

    def svg(self, units="mm"):
        return ("{}{}".format(self.w, units), "{}{}".format(self.h, units))

Circle = namedtuple("Circle", ["x", "y", "r"])
