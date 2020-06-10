def filter_func(x: int):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x: str):
    if x.isupper():
        return False
    return True


def square_func(x: int):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = 'abcDeFGHiJklmnoP'
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # Use filter to remove items from a list
    odds = list(filter(filter_func, nums))
    print(odds)
    lowers = list(filter(filter_func2, chars))
    print(lowers)

    # Use map to create a new sequence of values by applying a given function to each value in the
    # original sequence
    squares = list(map(square_func, nums))
    print(squares)

    grades = sorted(grades)
    letters = list(map(to_grade, grades))
    print(letters)


if __name__ == '__main__':
    main()
