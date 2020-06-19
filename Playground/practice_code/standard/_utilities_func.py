def main():
    list1 = [1, 2, 4, 0, 5, 6]

    # any() will return true if any of the sequence values are true
    print(any(list1))

    # all() will return true if all of the sequence values are true
    # Returns false because of the 0
    print(all(list1))

    # sum() will sum up all of the values of a sequence
    print(sum(list1))
    print(sum((1, 3, 4, 5)))


if __name__ == '__main__':
    main()
