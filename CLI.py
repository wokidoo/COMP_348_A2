import Shape
import Circle
import Ellipse
import Rhombus

class CLI:

    def __init__(self):
        self.set = None
        self.userInput = []
        self.fileName = ""
        self.quitting = False

    def run(self):
        while self.quitting == False:
            userInput = input("Enter command: ").split()

            if userInput[0] == "PRINT":
                self.PRINT()
            elif userInput[0] == "LOAD":
                self.set = self.LOAD(userInput[1])
            elif userInput[0] == "SUMMARY":
                self.SUMMARY()
            elif userInput[0] == "TOSET":
                self.TOSET()
            elif userInput[0] == "DETAILS":
                self.DETAILS()
            elif userInput[0] == "SAVE":
                self.SAVE(userInput[1])
            elif userInput[0] == "QUIT":
                self.QUIT()
                self.quitting = True
                break
            else:
                print("Invalid Input: "+userInput[0])


    def LOAD(self,file):
        print("Processing <<"+str(file)+">>")
        tempList = []
        try:
            with open(file, 'r') as file:
                strings = [line.strip() for line in file]
        except:
            print("Cannot open: "+file)
            return
        errorCount = 0
        lineNum = 0
        for line in strings:
            try:
                elements = line.strip().split()
                if elements[0] == "shape":
                    lineNum +=1
                    tempList.append(Shape.Shape())
                elif elements[0] == "circle":
                    lineNum += 1
                    tempList.append(Circle.Circle(int(elements[1])))
                elif elements[0] == "rhombus":
                    lineNum += 1
                    rho = Rhombus.Rhombus(int(elements[1]), int(elements[2]))
                    tempList.append(rho)
                elif elements[0] == "ellipse":
                    lineNum += 1
                    ell = Ellipse.Ellipse(int(elements[1]), int(elements[2]))
                    tempList.append(ell)
            except ValueError as error:
                errorCount += 1
                print("error on line " + str(lineNum) + ", " + str(line))
        self.set = tempList
        print("Processed "+str(lineNum+errorCount)+" row(s), "+str(lineNum)+" Shape(s) added, "+str(errorCount)+" error(s)")
        return self.set


    def PRINT(self):
        if self.set == None:
            print("No shapes loaded")
            return
        for element in self.set:
            try:
                if element.type == "Shape" or element.type == "Circle":
                    element.print()
                    print(end="\n")
                elif element.type == "Rhombus":
                    element.print()
                    print(", in-radius: " + str(element.inradius()))
                elif element.type == "Ellipse":
                    element.print()
                    print(", linear eccentricity: " + str(element.eccentricity()))
            except:
                print()

    def SUMMARY(self):
        if self.set == None:
            print("No shapes loaded")
            return
        circle = 0
        ellipse = 0
        rhombus = 0
        shape = 0
        tempList = self.set
        for element in tempList:
            if element.type == "Shape":
                shape += 1
            elif element.type == "Rhombus":
                rhombus += 1
            elif element.type == "Ellipse":
                ellipse += 1
            elif element.type == "Circle":
                circle += 1
        print("Circle(s): " + str(circle) + "\nEllipse(s): " + str(ellipse) + "\nRhombus(es): " + str(rhombus) + "\nShape(s): " + str(Shape.Shape.count))

    def TOSET(self):
        if self.set == None:
            print("No shapes loaded")
            return
        temp = []
        copy = False
        print("<<Clearing duplicates from multi-set>>")
        for element in self.set:
            for node in temp:
                if element == node:
                    copy = True
            if copy != True:
                temp.append(element)
            copy = False
        self.set.clear()
        for element in temp:
            self.set.append(element)
        print("<<Multi-set converted to set>")

    def DETAILS(self):

        if self.set == None:
            print("No shapes loaded")
            return

        string = ""

        for element in self.set:
            if element.type == "Shape":
                string += ("shape\n")
            elif element.type == "Rhombus":
                string += ("rhombus " + str(element.diag1) + " " + str(element.diag2) + "\n")
            elif element.type == "Ellipse":
                string += ("ellipse " + str(element.major) + " " + str(element.minor) + "\n")
            elif element.type == "Circle":
                string += ("circle " + str(element.radius) + "\n")
        print(string)

    def SAVE(self, fileName):
        string = ""

        for element in self.set:
            if element.type == "Shape":
                string += ("shape\n")
            elif element.type == "Rhombus":
                string += ("rhombus " + str(element.diag1) + " " + str(element.diag2) + "\n")
            elif element.type == "Ellipse":
                string += ("ellipse " + str(element.major) + " " + str(element.minor) + "\n")
            elif element.type == "Circle":
                string += ("circle " + str(element.radius) + "\n")
        print("Creating/opening <<"+fileName+">>")
        try:
            file = open(fileName, "w")
        except:
            print("Could not open/create <<"+str(fileName)+">>")
        print("Saving data to <<" + str(fileName) + ">>")
        file.write(string)
        file.close()
        print("Data saved to <<" + str(fileName) + ">>")

    def QUIT(self):
        print("Exiting Program")
