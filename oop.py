class Shape(object):
    """ Creates superclass Shape"""
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def getarea(self):
        return 0


class Square(Shape):
    """Square is a subclass of Shape"""
    def getarea(self, length, width):
        print(length * width)


class Triangle(Shape):
    """Triangle is a subclass of Shape"""
    def getarea(self, length, width):
        print(0.5 * (length*width))


Square(4, 4)
Triangle(4, 4)
