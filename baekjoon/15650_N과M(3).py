import itertools

n, m = map(int, input().split())
p = itertools.product([i for i in range(1, n + 1)], repeat=m)

for e in p:
    print(" ".join(map(str, e)))
