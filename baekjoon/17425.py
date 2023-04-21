MAX = 1000000
dp = [1] * (MAX + 1)
s = [0] * (MAX + 1)
s[1] = 1

for i in range(2, MAX + 1):
    for j in range(i, MAX +1, i):
        dp[j] += i
    s[i] = s[i-1] + dp[i]
        
n = int(input())
for _ in range(n):
    number = int(input())
    print(s[number])