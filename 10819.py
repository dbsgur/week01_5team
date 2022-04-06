import sys
from itertools import permutations

input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))

# n개의 정수로 이루어진 배열 a 정수 순서 적절히 [정렬]
# 얻을 수 있는 식 최대값 [중복없이 모든 경우의 수]
# permutations(list,개수)

arr.sort() #순서대로 정렬 

per= permutations(arr,n) #n개로 묶을 수 있는 경우의 수 >> 튜플
result = 0 #담을 공간

for i in per: #(1,4,8,10,15,20) >> 값을 꺼낸 것
    current=0
    for j in range(1,len(i)): #1~5까지
        current+=abs(i[j-1]-i[j]) #이전 수에서 현재 수를 뺀 값을 절대값 씌워서 current에 추가
    # if current>result:
    #     result=current
    result = max(current,result) #쌓인 reuslt 값과 current 중 최대값

print(result)