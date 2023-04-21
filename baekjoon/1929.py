import math

def isPrime(n: int):
    if(n == 1): return False
    
    sq = int(math.sqrt(n))
    for i in range(2, sq+1):
        if n % i == 0: return False
    
    return True

m, n = list(map(int, input().split()))

for i in range(m, n+1):
    if isPrime(i) :
        print(i)