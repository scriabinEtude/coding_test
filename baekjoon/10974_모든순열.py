import itertools

n = int(input())

for s in itertools.permutations([i for i in range(1, n + 1)], n):
    print(*s)
