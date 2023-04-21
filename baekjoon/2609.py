a, b = map(int, input().split())

min = min(a, b)
max = max(a, b)

while(True):
    mod = max % min 
    if mod != 0:
        max = min
        min = mod
    else :
        print(min)
        print(int(a * b / min))
        break