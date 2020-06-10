class Animal:
    # This is a class variable. These are the exact same in every instance of the class
    # Defining class variables in this way is generally a bad idea unless you really intend to do so
    x = [1, 2, 3]

    def __init__(self, **kwargs):
        # The _ is a convention that indicates these are object variables.
        # They are not defined before the object is instantiated and thus are bound to
        # the object, not the class.
        # The _ discourages other developers from using them directly, and should use the methods below.
        # This is because python doesnt have private variables
        # self._type = type
        # self._name = name
        # self._sound = sound
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    # Getter/Setter pattern
    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None

    # This is called when the object or class is passed through the str(), print(), or format() functions
    # This is generally more human readable
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'

    # How the class is printed using the repr() function. This is generally useful when debugging.
    def __repr__(self):
        return f'repr: The {self.type()} is named "{self.name()}" and says "{self.sound()}"'


class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)


class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')


class RevStr(str):
    def __str__(self):
        return self[::-1]


def main():
    a0 = Kitten(name='fluffy', sound='rawr')
    a1 = Duck(name='donald', sound='quack')
    a0.sound('bark')
    print(a0)
    print(repr(a1))
    a0.kill('humans')

    # Demonstrates how class variables are mutable between different class instances.
    # See how we print a0, but changed a1, the value of a0 still changes
    print(a0.x)
    a1.x[0] = 7
    print(a0.x)

    # Demonstrates how we can extend the base str function with our own class to reverse the string
    hello = RevStr('Hello, world!')
    print(hello)


if __name__ == '__main__':
    main()
