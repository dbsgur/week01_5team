import sys
import copy
input = sys.stdin.readline

N = int(input())

table = [[int(x) for x in input().split()]for _ in range(N)]

# tmpList = []
# result = []


def raffle(N, x, y):
    if N == 2:
     #       realLast = [table[x][y], table[x][y+1],
        #                    table[x+1][y], table[x+1][y+1]]
        return select([table[x][y], table[x][y+1],
                       table[x+1][y], table[x+1][y+1]])
    N = N//2
   # num1 = raffle(N, x, y)
  #  num2 = raffle(N, x, y+N)
 #   num3 = raffle(N, x+N, y)
#    num4 = raffle(N, x+N, y+N)
    return select([raffle(N, x, y), raffle(N, x, y+N), raffle(N, x+N, y), raffle(N, x+N, y+N)])


def select(arr):
    arr.sort()
    return arr[1]


# def divide(arr):
#     tmpList2 = []
#     if len(arr) == 1:
#         print(arr[0])
#         return
#     for i in range(0, N, 4):
#         result = copy.deepcopy(arr[i:i+4])
#         tmpList2.append(select(result))
#     divide(tmpList2)


print(raffle(N, 0, 0))
# divide(tmpList)


# print(select([1, 23, 34, 5]))

# 8
# 1 2 3 4 5 6 7 8
# 0 9 10 11 12 13 14 15
# 16 17 18 19 20 21 22 23
# 25 26 27 28 29 30 31 32
# 34 35 36 37 38 39 40 41
# 24 33 42 43 44 45 46 47
# 48 49 50 51 52 53 54 55
# 56 57 58 59 60 61 62 63

##################
# [1, 4,17, 19,6,8,21 ,23, 33, 37,49, 51, 39, 41, 53, 55] 16개
# [4, 8, 37, 41] 4개
