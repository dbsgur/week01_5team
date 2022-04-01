import sys

input = sys.stdin.readline

n=int(input())

for i in range(n): #n번까지 돌림
    a= list(input().strip()) #strip 공백 제거
    score = 0 # for문 위에다 변수를 주어야지만 담길 수 있음.... ㅂㄷㅂㄷ
    result = 0
    for ai in a:
        if ai == 'O': #ai에 O이 있을 경우
            score+=1 #score에 1을 추가하고
            result+=score #결과값에 score를 더해
        else: #없을 경우
            score=0 #score는 0임
    print(result)