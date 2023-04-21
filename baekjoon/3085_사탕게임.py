import sys

input = sys.stdin.readline


def swipe_two_candies(m: list, x: int, y: int):
    length = len(m)
    high_score = 0

    if x < length - 1 and m[y][x] != m[y][x + 1]:
        m[y][x], m[y][x + 1] = m[y][x + 1], m[y][x]
        high_score = max(high_score, find_max_eatable_way(m))
        m[y][x], m[y][x + 1] = m[y][x + 1], m[y][x]

    if y < length - 1 and m[y][x] != m[y + 1][x]:
        m[y][x], m[y + 1][x] = m[y + 1][x], m[y][x]
        high_score = max(high_score, find_max_eatable_way(m))
        m[y][x], m[y + 1][x] = m[y + 1][x], m[y][x]

    return high_score


def find_max_eatable_way(m: list):
    high_score = 0
    for row in m:
        high_score = max(high_score, get_score(row))

    for i in range(len(m)):
        high_score = max(high_score, get_score([e[i] for e in m]))

    return high_score


def get_score(values: list):
    key = ""
    score = 0
    high_score = 0
    for value in values:
        if key == value:
            score += 1
        else:
            key = value
            score = 1
        high_score = max(high_score, score)

    return high_score


def bomboni(m: list):
    high_score = 0

    for x in range(len(m)):
        for y in range(len(m)):
            high_score = max(high_score, swipe_two_candies(m, x, y))

    print(high_score)


def printFormat(original: list, m: list):
    for i in range(len(original)):
        print(
            "".join(original[i]), "".join(m[i]), ("".join(original[i]) == "".join(m[i]))
        )

    print()


M = 5

m = list(
    map(
        list,
        """
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
""".strip().split(),
    )
)

# N = int(input())
# m = []
# for _ in range(N):
#     m.append(list(input()))

bomboni(m)
