import sys

input = sys.stdin.readline

N, X = map(int, input().split())

# nums = list(map(int, input().split()))

nums = [int(x) for x in input().split()]

for num in nums:
    if num < X:
        print(num, end=' ')

print()
