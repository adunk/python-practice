import numpy as np

# Example if a list (mutable). Holds a collection of items of any type. List of lists are certainly possible
# Lists are ordered allowing us to use indexes to access any item
# Items do NOT need to be unique (compared to sets which are unique)
a = [1, 2, 3, 4, 5, 6]
a[2] = 42
for i in a:
    print(f'a is {i}')

# The numpy package includes an 'array' data structure which are very similar to 'lists' in terms of construction
# The key difference (and advantage) is that they store large amounts of data very compactly, particularly when dealing
# with numbers. So for data analysis they can offer significant performance improvements.

# For performance reasons it's actually better to start with a list and add items to that, and then later convert to an
# array. list.append() is much more efficient than array.append()

array = np.array([3, 6, 9, 12])
# You can also perform numeric operations directly on arrays, which you can't on lists
division = array / 3
print(division)

# Example if a tuple (immutable)

# This is generally favorable when working with lists unless you know you will need to change the items
b = (1, 2, 3, 4, 5, 6)
# This will fail
# b[2] = 42
for i in b:
    print(f'b is {i}')

# Unpacking

# This will assign values based on the tuple index. Trying to assign more variables that are available in the
# tuple will cause an error. Same is true if there are not enough values in the tuple

xy, yz = (1, 2)
# _ is a convention in python to indicate the variable is not being used
ad, _ = (2, 3)
# The *sf will be assigned the remaining values in the tuple (4, 5, 6)
sa, sd, *sf = (1, 3, 4, 5, 6)
# In this case we can also assign the last value. re = 1, rt = 2, _ = [3, 4, 5], and ry = 6
re, rt, *_, ry = (1, 2, 3, 4, 5, 6)

# Example of ranges. Like tuples these are NOT mutable.
c = range(5)
for i in c:
    print(f'c is {i}')

# range(start, stop, range)
d = range(5, 50, 5)
for i in d:
    print(f'd is {i}')

# Example of how to use range to build a mutable list.
e = list(range(5))
e[2] = 42
for i in e:
    print(f'e is {i:<1}', end=' ', flush=True)
print()

# Example of a dictionary, a searchable index of key / value pairs.
f = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# dict values can also be changed
f['three'] = 42
for k, v in f.items():
    print(f'k: {k}, v: {v}')

# Another way to create a dictionary
g = dict(one=1, two=2, three=4, four=4, five=5)
