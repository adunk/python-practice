class Duck:
    sound = 'Quaaaack!'
    walking = 'Walk like a duck.'

    def __init__(self):
        # Colors!
        self._red = 50
        self._green = 75
        self._blue = 100

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

    # This is called when the requested attribute can't be found on the object and a default value needs to be returned
    def __getattr__(self, item):
        if item == 'rgbcolor':
            return (self._red, self._green, self._blue)
        elif item == 'hexcolor':
            return '#{0:02x}{1:02x}{2:02x}'.format(self._red, self._green, self._blue)
        else:
            raise AttributeError

    # This is called whenever an attribute is requested, regardless of whether it exists or not.
    # It is also called by python when it goes to lookup any methods on the class. Careful!
    # def __getattribute__(self, item):
    #     pass

    # Called when an attribute value is set on an object.
    def __setattr__(self, key, value):
        if key == 'rgbcolor':
            self._red = value[0]
            self._green = value[1]
            self._blue = value[2]
        else:
            # Important here to call the super() if the attribute requested is not the one we care about.
            # Otherwise everything breaks
            super().__setattr__(key, value)

    # Called when a value attribute is deleted on an object
    # def __delattr__(self, item):
    #     pass

    # Called when the dir() function is called on the object. Lists the available properties
    def __dir__(self):
        # Return a list of regular properties and computed properties
        return ('_red', '_green', '_blue', 'rgbcolor', 'hexcolor')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    print(donald.rgbcolor)
    print(donald.hexcolor)
    donald.rgbcolor = (100, 75, 50)
    print(donald.rgbcolor)
    print(donald.hexcolor)
    print(dir(donald))


if __name__ == '__main__':
    main()
