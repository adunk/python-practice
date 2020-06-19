def main():
    # List type. Basic sequence. The list is mutable which means we can add, delete and change values
    x = [1, 2, 3, 4, 5]
    # Print the specific index
    print(x[0])
    # Print starting from position 1, end position 3
    print(x[1:3])
    # Print starting from position 1, end position 4, every 2nd item (step)
    print(x[1:4:2])
    # Search list for item. Returns index value if found
    i = x.index(5)
    print(i)
    # Add item to end of index
    x.append(999)
    # Insert an item to index at a particular index
    x.insert(0, 909)
    # Remove item from end of list, or particular index
    t = x.pop()
    u = x.pop(2)
    # Delete an item at index
    del x[3]
    print_list(x)

    p = ['rock', 'paper', 'scissors']
    # Array to string join. Only works on string objects
    print(', '.join(p))
    # Get the number of items in list
    print(len(p))

    # A tuple. Like a list but is immutable. Once created it cannot change
    # So things like append, insert, pop, etc don't work here
    y = (1, 2, 3, 4, 5)

    # A dictionary is a sequence of key/value pairs
    # These can be defined in two different ways as shown
    z = dict(a=1, b=2, c=3)
    # z = {"a": 1, "b": 2, "c": 3}
    # Access a particular key
    print(z['b'])
    # Change a key
    z['c'] = 'I am now d'
    # Add a new item
    z['d'] = 'I am a new item'
    print_dict(z)
    # Search for a key. returns boolean
    print('c' in z)
    print('found' if 'z' in z else 'nope')

    # A set is an unordered list of unique values. Useful for finding an operating on unique values
    # within a sequence.
    a = {1, 2, 3, 4, 5}
    # Can also be created with other objects. These both return the unique characters in the string. Sets do not allow
    # duplicates. On it's own the string come back in random order.
    b = set("We're gonna need a bigger boat.")
    c = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(sorted(b))
    # Here we sort the characters
    print_set(sorted(c))
    # Returns characters in set b, but no set c
    print_set(b - c)
    # Returns characters that are in b or c
    print_set(b | c)
    # Returns characters in b or c, but not both
    print_set(b ^ c)
    # Returns characters in both b and c
    print_set(b & c)

    # Any of these structures may contain any object or type

    # List comprehension techniques
    seq = range(11)
    # Creates a sequence of items from the first list * 2
    seq2 = [x * 2 for x in seq]
    # Sequence of items from seq if value is not divided by 3
    seq3 = [x for x in seq if x % 3 != 0]
    # Create a list of tuple
    seq4 = [(x, x**2) for x in seq]
    # Example of using a function on each element in array to create a new array
    from math import pi
    seq5 = [round(pi, i) for i in seq]
    # Example of creating a dictionary
    seq6 = {x: x**2 for x in seq}
    # Example of creating a set of strings
    seq7 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq5)


def print_list(o):
    for item in o:
        print(item, end=' ', flush=True)
    print()


def print_dict(o):
    # Print keys
    # for k in o.keys(): print(f'{k}')

    # Print values
    for v in o.values(): print(f'{v}')

    # Print key / values
    # f or k, v in o.items(): print(f'{k}: {v}')


def print_set(o):
    print('{', end='')
    for x in o: print(x, end='')
    print('}')


if __name__ == '__main__': main()
