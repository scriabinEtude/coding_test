# M, N, x, y = 10, 12, 3, 9
# M, N, x, y = 13, 11, 1, 2

import sys

input = sys.stdin.readline


def find(M, N, x, y):
    limit = M * N
    xp = x
    yp = y
    while xp <= limit or yp <= limit:
        # print(xp, yp)
        if xp == yp:
            return xp
        elif xp < yp:
            xp += M
        else:
            yp += N

    return -1


for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    print(find(M, N, x, y))
