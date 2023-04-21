import itertools

n, m = map(int, input().split())
iters = list(map(int, input().split()))
iters.sort()
p = itertools.combinations(iters, m)

for e in p:
    print(" ".join(map(str, e)))
