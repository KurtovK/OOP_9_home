from.management_file import FigureManagementFile

class Shape:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y


class Sguare(Shape, FigureManagementFile):
    pass

class Circle(Shape, FigureManagementFile):
    pass

class Ellipse (Shape,FigureManagementFile):
    pass

