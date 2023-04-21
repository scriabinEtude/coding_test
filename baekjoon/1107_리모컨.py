from functools import reduce
import math
import sys

input = sys.stdin.readline


def size(n: int):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1


def canNumber(number: int, cant: list):
    for s in str(number):
        if int(s) in cant:
            return False
    return True


def findCanNumber(goal: int, cant: list):
    start = 100
    can = canNumber(goal, cant)
    number = 0
    min_op = abs(goal - start)
    if can:
        return size(goal)
    elif reduce(lambda a, b: a + b, cant) == 45 and cant.count(0) == 1:
        return min_op
    else:
        # i = 1
        # while True:
        #     if goal - i >= 0 and canNumber(goal - i, cant):
        #         number = goal - i
        #         break
        #     if canNumber(goal + i, cant):
        #         number = goal + i
        #         break
        #     i += 1
        # print(abs(goal - number), number, size(number))
        # return min(abs(goal - start), abs(goal - number) + size(number))
        for i in range(1000001):
            if canNumber(i, cant):
                min_op = min(min_op, abs(goal - i) + size(i))

        return min_op


# goal = int(input())
# cant = []

# if int(input()) != 0:
#     cant = list(map(int, input().split()))

goal = 5457
cant = [6, 7, 8]

print(findCanNumber(goal, cant))

goal = 100
cant = [0, 1, 2, 3, 4]

print(findCanNumber(goal, cant))

goal = 500000
cant = [0, 2, 3, 4, 6, 7, 8, 9]

print(findCanNumber(goal, cant))

goal = 100
cant = [1, 0, 5]

print(findCanNumber(goal, cant))

goal = 14124
cant = []

print(findCanNumber(goal, cant))

goal = 12305
cant = [5, 0]

print(findCanNumber(goal, cant))

goal = 500000
cant = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]

print(findCanNumber(goal, cant))
