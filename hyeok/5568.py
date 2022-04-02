import sys
import itertools

input = sys.stdin.readline

n = int(input())

k = int(input())

nums = [input().strip() for _ in range(n)]

nPr = list(map(''.join, itertools.permutations(nums, k)))

nPr = [int(x) for x in nPr]
nPr = list(set(nPr))
print(len(nPr))
