import itertools

heights = []

for _ in range(9):
    heights.append(int(input()))

for i in itertools.combinations(heights, 7):
    if sum(i) == 100:
        for h in sorted(i):
            print(h)
        break
