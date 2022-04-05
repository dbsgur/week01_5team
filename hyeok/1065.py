import sys
input = sys.stdin.readline


N = int(input())

count = 99
if N < 100:
    print(N)
else:
    for i in range(100, N+1):
        numsList = [int(x) for x in str(i)]
        # print(numsList)
        if numsList[2]-numsList[1] == numsList[1]-numsList[0]:
            count += 1

    print(count)
