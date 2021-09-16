# python3

def fib(n):

    f0 = 0
    f1 = 1

    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:

        rem = n % 60

        if rem == 0:
            return 0

        for i in range(2, rem + 3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f

        s = f1 - 1
        return s % 10


if __name__ == '__main__':

    n = int(input())
    print(fib(n))


