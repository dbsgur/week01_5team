import sys
import itertools

input = sys.stdin.readline


talls = [int(input()) for _ in range(9)]

talls.sort()

result = list(itertools.combinations(talls, 7))

for num in result:
    nums = sum(num)
    if nums == 100:
        for n in num:
            print(n)
        break


# result = talls[i:i+7]

# print(result)
