from itertools import permutations


def cal(l: list):
    total = 0
    for i in range(len(l) - 1):
        total += abs(l[i] - l[i + 1])
    return total


n = int(input())
a = permutations(list(map(int, input().split())))

max_value = 0

for l in a:
    max_value = max(max_value, cal(l))

print(max_value)
