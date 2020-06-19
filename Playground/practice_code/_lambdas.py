# Typically used in place just when needed, and would otherwise add complexity to the code
# lambda: (parameters) : (expression)

def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Convert to celsius
    print(list(map(lambda t: (t - 32) * 5 / 9, ftemps)))
    # Convert to fahrenheit
    print(list(map(lambda t: (t * 9 / 5) + 32, ctemps)))

    # Another example
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    even_squared = list(map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(even_squared)

    # These can also be done using comprehensions
    # [] take the place of list()
    # e ** 2 is the function expression
    # for e in evens is taking the place of map() and applying the expression to each element
    even_squared_2 = [e ** 2 for e in evens]
    print(even_squared_2)

    # Applying a filter to the loop as well
    odds_squared = [e ** 2 for e in odds if 3 < e < 17]
    print(odds_squared)

    # Comprehensions can also be used on dictionaries

    # {key: value expression for i in list if predicate}
    temp_dict = {t: (t * 9 / 5) + 32 for t in ctemps if t < 100}
    print(temp_dict)
    print(temp_dict[12])

    team1 = {'Jones': 24, 'Jameson': 18, 'Smith': 58, 'Burns': 7}
    team2 = {'White': 12, 'Macke': 88, 'Perce': 4}

    # Merge the two team into a single dictionary using two loops within the same comprehension
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)

    # Comprehensions can also be used for sets of unique values

    ctemps_2 = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]
    # Create a standard list
    ftemps_1 = [(t * 9 / 5) + 32 for t in ctemps_2]
    print(ftemps_1)
    # Create a set lis of unique values
    ftemps_2 = {(t * 9 / 5) + 32 for t in ctemps_2}
    print(ftemps_2)

    s_temp = 'The quick brown fox jumped over the lazy dog'
    chars = {c.upper() for c in s_temp if not c.isspace()}
    print(chars)


if __name__ == '__main__':
    main()
