n = int(input())
ops = list(input().split())

stack = []
ans = []


def dfs(d):
    if d == n + 1:
        ans.append("".join(map(str, stack)))
        return

    for i in range(10):
        if d == 0 or (i not in stack and op(stack[d - 1], i, ops[d - 1])):
            stack.append(i)
            dfs(d + 1)
            stack.pop()


def op(a, b, op: str):
    if op == "<":
        return a < b
    else:
        return a > b


dfs(0)
ans.sort()
print(ans[-1])
print(ans[0])
