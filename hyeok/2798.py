
import sys

N, M = map(int, (sys.stdin.readline().strip().split()))

nums = list(map(int, sys.stdin.readline().strip().split()))

max_sum = 0
nums.sort()

for i in range(0, N-2):
    left = i + 1
    right = N - 1
    # N-1?

    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < M:
            max_sum = max(max_sum, sum)
            left += 1
        elif sum > M:
            right -= 1
        else:
            print(M)
            sys.exit(0)


print(max_sum)

# import sys
# from itertools import combinations

# input = sys.stdin.readline

# N, M = map(int, input().split())

# cards = [int(x) for x in input().split()]

# result = list(combinations(cards, 3))

# minN = M

# for res in result:
#     # print(abs(M-sum(res)))
#     if M - sum(res) >= 0:
#         minN = min(minN, M-sum(res))

# print(M-minN)
