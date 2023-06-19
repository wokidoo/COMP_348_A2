import math
from Shape import Shape

class Circle(Shape):
    def __init__(self,radius_t):
        if radius_t > 0:
            super().__init__()
            self.type = "Circle"
            self.radius = radius_t
        else:
            raise ValueError("Error: Invalid circle radius")

    def perimeter(self):
        return (2 * math.pi * self.radius)

    def area(self):
        return (math.pi * self.radius * self.radius)

    def __eq__(self,other):
        if other.type == "Circle":
            if other.radius == self.radius:
                return True
        return False