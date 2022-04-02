# 다시 풀기 시간초과
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())

count = 0
row = [0]*(N+1)


def check(x):
    for i in range(x):
        if row[x] == row[i] or (x-i == abs(row[x] - row[i])):
            return False
    return True


def nQueens(x):
    global count
    if x == N:
        count += 1
        return
    else:
        for i in range(N):
            # if check(i):
            #     continue
            row[x] = i
            if check(x):
                nQueens(x+1)


nQueens(0)
print(count)


# N = int(sys.stdin.readline())
# count = 0


# def logic(n):
#     if n == N:
#         global count
#         count += 1
#     else:
#         for i in range(N):
#             if visited[i]:
#                 continue
#             board[n] = i  # (n, i)에 퀸 놓기

#             if check(n):  # 퀸 놓기 조건에 맞다면
#                 visited[i] = True
#                 logic(n+1)  # 다음 행으로 넘어가기
#                 visited[i] = False


# def check(n):
#     for i in range(n):
#         if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):
#             return False

#     return True


# board = [0 for _ in range(N)]  # 인덱스 번호 == 행, 인덱스 값 ==열
# visited = [False for _ in range(N)]

# logic(0)
# print(count)
