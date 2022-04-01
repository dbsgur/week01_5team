import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    # print(S)
    # print(R)
    for i in S:
        # print(i)
        # print(R)
        print(i*R, end='')
    print()
