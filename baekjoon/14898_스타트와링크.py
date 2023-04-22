import sys
import itertools

input = sys.stdin.readline


def sol():
    difference = 1e10
    for start in ps:
        link = makeLinkTeamByStart(start)
        difference = min(difference, abs(sumAbility(start) - sumAbility(link)))

    print(difference)


def makeLinkTeamByStart(start):
    link = []
    for i in range(n):
        if i not in start:
            link.append(i)

    return link


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

ps = itertools.combinations(list(range(n)), n // 2)

sol()
