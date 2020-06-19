# Arithmetic Operators
# + addition
# - subtraction
# * multiplication
# / division
# // integer division
# % remainder (modulo)
# ** exponent
# - unary negative
# + unary positive

x = 5
y = 3

z = x / y
#print(f'z is {z}')

# Bitwise Operators
# & and
# | or
# ^ Xor
# << shift left
# >> shift right

a = 0x0a
b = 0x05
c = a & b
d = a | b

#print(f'(hex) a is {a:02x}, b is {b:02x}, c is {c:02x}, d is {d:02x}')
#print(f'(bin) a is {a:08b}, b is {b:08b}, c is {c:08b}, d is {d:08b}')

# Comparison Operators
# < less than
# > greater than
# <= less than or equal
# >= greater than or equal
# == equal
# != not equal

# Boolean Operators
# and - And
# or - Or
# not - Not
# in - Value in set
# not - in Value not in set
# is - Same object identity
# is not - Not same object identity

a = True
b = False

if a and b:
    print('expression is True')
else:
    print('expression is False')

c = ('bear', 'bunny', 'tree', 'sky', 'rain')
d = 'bear'

if d in c:
    print('d is in c')
else:
    print('d is not in c')

if d is c[0]:
    print('this expression is true')
    # Can see here they are in fact the same object
    print(f'id of d is {id(d)}, id of c[0] is {id(c[0])}')
else:
    print('this expression is false')
