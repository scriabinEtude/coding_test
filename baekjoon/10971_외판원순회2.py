import sys

input = sys.stdin.readline

n = int(input())
g = []
stack = []
min_value = 1e20
for _ in range(n):
    g.append(list(map(int, input().split())))


def dfs(d, s):
    global min_value

    if min_value < s:
        return

    if d == n and g[stack[-1]][stack[0]] != 0:
        min_value = min(min_value, s + g[stack[-1]][stack[0]])
        return

    for i in range(n):
        if d == 0:
            stack.append(i)
            dfs(d + 1, s)
            stack.pop()
        elif i not in stack and g[stack[-1]][i] != 0:
            stack.append(i)
            dfs(d + 1, s + g[stack[-2]][i])
            stack.pop()


dfs(0, 0)
print(min_value)
