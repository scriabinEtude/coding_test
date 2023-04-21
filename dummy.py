import math

N = 30
sqrt = int(math.sqrt(N))  # 중앙값 5.477.. => 5

measures = set()

for i in range(1, sqrt + 1):
    if N % i == 0:
        measures.add(i)
        measures.add(int(N / i))  # 중앙값보다 작거나 같은값으로 나눈 값

print(measures)  # {1, 2, 3, 5, 6, 10, 15, 30}
