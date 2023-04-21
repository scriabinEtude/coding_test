import sys
input = sys.stdin.readline

MAX = 1000000
dp =[ False if i % 2 == 0 else True for i in range(MAX+1) ]
dp[1] = False
dp[2] = False

for i in range(3, MAX+1, 2):
    if dp[i]:
        for j in range(2* i, MAX+1, i):
            dp[j] = False


def findSum(n):
    for i in range(3, int(MAX+1 / 2)):
        if dp[i] and dp[n-i]:
            print(f"{n} = {i} + {n-i}")
            return
    
    print("Goldbach's conjecture is wrong.")
    return

while(True):
    n = int(input())
    if(n == 0): exit()
    findSum(n)