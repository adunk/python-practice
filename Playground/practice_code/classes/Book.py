# Mostly based off of this course: https://www.linkedin.com/learning/python-object-oriented-programming

# This allows us to type hint a class within itself
from __future__ import annotations


class Book:
    # Class level attributes and methods are shared across all instances of the class

    # Uppercase here is just a naming convention to indicate this is a class property
    BOOK_TYPES = ('Hardcover', 'Paperback', 'Ebook')

    # double-underscore properties are hidden from other classes
    __booklist = None

    # Static methods. These don't modify the state of a specific class object instance, or the class itself.
    # Limited use but can be helpful when following the singleton pattern, and namespacing methods to a class
    # that would otherwise be a global function.
    # Makes sense when you don't been to access a particular class attribute or method, but make sense to include in the
    # class definition
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # @classmethod is a decorator to identify this has a class method
    # This methods cannot be called on by class objects, but rather the class itself.
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # Whenever we call a method on an object the object itself automatically gets passed into the method
    # This is 'self' and will always be the first argument in class methods
    # The word 'self' is just a naming convention. We could call it anything, but this is just the convention
    # that most Python programming follows

    def __init__(self, title, author, pages, price, book_type):
        # These are examples of 'instance' attributes. Each value will be unique to each class object instance
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        if not book_type in Book.BOOK_TYPES:
            raise ValueError(f'{book_type} is not a valid book type')
        else:
            self.book_type = book_type

        # Properties with a __ (double underscores) are hidden by the interpreter
        # The purpose of this feature is to prevent sub-classes from inadvertently overriding the attribute
        # Can be useful in certain circumstances when you want to make sure this doesnt happen
        self.__secret = 'This is a secret'

        self._discount = 0.1

    # Class methods are also 'instance' methods to each object instance of the class
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        # _attribute is a naming hint to other developers that this attribute is internal to the class
        # and should not be accessed outside of the classes object
        # (similar to private / protected in PHP but python doesn't have a formal way of enforcing this)
        self._discount = amount

    def getsecret(self):
        return self.__secret

    def __str__(self):
        return f'{self.title} by {self.author}, costs ${self.price}'

    # This method gets called when the object is compared against another object
    def __eq__(self, other: Book) -> bool:
        return (self.title == other.title and self.author == other.author)

    def __ge__(self, other: Book) -> bool:
        return self.price >= other.price

    # Less than operator. This also has automatically adds support for sorting, which uses this function internally
    def __lt__(self, other: Book) -> bool:
        return self.price < other.price

    # Allows us to control access when an attribute is retrieved. This is a called whenever a value is accessed
    # It is also called by python when it goes to lookup any methods on the class. Careful!
    def __getattribute__(self, item):
        # Here we're looking at when we access the price attribute
        if item == 'price':
            # If so we can automatically calculate price based on a discount
            # We use super() here to avoid recursion on this classes __getattribute__() method
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p * d)
        return super().__getattribute__(item)

    # This is only called when __getattribute__ lookup fails. Consequently the primary purpose of this method is to
    # dynamically set attributes on the fly
    def __getattr__(self, item):
        if item == 'date':
            return 'The date attribute was called but not defined'

    # Allows us to control access when an attribute is set
    def __setattr__(self, key, value):
        if key == 'price':
            if type(value) is not float:
                raise ValueError('the price attr must be a float')
        return super().__setattr__(key, value)

    # This can be used to call the object just a like a function
    def __call__(self, *args, **kwargs):
        for k, v in kwargs.items():
            # Took me a while to figure this out, but this is the method to change class attributes with key/value pairs
            setattr(self, k, v)


b1 = Book('A Brave New World', 'JD Salinger', 234, 29.95, 'Hardcover')
b2 = Book('War and Peace', 'Leo Tolstoy', 1225, 39.95, 'Paperback')
b3 = Book('A Brave New World', 'JD Salinger', 234, 29.95, 'Hardcover')
b4 = Book('To Kill a Mockingbird', 'Harper Lee', 175, 24.95, 'Hardcover')

# print(b1 == b2)
# print(b1 == b3)
print(b2 >= b1)
print(b3 < b2)

books = [b3, b2, b4, b1]
# This will call the __lt__ method to use for sorting, in this case by price
books.sort()
print([book.title for book in books])

print(b1)
# Call b1 as a function to change it attribute values
b1(title='A new Title', author='Andrew Dunkle')
print(b1)

print(b1.getprice())
print(b1.title)

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# This property can't be seen outside of the class and will return an error
# print(b2.__secret)
# This however works just fine
print(b2.getsecret())

# Here we are calling a class method
print('Book Types', Book.get_book_types())

# static methods
# Remember that while this is part of the class, this doesn't actually modify the classes state. Really just a helper
# function that relates to the Book class
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
print(Book.getbooklist())
