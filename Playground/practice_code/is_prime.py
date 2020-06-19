def is_prime(n):
    if (n <= 1):
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


def list_primes():
    for n in range(100):
        if is_prime(n):
            print(n, end=' ', flush=True)
    print()


list_primes()


def is_even(n):
    if n % 2 == 0:
        return True
    return False


# numbers = range(1, 10)
#
# for i in numbers:
#     print('Is the number {} even? {}'.format(i, is_even(i)))
