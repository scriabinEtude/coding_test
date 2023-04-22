import sys
import itertools

input = sys.stdin.readline


def sol():
    difference = 1e10

    for i in range(1, int(n / 2) + 1):
        ps = itertools.combinations(list(range(n)), i)

        for start in ps:
            link = pn - set(start)
            difference = min(difference, abs(sumAbility(start) - sumAbility(link)))
            if difference == 0:
                print(difference)
                return

    print(difference)


def sumAbility(players: list[int]):
    total = 0
    for c in itertools.combinations(players, 2):
        total += pickAbility(c[0], c[1])
    return total


def pickAbility(i, j):
    return a[i][j] + a[j][i]


n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

pn = set(range(n))

sol()
