# 다시 풀기

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

A = [int(x) for x in input().split()]

visited = [False] * N

results = []

# nPr = [x for x in permutations(A, N)]
# answer = 0

# for n in nPr:
#     sumN = 0
#     for i in range(N-1):
#         sumN += abs(n[i+1] - n[i])
#     if sumN > answer:
#         answer = sumN

# print(answer)


def dfs(arr, count, result):
    # print("N ? :", count)
    if count == N:
        results.append(result)
        return
    else:
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                result.append(arr[i])
                dfs(arr, count+1, result)
                visited[i] = False
        result.remove(arr[-1])


def differ(arr):
    sumN = 0
    for i in range(len(arr)-2):
        sumN += arr[i] + arr[i+1]
    return sumN


for i in range(N):
    result = [A[i]]
    visited[i] = True
    dfs(A, 1, result)
    # print(result)
    visited[i] = False

# dfs(A, 1, [])

print(len(results))
print(results[1])


maxN = -1e9
for res in results:
    num = differ(res)
    if maxN < num:
        maxN = num

# print(results[1])
