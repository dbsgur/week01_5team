# 다시 풀기

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

A = [int(x) for x in input().split()]

nPr = [x for x in permutations(A, N)]
answer = 0

for n in nPr:
    sumN = 0
    for i in range(N-1):
        sumN += abs(n[i+1] - n[i])
    if sumN > answer:
        answer = sumN

print(answer)
