import math
from Shape import Shape

class Rhombus(Shape):
    def __init__(self,diag1_t,diag2_t):
        if diag1_t > 0 and diag2_t > 0:
            super().__init__()
            self.type = "Rhombus"
            self.diag1 = diag1_t
            self.diag2 = diag2_t
        else:
            raise ValueError("Error: Invalid rhombus parameters")

    def perimeter(self):
        try:
            value =  (2 * math.sqrt(self.diag1 * self.diag1 + self.diag2 * self.diag2))
        except ValueError as error:
            print("Error: Invalid perimeter")
            return None
        else:
            return value

    def area(self):
        return (self.diag1 * self.diag2 / 2)

    def side(self):
        return (math.sqrt(self.diag1 * self.diag1 + self.diag2 * self.diag2)/2)

    def inradius(self):
        if self.perimeter() != None:
            return ((self.diag1 * self.diag2) / self.perimeter())
        else:
            return None

    def __eq__(self,other):
        if other.type == "Rhombus":
            if other.diag1 == self.diag1 and other.diag2 == self.diag2:
                return True
        return False

