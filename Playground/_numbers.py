from decimal import *

a = 7 / 3
print(f'a is {a}')
print(type(a))

b = 7 // 3
print(f'b is {b}')
print(type(b))

c = 7 % 3
print(f'c is {c}')
print(type(c))

# You would think this would equal 0, but does not.
# This is the precision value, not the accurate value,
# and may lead to unexpected results particularly when
# dealing with money calculations.
d = 0.1 + 0.1 + 0.1 - 0.3
print(f'd is {d}')
print(type(d))

e = Decimal('0.1')
f = Decimal('0.3')
g = e + e + e - f
print(f'g is {g}')
print(type(g))

# Number functions
x = '47'
# Integer
y = int(x)
# Float
z = float(x)
# Absolute value
t = -47
u = abs(t)

m = 47
# Returns a tuple with two values. Divisible and remainder (15, 2)
n = divmod(m, 3)


print(f'x is {x}')
print(f'y is {y}')
