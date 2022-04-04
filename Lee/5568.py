import sys
from itertools import permutations

#list에 있는 값들의 모든 조합을 구하기 위한 방법
# 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations, combinations을 사용

input=sys.stdin.readline

n=int(input())
k=int(input())

# for i in range(n):
#     cards=[input().strip()]
cards=[input().strip() for i in range(n)]

result = set()
for per in permutations(cards,k):
    result.add(''.join(per)) #잘린거 문자 합치고 result에 담기

print(len(result))

# cardList = []
# for ni in range(n):
#     card = int(input().strip())
#     cardList.append(card) #[72, 2, 12, 7, 2, 1]

# print(cardList)
# result = list(permutations(cardList,k))
# print(len(set(result)))

# print(len(result))
#k장을 선택해서 만듦, 근데 이거 중복이 생겨서 set()함수 이용해서 제거 해줌