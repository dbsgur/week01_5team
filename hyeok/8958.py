import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    testCase = input()
    sum = 0
    c = 1
    for i in testCase:
        if i == 'O':
            sum += c
            c += 1
        elif i == 'X':
            c = 1
    print(sum)
