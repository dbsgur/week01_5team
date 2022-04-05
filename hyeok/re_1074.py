import sys

input = sys.stdin.readline


N, r, c = map(int, input().split())

result = []


def zet(N, x, y):
    if N == 1:
        # 내마음속에 저장 ~?
        result.append()

    N //= 2
    zet(N, x, y)
    zet(N, x, y+N)
    zet(N, x+N, y)
    zet(N, x+N, y+N)
