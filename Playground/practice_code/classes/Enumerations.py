from enum import Enum
from enum import auto
from enum import unique


# Add unique decorator to class to ensure all enum values are unique
@unique
class Fruits(Enum):
    # These seem like const in PHP, but their particular uses are still a little unknown...
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # This would cause an error as the values aren't unique
    # MANGO = 4
    # This auto-generates the value to 5 based on previous values to create a sequence.
    PEAR = auto()


def main():
    print(Fruits.APPLE)
    print(type(Fruits.APPLE))
    print(repr(Fruits.APPLE))
    print(Fruits.APPLE.name, Fruits.APPLE.value)
    pass


if __name__ == '__main__':
    main()
