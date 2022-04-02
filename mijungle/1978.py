import sys, math

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for num in nums:
    count = 0
    if num ==1:
        ans +=1
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            count += 1
    if count == 0:
        ans += 1
print(ans)


