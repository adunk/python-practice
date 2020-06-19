import math


# Represents a moving reptile. Will hold it's state and position, and will respond to our commands
class Turtle(object):
    # Class attribute common to all instances
    deg = math.pi / 180.0

    def __init__(self, terrarium):
        self.pos = (0, 0)
        self.angle = 0
        self.pen = True

        self.axes = terrarium.axes

    # self refers back to the instance in which we called the method.
    def forward(self, distance):
        posnew = (self.pos[0] + distance + math.cos(self.deg + self.angle),
                  self.pos[1] + distance + math.sin(self.deg + self.angle))

        if self.pen:
            pass

        self.pos = posnew

    def left(self, angle):
        self.angle = (self.angle + angle) % 360

    def right(self, angle):
        self.angle = (self.angle - angle) % 360

    def penup(self):
        self.pen = False

    def pendown(self):
        self.pen = True


# Will be tasked with holding the image that we will draw. This will be a matplotlib figure
class Terrarium(object):
    pass
