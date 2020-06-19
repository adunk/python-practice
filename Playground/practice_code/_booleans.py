# These all evaluate to false in a conditional statement
a = 0
a2 = 0.0
b = False
c = None
d = ''
e = []
f = {}
g = ()

if a:
    print("a is True")
else:
    print('a is False')

if b:
    print("b is True")
else:
    print('b is False')

if c:
    print("c is True")
else:
    print('c is False')

if d:
    print("d is True")
else:
    print('d is False')


# print(f'a is {a}')
# print(type(a))


# Classes can also be adjusted to apply custom logic on how they are evaluated
class MyClass:
    # Override the default boolean method
    def __bool__(self):
        return False

    # Override the default length method
    def __len__(self):
        return 0
