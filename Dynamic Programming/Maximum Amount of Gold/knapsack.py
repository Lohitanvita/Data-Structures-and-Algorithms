# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w = [0] + w
    items = len(w)
    capacity = W + 1

    # Create a weight matrix and write in initial values.
    weights = [[0 for _ in range(items)] for _ in range(capacity)]

    for j in range(1, items):
        for i in range(1, capacity):
            prev = weights[i][j - 1]
            cur = w[j] + weights[W - w[j]][j - 1]
            if cur > i:
                weights[i][j] = prev
            else:
                weights[i][j] = max(prev, cur)

    return weights[-1][-1]


if __name__ == "__main__":
    W, n = list(map(int, input().split()))
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
