def main():
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    daysFr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

    # Use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))
    with open('scores.txt', 'r') as fp:
        # In this case the iter() function is calling the fp.readline method until it finds ''
        # Once this happens the loop stops. Here this is an empty string and thus must be the
        # end of the file
        for line in iter(fp.readline, ''):
            print(line)

    # Using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # Use zip to combine sequences in a single loop
    for m in zip(days, daysFr):
        # Returns a tuple of the items in each list of the same index
        print(m)

    for day, dayFr in zip(days, daysFr):
        print(f'{day} = {dayFr} in French')

    # Combining it all together
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], '=', m[1], 'in French')


if __name__ == '__main__':
    main()
