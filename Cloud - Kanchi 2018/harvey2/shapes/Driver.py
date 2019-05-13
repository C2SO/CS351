#!/usr/bin/python3

# Author: Daniel Harvey
# Written: April 26 2018

import math

class Shape:
    sides = []
    
    def __init__(self, sides):
        self.sides = sides
        for i in range(0,len(self.sides)):
            self.sides[i] = float(self.sides[i])

    def printSides(self):
        s = ""
        for side in self.sides:
            s += str(side) + ' '
        
        return s.strip()


    def area(self):
        pass

class Triangle(Shape):
    
    def __init__(self, sides):
        assert( len(sides) == 3 )
        Shape.__init__(self, sides)

    def area(self):
        # Use herons formula
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        return math.sqrt(p * (p-self.sides[0]) * (p-self.sides[1]) * (p-self.sides[2]))

class Rectangle(Shape):
    
    def __init__(self, sides):
        assert(len(sides)==2)
        Shape.__init__(self, sides)

    def area(self):
        # Width times Length
        return self.sides[0] * self.sides[1]

class Driver:
    fileName = 'shapes.txt'
    
    def __init__(self, fileName):
        self.fileName = fileName
    
    def loadShapesFromFile(self):
        listOfShapes = []

        data = open(self.fileName, 'r').read()
        for line in data.split('\n'):
            pieces = line.split()

            if len(pieces) > 0:
                if pieces[0] == 'T':
                    listOfShapes.append(Triangle(pieces[1:4]))
                elif pieces[0] == 'R':
                    listOfShapes.append(Rectangle(pieces[1:3]))
        
        return listOfShapes

    def printShapes(self, listOfShapes):
        for shape in listOfShapes:
            print("%s with sides %s: Area = %d" % (type(shape).__name__, shape.printSides(), shape.area()))

driver = Driver('shapes.txt')
driver.printShapes(driver.loadShapesFromFile())


