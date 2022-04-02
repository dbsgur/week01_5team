# 다시 풀기

import sys

input = sys.stdin.readline

N = int(input())

checkList = [0] * 10001

# ~~

for i in range(N):
    num = int(input())
    checkList[num] += 1


for i in range(10001):
    if checkList[i] > 0:
        for _ in range(checkList[i]):
            print(i)
