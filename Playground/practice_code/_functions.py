def main():
    x = 5
    kitten(x)
    print(f'in main: x is {x}')
    # The * here is a little trick to convert the list into individual function arguments
    print(addition(*[1, 3, 4, 5]))


def addition(*args):
    return sum(args)


def kitten(a):
    # This creates a whole new variable and x above is not changed
    a = 3
    print('meow')
    print(a)


def mutable():
    b = [5]
    change(b)
    print(b)


def change(c):
    # We are now changing the value of b in the mutable call above.
    c[0] = 88
    print(c)


def dog():
    x = ('grr', 'woof', 'pant')
    # Notice the list argument indicator
    bark(*x)


# * variable length argument list indicator. Treats the argument as a tuple.
# This allows us to pass in any number of arguments into the function
def bark(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('wag')


def a_list():
    y = dict(Buffy='meow', Zilla='grr', Angel='rawr')
    a_action(**y)


# Example of **kwargs (keyword arguments). See a_list() above
# The double asterisk form of **kwargs is used to pass a keyworded, variable-length argument dictionary to a function.
# Again, the two asterisks (**) are the important element here, as the word kwargs is conventionally used, though not
# enforced by the language.
def a_action(**kwargs):
    if len(kwargs):
        for k, v in kwargs.items():
            print(f'Item {k} says {v}')
    else:
        print('Empty list')


# Example of using a generator function
def main_b():
    try:
        for i in inclusive_range(25):
            print(f'Number is {i}', end=' ', flush=True)
            print()
    except TypeError as e:
        print(f'Error: {e}')


# Example of a generator function. Useful for creating a series of values.
def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1

    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # Generator
    i = start
    while i <= stop:
        yield i
        i += step


# __name__ is a special variable that returns the name of the current module
# This is important when importing code into other scripts to avoid name clashing
# the '__main__' is a special value that means this was not imported and this is the 'main' file.
# This is also important as it allows functions in the script to call other functions that have been defined after it.
# Otherwise they won't work.
if __name__ == '__main__':
    main()
    mutable()
    dog()
    a_list()
    main_b()
