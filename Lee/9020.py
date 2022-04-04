import sys

input = sys.stdin.readline

t = int(input()) #범위 설정

#내가 하고싶었던 것
#ex.8이면 8의 소수를 다 찾아서 리스트에 넣고 [이때 수는 int형] >> [1,3,5,7]
#중간지점을 출력하는 거 [이 식 설계를 못하겠음..ㅠ]

che = [True]*t


for i in range(t):
    even=int(input()) #t범위 만큼 정수로 input

    #다시 풀어보기 골바..