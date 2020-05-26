name = 'Taylor'
# Number of characters in string
print(len(name))
# Technically equal to this built in property of string objects
print(name.__len__())

ages = [0, 11, 43, 12, 10]
# Prints out the number of items in list
print(len(ages))

for i in range(0, len(ages)):
    print(ages[i])

# Print the number of items in collections
collection = {'bob': 10, 'mary': 7, 'sam': 18}
print(len(collection))
