import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

max = max(nums)
print(max)
print(nums.index(max) + 1)
