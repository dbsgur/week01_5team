# import sys
# import itertools

# input = sys.stdin.readline

# n = int(input())

# k = int(input())

# nums = [input().strip() for _ in range(n)]

# nPr = list(map(''.join, itertools.permutations(nums, k)))

# nPr = [int(x) for x in nPr]
# nPr = list(set(nPr))
# print(len(nPr))

import sys

input = sys.stdin.readline

n = int(input())

k = int(input())

# 카드 쓴지 여부
visited = [False]*n

nums = [input().strip() for _ in range(n)]

results = []

# arr 남은 숫자 배열, count 몇개 뽑았는지


def cards(arr, count, result):
    if count == k:
        results.append(result)
        return

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            cards(arr, count+1, result+arr[i])
            visited[i] = False


for i in range(n):
    # print(nums[i])
    visited[i] = True
    cards(nums, 1, nums[i])
    visited[i] = False


results = len(list(set(map(int, results))))

print(results)
