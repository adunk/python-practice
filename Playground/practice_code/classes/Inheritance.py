class Publication:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title: str, price: float, period: str, publisher: str):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Author:
    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname

    # The __str__ method is used to define a user friendly string representation of an object
    # If the object is passed through a print() function, this is how it will be represented
    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'

    # Used to define a more developer facing string representation of the object that ideally can be used to recreate
    # the object in its current state. Commonly used for debugging purposes
    def __repr__(self):
        pass


class Chapter:
    def __init__(self, name: str, pagecount: int):
        self.name = name
        self.pagecount = pagecount


class Book(Publication):
    def __init__(self, title: str, pages: int, price: float, author: Author = None):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

        self.chapters = []

    def addchapter(self, chapter: Chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self) -> int:
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

    def __str__(self):
        return f'{self.title} by {self.author}, costs ${self.price}'

    def __repr__(self):
        return f'title={self.title}, author={self.author}, price={self.price}'


class Magazine(Periodical):
    def __init__(self, title: str, publisher: str, price: float, period: str):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title: str, publisher: str, price: float, period: str):
        super().__init__(title, price, period, publisher)


a1 = Author('Aldous', 'Huxley')
b1 = Book('Brave New World', 311, 29.00, a1)
print(b1)
print(repr(b1))
b1.addchapter(Chapter('Chapter 1', 125))
b1.addchapter(Chapter('Chapter 2', 97))
b1.addchapter(Chapter('Chapter 3', 143))

# Notice here we are printing the Author object directly, which is being controlled by its __str__ method
print(b1.author)
print(b1.title)
print(b1.getbookpagecount())

m1 = Book('Scientific American', 'Springer Nature', 5.99, 'Monthly')
n1 = Book('NY Times', 'New York Times Company', 6.0, 'Daily')


# Unlike other classes, Python allows classes to inherit from multiple other classes


class A:
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'Class B'


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        # Notice there that we are accessing a prop that was defined in class A and B
        # In this case class A 'wins' as it was the first class passed in through inheritance
        # This obviously can lead to unexpected behavior if not used carefully
        print(self.name)


c = C()
c.showprops()
# Print out the class method resolution order
print(C.__mro__)
