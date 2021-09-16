# python3
import sys


def compute_min_refills(distance, miles, tank, stops):
    # write your code here
    num_refill, curr_refill, limit = 0, 0, miles
    while limit < distance:
        if curr_refill >= tank or stops[curr_refill] > limit:
            return -1
        while curr_refill < tank - 1 and stops[curr_refill + 1] <= limit:
            curr_refill += 1

        num_refill += 1  # Stop to tank
        limit = stops[curr_refill] + miles  # Fill up the tank
        curr_refill += 1

    return num_refill


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops = list(map(int, input().split()))
    print(compute_min_refills(d, m, n, stops))
