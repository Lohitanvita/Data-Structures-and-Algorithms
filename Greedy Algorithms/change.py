# Uses python3
import sys

def get_change(m):
    #write your code here
    deno = [1, 5, 10]
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while i >= 0:

        # Find denominations
        while (m >= deno[i]):
            m -= deno[i]
            ans.append(deno[i])

        i -= 1
    return len(ans)


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
