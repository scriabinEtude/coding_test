from itertools import combinations

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break

    n = a[0]
    a = a[1:]
    for _ in combinations(a, 6):
        print(*_)
    print()
