import math

# N = int(input())


# def sol(N):
#     if N < 10:
#         print(N)
#         return

#     size = int(math.log10(N) + 1)
#     dp = [9]
#     for i in range(2, size):
#         dp.append(dp[-1] + (i * 9 * (10 ** (i - 1))))

#     print(dp[-1] + (size * (N - (10 ** (size - 1) - 1))))


# sol(5)
# sol(15)
# sol(120)

n = input()
k = 0

for i in range(len(n)):
    k += int(n) - (10**i) + 1
    print(n, i, k)
# print(k)
