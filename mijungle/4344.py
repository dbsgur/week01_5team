
import sys
input = sys.stdin.readline

nums = []
for i in range(N):
    a = list(map(int, input().split()))
    nums.append(a)

averarray = []
for i in range(N):
    aver = (sum(nums[i])-nums[i][0]) / nums[i][0]
    nums[i].append(aver)

ddd = []
for i in range(N):
    count = 0
    for j in range(1,len(nums[i])-1 ):
        if nums[i][j]>nums[i][-1]:
            count += 1
    ddd.append(count/nums[i][0])


for i in range(len(ddd)):
    ans = 100 * ddd[i]
    print(format(ans,'.3f')+'%')