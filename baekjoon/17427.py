import math
from functools import reduce

n = int(input())

sum = 0
for i in range(1, n+1):
    sum += (n//i)*i

print(sum)