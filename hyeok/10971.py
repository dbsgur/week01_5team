# 다시풀기

import sys
min_value = sys.maxsize
input = sys.stdin.readline

N = int(input())
w = []
visited = [False]*N
for i in range(N):
    w.append(list(map(int, input().split())))

result = []


# 틀렷습니다.
def sales(x, y, cost, startingPoint):
    """x 방문 횟수, y 어디 방문한지, cost 비용, startkingPoint 시작점"""
    # global result
    # if x == N:
    #     result.append(cost)
    #     return
    if x == N-1:
        if w[y][startingPoint] != 0:
            cost += w[y][startingPoint]
            # visited[startingPoint] = True
            # sales(x+1, startingPoint, cost, startingPoint)
            result.append(cost)
            # visited[startingPoint] = False
        return

    for i in range(N):
        if (visited[i] == False) and (w[y][i] != 0) and (i != startingPoint):
            # 방문
            cost += w[y][i]
            visited[y] = True
            sales(x+1, i, cost, startingPoint)
            visited[y] = False
            # min max 비교


for i in range(N):
    # for j in range(N):
    sales(0, i, 0, i)


result.append(min_value)


print(min(result))

print(result)
print(visited)
# print(maxN)
# print(minN)
