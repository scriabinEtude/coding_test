# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19


def addOne(value: int, limit: int):
    if value + 1 > limit:
        return 1
    else:
        return value + 1


def count(E, S, M):
    count = 1
    ESM = [1, 1, 1]
    while True:
        if ESM[0] == E and ESM[1] == S and ESM[2] == M:
            return count
        else:
            count += 1
            ESM[0] = addOne(ESM[0], 15)
            ESM[1] = addOne(ESM[1], 28)
            ESM[2] = addOne(ESM[2], 19)


# print(count(1, 16, 16))

E, S, M = map(int, input().split())
print(count(E, S, M))
