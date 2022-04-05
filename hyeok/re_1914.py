import sys

input = sys.stdin.readline

N = int(input())

# N 원판 갯수 start에서 via를 거쳐서 to로 이동


def hanoi(N, start, to, via):
    if N == 1:
        print(start, to, sep=' ')
    else:
        hanoi(N-1, start, via, to)
        print(start, to, sep=' ')
        hanoi(N-1, via, to, start)


print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)
