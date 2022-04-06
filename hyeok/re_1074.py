import sys

input = sys.stdin.readline


N, r, c = map(int, input().split())

result = []

count = 0


def zet(N, x, y):
    global count
    if x == r and y == c:
        print(count)
        exit(0)
    if N == 1:
        # 내마음속에 저장 ~?
        count += 1
        return
    if not(x <= r < x+N and y <= c < y+N):
        count += (N*N)
        return
    N //= 2
    zet(N, x, y)
    zet(N, x, y+N)
    zet(N, x+N, y)
    zet(N, x+N, y+N)


zet(2**N, 0, 0)
# print(count-1)
