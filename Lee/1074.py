import sys

input = sys.stdin.readline

n,r,c=map(int, input().split())
# n은 탐색횟수

# 배열을 크기가 2^N-1 × 2^N-1로 4등분 한 후에 재귀적으로 순서대로 방문
# **은 좌항을 우항으로 거듭 제곱 ex. 3**4 == 3^4=81 입니다~
# //는 좌항을 우항으로 나누는 것이고, 결과값은 정수형으로 출력됨! 
# ex. 3//4 == 3/4 인데 정수형이라 값이 '0'만 출력됩니다.
# 네모 z순으로 '2사분면 > 1사분면 > 3사분면 > 4사분면'으로 그려집니다.

count = 0
while n>1:
    size = (2**n)//2
    if r < size and c < size: # 2사분면 시작=좌표 수정 이유x
        pass
    elif r < size and c >= size: # 1사분면
        count += size**2
        c -= size # 말그대로 1사분면이 2사분면 기준에서 c로 움직움직
    elif r >= size and c < size: # 3사분면
        count += size**2*2
        r -= size
    elif r >= size and c >= size: # 4사분면
        count += size**2*3
        r-=size # 2사분면 기준에서 (r,c) 둘 다 움직임!
        c-=size
    n -=1 # 탐색 돌면 -1로 횟수 없애줌

if r == 0 and c == 0:
    print(count)
if r == 0 and c == 1:
    print(count+1)
if r == 1 and c == 0:
    print(count+2)
if r == 1 and c == 1:
    print(count+3)


#재귀를 할 땐 종료시점 넣어줘야하고...
# def recur(count,next,visited):
#     if count == n:
#         return #애초에 이 횟수랑 같을때 리턴이 맞을까?ㅋㅋ

    
    

# 돌려야 하고
# 전역변수? 방문한 곳 표시해줘야하고

#함수(값) 넣어주고...