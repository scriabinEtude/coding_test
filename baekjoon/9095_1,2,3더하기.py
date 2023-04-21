def find_sum_way(n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return find_sum_way(n - 1) + find_sum_way(n - 2) + find_sum_way(n - 3)


for _ in range(int(input())):
    print(find_sum_way(int(input())))
