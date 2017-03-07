class Shape(object):
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def getarea(self):
        print (0)


class Square(Shape):
    def getarea(self, length, width):
        print (length*width)


class Triangle(Shape):
    def getarea(self, length, width):
        print (0.5*(length*width))
