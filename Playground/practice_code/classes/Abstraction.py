# Using abstract base classes to enforce class constraints
import math
from abc import ABC
from abc import abstractmethod


# In concept this is an 'Interface'. We are defining a class that other classes may inherit from that MUST implement
# the methods we define here
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    # This flags an classes that extend this class that they must also implement this method. Otherwise they fail.
    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return math.pi * (self.radius ** 2)

    def toJSON(self):
        return f'{{\'circle\' : {str(self.calcArea())} }}'


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side
