import sys

input = sys.stdin.readline

K = int(input())

# start에서 to로 via를 거쳐 총 N개의 원반을 운반할 때


def hanoi(N, start, to, via):
    # global count
    if N == 1:
        print(start, to, sep=' ')
        # result.append([start, to])
        # count += 1
    else:
        hanoi(N-1, start, via, to)
        print(start, to, sep=' ')
        # result.append([start, to])
        # count += 1
        hanoi(N-1, via, to, start)


# hanoi(K, 1, 3, 2)
# print(count)
# print(result)
# first TRY
# for answer in result:
#     # print(' '.join(str(answer)))
#     print(answer[0], answer[1])

print(2**K-1)
if K <= 20:
    hanoi(K, 1, 3, 2)
