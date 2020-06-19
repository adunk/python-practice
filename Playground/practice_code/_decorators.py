
def f1():
    print('this is f1')


# Everything in python is an object, so even a function can be assigned to a variable and called like so.
x = f1
x()


# This means we can do silly stuff like this.
def f2():
    # This exists locally with the scope of f2 and cannot be called outside of this scope.
    # f2 could be said to be a wrapper of f3
    def f3():
        print('this is f3')
    return f3


y = f2()
y()


# This is the decorator function
def f4(f):
    def f5():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f5


# This indicates how this function decorated. When this is called before, this function is passed into f4 automatically
# This means we can't call f6 directly. We can only call it through it's decorator wrapper
@f4
def f6():
    print('this is f6')


# f6 is no longer available in its original form, only its wrapper is available. This is rather meta so it is better
# to define this as a decorator above
# f6 = f4(f6)

f6()
