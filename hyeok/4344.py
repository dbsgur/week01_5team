import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    testCase = list(map(int, input().split()))
    avg = sum(testCase[1:]) / testCase[0]
    cnt = 0
    for score in testCase[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / testCase[0] * 100
    print(f'{rate:.3f}%')
    # average = sum / testCase[0]
    # print(average)
