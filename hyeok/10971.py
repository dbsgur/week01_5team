import sys

input = sys.stdin.readline

N = int(input())

# w = [list(map(int, input().split())) for _ in range(N)]
w = [[int(x) for x in input().split()] for _ in range(N)]


min_value = 1e9

# print(w)


def dfs(next, start, cost, visited):
    global min_value

    if len(visited) == N:
        # 방문 완료
        if w[next][start] != 0:
            # 갈수 잇다면~?
            min_value = min(cost+w[next][start], min_value)
        return
    else:
        for i in range(N):
            if i not in visited and w[next][i] != 0 and cost < min_value:
                visited.append(i)
                dfs(i, start, cost+w[next][i], visited)
                visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])

print(min_value)
