# System info and functions
# Library dealing with dates and time
import datetime
# Operating system info and functions
import os
# Library dealing with random stuff
import random
import sys


def main():
    v = sys.version_info
    p = sys.platform
    print(p)
    print('Python version {}.{}.{}'.format(*v))

    print(os.getenv('PATH'))

    # Random integer generator
    print(random.randint(1, 10000))

    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day)


if __name__ == '__main__':
    main()
