def dfs(x, c, a):
    if len(stack) == l and validation():
        print("".join(stack))
        return

    for i in range(x, c):
        stack.append(a[i])
        dfs(i + 1, c, a)
        stack.pop()


def validation():
    m, j = 0, 0
    for c in stack:
        if c in "aeiou":
            m += 1
        else:
            j += 1

        if m >= 1 and j >= 2:
            return True

    return False


l, c = map(int, input().split())
a = input().split()
# l, c = 4, 6
# a = ["a", "t", "c", "i", "s", "w"]
a.sort()
stack = []

dfs(0, c, a)
