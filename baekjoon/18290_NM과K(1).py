import sys

input = sys.stdin.readline


stack = []
ans = -1e10


def dfs(x, y, n, m, d, a, grid):
    global ans

    for i in range(x, n):
        for j in range(y if x == y else 0, m):
            if not isNearBy(i, j):
                stack.append((i, j))

                if d == len(stack):
                    ans = max(ans, a + grid[i][j])
                else:
                    dfs(i, j, n, m, d, a + grid[i][j], grid)

                stack.pop()


def isNearBy(i, j):
    if (i, j) in stack:
        return True
    elif (i - 1, j) in stack:
        return True
    elif (i + 1, j) in stack:
        return True
    elif (i, j - 1) in stack:
        return True
    elif (i, j + 1) in stack:
        return True
    else:
        return False


n, m, k = map(int, input().split())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

dfs(0, 0, n, m, k, 0, grid)
print(ans)
