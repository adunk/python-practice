
x = '''

seven

'''
print(f'x is {x}')
print(type(x))

z = 'eight eleven twelve'
# Counts the number of occurrences in string.
y = z.count('e')
print(f'e occurs {y} times in string "{z}"')
print(type(y))

# Replacing values (this can also be chained on top of other string functions)
# Replaces e with 8
print(z.replace('e', '8'))

m = 42
n = 24
print('the value of m: {mm} and n: {nn}'.format(mm=m, nn=n))


# Changes the entire case of string
# Since strings are immutable in python, these all create new objects rather than modifying the original string
print(z.upper())
print(z.lower())
# Swaps cases
print(z.swapcase())
# Capitalizes the first letter of string
print(z.capitalize())
# Capitalizes every word
print(z.title())

# Adjustments to string assignment positions.
a = 'seven "{0:<9}" "{1:>4}"'.format(8, 9)
print(a)
b = 'three "{0:<09}" "{1:>06}"'.format(4, 5)
print(b)

c = 12
d = 15
e = f'more string fun "{c:<3}" and "{d:>4}"'
print(e)

# Example of how to values on the same line
e = list(range(5))
for i in e:
    print(f'e is {i:<1}', end=' ', flush=True)
print()

# Formatting large numbers with , for thousands
t = 7 * 747 * 5
print('the value of t: {:,}'.format(t))
# Defaults to 6 decimals can can be changes like {:.3f} to show 3 decimals
print('value of t with decimals: {:f}'.format(t))

s = 'this is a long string with a bunch of words in it.'
# Create a list each word in the string
l = s.split()
# Create a new string from a list and 'join' by a given value
s2 = ':'.join(l)
print(s2)

# Notes: Strings in python are immutable. When formatting a string as above, these are actually new strings
# objects being created.
