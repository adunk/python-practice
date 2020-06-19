children = ['Sue', 'Jerry', 'linda']
print(sorted(children))
# Sort by case insensitive values
print(sorted(children, key=str.upper))

# List comprehension method to apply a function to every item in list
new = [item.upper() for item in children]
print(new)
print(children)

# Map method to apply function to every method of list
_map = list(map(str.lower, children))
print(_map)

print(sorted('My favorite child is Linda'.split(), key=str.upper))

students = [('alice', 'B', 12), ('eliza', 'A', 16), ('tae', 'C', 15)]
# Sort by first key
print(sorted(students, key=lambda student: student[0]))
# Sort by send key
print(sorted(students, key=lambda student: student[1]))
# Sort by third key
print(sorted(students, key=lambda student: student[2]))

