
def read_numbers():
    n = int(input())
    m = int(input())
    return n, m


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def least_factor(number):
    if number <= 1:
        return 1

    for i in range(2, number + 1):
        if number % i == 0:
            return i


def main():
    n, m = read_numbers()
    result = eratosthenes(n, m)
    return result


if __name__ == '__main__':
    print(main())
