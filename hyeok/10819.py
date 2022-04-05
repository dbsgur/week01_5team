
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

A = [int(x) for x in input().split()]

visited = [False] * N

results = []


nPr = [x for x in permutations(A, N)]
answer = 0

for n in nPr:
    sumN = 0
    for i in range(N-1):
        sumN += abs(n[i+1] - n[i])
    if sumN > answer:
        answer = sumN

print(answer)

# FUCK U
# def dfs(arr, count, result):
#     # print("N ? :", count)
#     # print("result : ", result)
#     if count == N:
#         plz = result[:]
#         results.append(plz)
#         # print(plz)
#         return
#     else:
#         for i in range(N):
#             if arr[i] not in result:
#                 result.append(arr[i])
#                 dfs(arr, count+1, result)
#                 result.pop()


# def differ(arr):
#     sumN = 0
#     for i in range(N-1):
#         sumN += abs(arr[i] - arr[i+1])
#     return sumN


# for i in range(N):
#     result = [A[i]]
#     # visited[i] = True
#     dfs(A, 1, result)
#     # print(result)
#     # visited[i] = False

# # dfs(A, 1, [])

# # print(len(results))
# # print(results[1])


# maxN = 0
# for res in results:
#     num = differ(res)
#     if maxN < num:
#         maxN = num

# # print("results : ", results)
# # print("len(result): ", len(results))
# # print("results[1] : ", results[1])
# print(maxN)
