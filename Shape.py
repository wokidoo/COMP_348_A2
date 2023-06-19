
class Shape:
    count = 0

    def __init__(self):
            self.type = "Shape"
            Shape.count += 1
            self.id = Shape.count

    def perimeter(self):
        return "undefined"

    def area(self):
        return "undefined"

    def print(self):
        print(str(self.id)+": "+self.type+", perimeter: "+str(self.perimeter())+", area: "+str(self.area()),end="")

    def __eq__(self,other):
        if other.type == self.type:
            return True
        else:
            return False
