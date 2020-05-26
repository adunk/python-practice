# Example of a tuple
x = (1, 'two', 3.0, [4, 'four'], 5)
# Example of a string
y = [1, 'two', 3.0, [4, 'four'], 5]

print('x is {}'.format(x))
# See here that python has given the two objects separate internal IDs
print(id(x))
print(id(y))
# However here the two values share the same internal ID
print(id(x[0]))
print(id(y[0]))

# Checks to see if two objects are exactly the same (based on ID values)
if x is y:
    print('the same')
else:
    print('they are different')

if x[0] is y[0]:
    print('these values are the same')
else:
    print('these values are different.')

if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('none')
