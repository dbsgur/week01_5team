# 다시 풀기
import sys

input = sys.stdin.readline

# 에라토스테네스의 체
primeNumber = [0 for i in range(10001)]

T = int(input())

primeNumber[1] = 1
for i in range(2, 98):
    for j in range(i*2, 10001, i):
        primeNumber[j] = 1


for i in range(T):
    num = int(input())
    half = num // 2
    for j in range(half, 1, -1):
        if primeNumber[j] == 0 and primeNumber[num-j] == 0:
            print(j, num-j)
            break
