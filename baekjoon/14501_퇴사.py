import sys

input = sys.stdin.readline


def dfs(works, x, s):
    global income

    income = max(income, s)

    for i in range(x, n):
        if validation(works[i]):
            stack.append(works[i])
            dfs(works, i + 1, s + works[i][2])
            stack.pop()


def validation(work):
    if n - work[0] + 1 < work[1]:
        return False
    if len(stack) != 0 and stack[-1][0] + stack[-1][1] - 1 >= work[0]:
        return False
    return True


n = int(input())
works = []
stack = []
income = 0

for d in range(n):
    t, p = map(int, input().split())
    works.append([d + 1, t, p])

dfs(works, 0, 0)
print(income)
