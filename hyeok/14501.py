import sys

input = sys.stdin.readline

N = int(input())

T = [0]*(N)
P = [0]*(N)

for i in range(N):
    T[i], P[i] = map(int, input().strip().split())


dp = [x for x in P]
dp.append(0)

for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])

print(dp[0])

# fucking dfs !!!
# # print(a, b)
# print(T)
# print(P)

# max_value = 0

# def dfs(day, cost):
#     global max_value
#     if day <= N:
#         max_value = max(max_value, cost)
#     for i in range(day+1, N+1):
#         # 되는조건
#         print("###")
#         print("T[", i, "] : ", T[i], day)
#         print("###")
#         if (day + T[i] <= N) and (max_value < cost + P[i]) and (i+T[i]-1 <= N):
#             print("T[", i, "] : ", T[i], day)
#             print("P[", i, "] : ", P[i])
#             dfs(day + T[i], cost + P[i])

# dfs(0, 0)

# print(max_value)

# 7
# 1 1
# 6 2
# 1 1
# 1 1
# 1 1
# 1 1
# 1 200
