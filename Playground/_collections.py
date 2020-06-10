import string
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple


def main():
    # Named Tuples offer more functionality to the basic tuple structure. Advantage here is to give defined names to
    # indexes, which improve code readability.

    # 'Point' the name of the tuple.
    # 'x y' are the names of each value pair
    Point = namedtuple('Point', 'x y')
    p1 = Point(1, 2)
    p2 = Point(10, 20)
    print(p1, p2)
    # Now we have the ability to access values with the pre-defined descriptive values, rather pure index values
    print(f'p1.x is {p1.x} and p2.y is {p2.y}')

    # defaultdict

    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'grape', 'banana', 'banana']
    # defaultdict requires a factory function, in this case the int object that is used to initialize the counter value
    # Basically what this says is if I try and access a key that doesn't exist, create a default value for me using the
    # int() class as a constructor. int object initializes a value of 0
    fruitCounter = defaultdict(int)
    # This can be really any function, including a lambda
    # fruitCounter = defaultdict(lambda: 100)

    # This is all useful when you want to define a default dictionary value if it hasn't already been set

    for fruit in fruits:
        fruitCounter[fruit] += 1

    for (k, v) in fruitCounter.items():
        print(f'{k}: {v}')

    # Counters

    class1 = ['bob', 'becky', 'chad', 'darcy', 'frank', 'hannah', 'kevin', 'james', 'james', 'melanie', 'penny',
              'steve']
    class2 = ['bill', 'barry', 'cindy', 'debbie', 'frank', 'gabby', 'kelly', 'james', 'joe', 'sam', 'tara', 'ziggy']

    c1 = Counter(class1)
    c2 = Counter(class2)

    # Hom many students are names 'james' in c1ass1?
    print(c1['james'])
    # How many students are in class1?
    print(f'{sum(c1.values())} in class 1')
    # Add class 2 to class 1
    c1.update(c2)
    # Print new total
    print(f'{sum(c1.values())} in class 1')
    # What are the 3 most common names in c1? Returns a list of tuples
    print(c1.most_common(3))
    # Separate the classes again
    c1.subtract(c2)
    # See the results
    print(c1.most_common(3))
    # What's common between the two classes?
    print(c1 & c2)

    # OrderedDict

    # OrderedDict remembers the order in which items were added / removed
    sportTeams = [('Royals', (18, 12)), ('Rockets', (24, 6)), ('Cardinals', (20, 10)), ('Dragons', (22, 8)),
                  ('Kings', (20, 10)), ('Chargers', (20, 10)), ('Jets', (16, 14)), ('Warriors', (25, 5))]
    # Sort the teams by wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    # 'False' claims the first item in the last, true claims the last item in the list
    tm, wl = teams.popitem(False)
    print(f'Top Team: {tm} {wl}')
    # What are the next four teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # Test for equality
    a = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    b = OrderedDict({'a': 1, 'b': 2, 'c': 3})
    c = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    d = {'a': 1, 'c': 3, 'b': 2}
    print('Equality test: ', a == b)
    # This is now false since the order is not the same
    print('Equality test: ', a == c)
    # When compared the a regular dict this is now true since the order no longer matters. Shows where
    # OrderedDict can be
    # useful
    print('Equality test: ', a == d)

    # Deques - Really useful when you need to perform operations on the front and ends of lists, and perform actions
    # such as rotation.

    # Create a deque of all lower case letters
    d = deque(string.ascii_lowercase)
    print(d)
    # These objects can be counted as normal
    print(f'Item Count: {len(d)}')
    # And looped over as normal
    for elem in d:
        print(elem.upper(), end=', ')
    print()
    # Object can be manipulated as so
    # Take item from end
    tu = d.pop()
    # Take item from beginning
    ut = d.popleft()
    print(tu, ut)
    # Add item to end
    d.append(1)
    # Add item to start
    d.appendleft(2)
    print(d)
    # Rotate the deque by x spaces. Essentially this shifts the item order by x spaces to the left.
    # The value on the end goes to the front
    d.rotate(10)


if __name__ == '__main__':
    main()
