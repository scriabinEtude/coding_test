import itertools

n, m = map(int, input().split())
iters = list(map(int, input().split()))
iters.sort()
p = itertools.combinations_with_replacement(iters, m)

for e in p:
    print(" ".join(map(str, e)))
