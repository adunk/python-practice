import itertools

# Infinite counting
for x in itertools.count(50, 5):
    print(x)
    # Break out of the loop once we've hit 80. Otherwise will go on forever
    if x == 80:
        break

# This will loop over each letter of a string indefinitely. In order to break out we need a counter
y = 0
for c in itertools.cycle('racecar'):
    print(c)
    # Increment the counter
    y += 1
    # Once we looped over 50 characters, break out of the loop
    if y > 50:
        break

# Here we're just repeating a block of code until a condition break us out of the loop
for r in itertools.repeat(True):
    print(r)
    y += 1
    if y > 100:
        break

election = {1: 'barb', 2: 'karen', 3: 'erin'}

# This will create and loop over each possible permutation of a give list
for p in itertools.permutations(election.values()):
    print(p)

colors = ['red', 'blue', 'green', 'yellow', 'orange']

# Combinations: Similar to permutations but order does not matter - no copies with the same inputs
for c in itertools.combinations(colors, 2):
    print(c)

# Use chain() to connect sequences together
x = itertools.chain('ABCD', '1234')
print(list(x))


def test_function(x: int):
    return x < 40


vals = [10, 20, 30, 40, 50, 40, 30]

# dropwhile() and takewhile() will return values until a certain condition is met that stops them
# dropwhle() will ignore values until the condition is met, and then start filling in.
# takewhile() will take until condition is met, then stops
print(list(itertools.dropwhile(test_function, vals)))
print(list(itertools.takewhile(test_function, vals)))
