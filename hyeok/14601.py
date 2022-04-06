# L - 트로미노
# 다시풀기 줫나게 어렵네
# 잘못생각함
import sys

input = sys.stdin.readline

K = int(input())

targetX, targetY = map(int, input().split())

coordinate = [[0]*(2**K) for _ in range(2**K)]

targetX, targetY = (2**K)-targetY, targetX-1

coordinate[targetX][targetY] = -1
# coordinate[(2**K)-targetY][targetX-1] = -1

print(coordinate)

count = 0


def tile(N, x, y):
    if N == 1:
        # 0인애 숫자 부여
        return
    # 배수구 어디있는지 찾아야하는뒙,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    # if
    gap = N//2
    tile(N-1, x, y)
    tile(N-1, x, y+gap)
    tile(N-1, x+gap, y)
    tile(N-1, x+gap, y+gap)
