_ = input()
numbers: list = list(map(int, input().rstrip().split()))

min = min(numbers)
max = max(numbers)
print(min * max)