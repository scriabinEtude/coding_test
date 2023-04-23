n = int(input())
table = input()
stack = []
cols = [0]
arr = [[0] * n for _ in range(n)]
flag = False
k = 0

for i in range(n):
    for j in range(i, n):
        arr[i][j] = table[k]
        k += 1

for i in range(n, 1, -1):
    if i == 1:
        cols.append(1)
    else:
        cols.append(cols[-1] + i)


def isOk(a, b, s):
    c = ch(s)
    # print(a, b, c, table[cols[a] + b - a - 1])
    return pick(a, b) == c


def ch(s):
    return "0" if s == 0 else "+" if s > 0 else "-"


def pick(a, b):
    # return table[cols[a] + b - a]
    return arr[a][b]


def validation(l):
    size = len(l)
    if size == 0:
        return True

    for i in range(size):
        s = 0
        for j in range(i, size):
            s += l[j]
            if not isOk(i, j, s):
                return False

    return True


def dfs(d):
    # print(d, pick(d, d), stack)
    global flag
    if flag:
        return

    # print(stack, validation(stack))
    if not validation(stack):
        return
    if d == n:
        flag = True
        print(" ".join(map(str, stack)))
        return

    r = (
        [0]
        if pick(d, d) == "0"
        else range(1, 11)
        if pick(d, d) == "+"
        else range(-1, -11, -1)
    )

    for i in r:
        stack.append(i)
        dfs(d + 1)
        stack.pop()


dfs(0)
