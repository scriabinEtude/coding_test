import itertools

n, m = map(int, input().split())
p = itertools.combinations([i for i in range(1, n + 1)], m)

for e in p:
    print(" ".join(map(str, e)))
