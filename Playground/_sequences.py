# Example if a list (mutable)
a = [1, 2, 3, 4, 5, 6]
a[2] = 42
for i in a:
    print(f'a is {i}')

# Example if a tuple (immutable)
# This is generally favorable when working with arrays
# unless you know you will need to change the items
b = (1, 2, 3, 4, 5, 6)
# This will fail
#b[2] = 42
for i in b:
    print(f'b is {i}')

# Example of ranges. Like tuples these are NOT mutable.
c = range(5)
for i in c:
    print(f'c is {i}')

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
# Another way to create a dictionary
g = dict(one=1, two=2, three=4, four=4, five=5)
f['three'] = 42
for k, v in f.items():
    print(f'k: {k}, v: {v}')
