# Uses python3

def calc_fib(n, lookup):
    if n <= 1:
        return n

    if n not in lookup:
        lookup[n] = calc_fib(n - 1, lookup) + calc_fib(n - 2, lookup)

    return lookup[n]


if __name__ == '__main__':
    n = int(input())
    lookup = {}
    print(calc_fib(n, lookup))
