import sys

input = sys.stdin.readline

N = int(input())

Q = [0]*N
# print(Q)
count = 0


def check(x):
    for i in range(x):
        if Q[x] == Q[i] or (x-i == abs(Q[x] - Q[i])):
            return False
    return True


def nQueen(x):
    global count
    if x == N:
        count += 1
        # return
    else:
        for i in range(N):
            Q[x] = i
            # for j in range(x):
            #     if Q[x] == Q[j] or (x-j == abs(Q[x] - Q[j])):
            #         break
            # if Q[x] != Q[j] and (x-j != abs(Q[x]-Q[j])):
            if check(x):
                nQueen(x+1)


nQueen(0)
print(count)
