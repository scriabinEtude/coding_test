import math

def isPrime(n: int):
    if(n == 1): return False
    
    sq = int(math.sqrt(n))
    for i in range(2, sq+1):
        if n % i == 0: return False
    
    return True

input()
total = 0
for n in list(map(int, input().split())):
    if isPrime(n):
        total += 1

print(total)
