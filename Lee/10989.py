# 다시 풀기!!!
import sys

input = sys.stdin.readline

n=int(input())

li=[0] * 50
for i in range(n):
    li[int(input())]+=1

# print("#############")

for i in range(50): #i에는 0~49가 담겼어요
    if li[i] !=0: # 0이 아닌 값들을
        # 갯수가 1 이상이면 중복된만큼 출력
        for ii in range(li[i]): #li[i] == 개수
            print(i)