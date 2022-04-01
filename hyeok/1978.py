import math
import sys

input = sys.stdin.readline


N = int(input())

nums = [int(x) for x in input().split()]

answer = N
for num in nums:
    if num == 1:
        answer -= 1
        continue
    elif (num == 2) or (num == 3):
        pass
    else:
        sqrt = math.ceil(math.sqrt(num))

        for i in range(2, sqrt+1):

            if num % i == 0:
                answer -= 1
                break

print(answer)
