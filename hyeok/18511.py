# 다시 풀기

import sys

input = sys.stdin.readline
exit = sys.exit
N, amount = map(int, input().split())

K = [int(x) for x in input().split()]
K.sort(reverse=True)

number = N

# N = list(str(N))

# for i in range(len(N)):
#     N[i] = int(N[i])

# print(N)
# print("K : ", K)


aLength = len(str(N))

answer = 0
# order 자릿수, num 만들어진 수


def sol(order, num):
    global answer
    if order == aLength:
        if not '0' in str(num):
            answer = max(answer, num)
        return
    for i in K:
        tmp_num = i * (10**(aLength-order-1)) + num
        if tmp_num <= N:
            # 작으면 다음부터 무조건 가장 큰수 아닌가 ?...
            sol(order+1, tmp_num)
        else:
            sol(order+1, num)


sol(0, 0)
print(answer)
