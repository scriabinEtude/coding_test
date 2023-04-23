def next(l: list[int]):
    for y in range(len(l) - 1, 0, -1):
        if l[y - 1] < l[y]:
            x = y - 1
            for i in range(len(l) - 1, 0, -1):
                if l[x] < l[i]:
                    l[x], l[i] = l[i], l[x]
                    print(*(l[:y] + sorted(l[y:])))
                    exit()

    print(-1)


input()
l = list(map(int, input().split()))
next(l)
