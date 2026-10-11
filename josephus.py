
def josephus(n, k):
    """محاسبه موقعیت آخرین نفر باقیمانده"""
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n


def main():
    import sys

    data = sys.stdin.read().splitlines()

    x = int(data[0])
    results = []

    for i in range(1, x + 1):
        line = data[i].strip()

        if line == "*":
            break

        numbers = list(map(int, line.split()))

        n = 100
        k = 2

        if len(numbers) >= 1:
            n = numbers[0]

        if len(numbers) >= 2:
            k = numbers[1]

        safe_position = josephus(n, k) + 1
        results.append(safe_position)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
