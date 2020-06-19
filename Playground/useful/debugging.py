# Helpful for printing out the property values of objects
def object_props(obj):
    temp = vars(obj)
    for item in temp:
        print(f'{item}: {temp[item]}')
