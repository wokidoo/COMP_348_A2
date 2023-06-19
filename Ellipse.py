import math
from Shape import Shape

class Ellipse(Shape):
    def __init__(self,major_t,minor_t):
        if major_t > 0 and minor_t > 0:
            super().__init__()
            self.type = "Ellipse"
            self.major = major_t
            self.minor = minor_t
        else:
            raise ValueError("Error: Invalid ellipse parameters")

    def area(self):
        return (math.pi * self.major * self.minor)

    def eccentricity(self):
        try:
            value = math.sqrt(self.minor * self.minor - self.major * self.major)
        except ValueError as error:
            print("Error: Invalid eccentricity for shape: "+ self.type)
            return None
        else:
            return value

    def __eq__(self,other):
        if other.type == "Ellipse":
            if other.major == self.major and other.minor == self.minor:
                return True
        return False